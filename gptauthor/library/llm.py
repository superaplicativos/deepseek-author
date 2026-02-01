from datetime import datetime

from joblib import Memory
from loguru import logger
from omegaconf import DictConfig
from openai import AuthenticationError, OpenAI
from tenacity import retry, retry_if_not_exception_type, stop_after_attempt, wait_exponential

from .classes import AppUsageException

# Optional import; present when using Anthropic provider
try:
    from anthropic import Anthropic
except Exception:
    Anthropic = None  # type: ignore

memory = Memory(".joblib_cache", verbose=0)


def log_retry(state):
    msg = (
        f"Tenacity retry {state.fn.__name__}: {state.attempt_number=}, {state.idle_for=}, {state.seconds_since_start=}"
    )
    if state.attempt_number < 1:
        logger.warning(msg)
    else:
        logger.exception(msg)


@memory.cache()
@retry(
    wait=wait_exponential(multiplier=2, min=10, max=600),
    stop=stop_after_attempt(3),
    before_sleep=log_retry,
    retry=retry_if_not_exception_type(AppUsageException),
)
def make_call(system: str, prompt: str, llm_config: DictConfig) -> tuple[str, int]:
    provider = (llm_config.get("provider") or "openai").lower()
    start = datetime.now()

    try:
        if provider == "anthropic":
            if Anthropic is None:
                raise AppUsageException("Anthropic library not installed. Please add 'anthropic' dependency.")

            client = Anthropic(api_key=llm_config.api_key)
            max_tokens = llm_config.get("max_tokens") or 1024
            api_response = client.messages.create(
                model=llm_config.model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": prompt}],
                temperature=llm_config.temperature,
            )

            chat_response = "".join([c.text for c in api_response.content if hasattr(c, "text")])
            usage = getattr(api_response, "usage", None)
            if usage and hasattr(usage, "input_tokens") and hasattr(usage, "output_tokens"):
                total_tokens = int(usage.input_tokens) + int(usage.output_tokens)
            else:
                total_tokens = -1

        else:
            client = OpenAI(
                api_key=llm_config.api_key if not llm_config.use_localhost else "localhost",
                base_url="http://localhost:8081" if llm_config.use_localhost else (llm_config.get("base_url") or None),
            )
            messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]

            kwargs = {
                "model": llm_config.model,
                "messages": messages,
                "temperature": llm_config.temperature,
                "top_p": llm_config.top_p,
            }
            if llm_config.get("max_tokens"):
                kwargs["max_tokens"] = llm_config.max_tokens
            api_response = client.chat.completions.create(**kwargs)

            chat_response = api_response.choices[0].message.content
            total_tokens = int(api_response.usage.total_tokens)

    except AuthenticationError as ex:
        raise AppUsageException(str(ex)) from ex
    except Exception as ex:
        raise AppUsageException(str(ex)) from ex

    took = datetime.now() - start

    logger.debug(f"{llm_config.use_localhost=}")
    logger.debug(f"{system=}")
    logger.debug(f"{prompt=}")
    logger.debug(f"{took=}")
    logger.debug("\n---- RESPONSE:")
    logger.debug(f"{chat_response=}")
    logger.debug(f"{total_tokens=}")

    return chat_response, total_tokens
