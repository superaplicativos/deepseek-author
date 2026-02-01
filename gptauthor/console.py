from typing import Optional

import typer
from loguru import logger
from omegaconf import OmegaConf
from rich import print
from typing_extensions import Annotated

from .library import consts, engine, env, log
from .library.classes import AppUsageException

typer_app = typer.Typer()


def version_callback(value: bool):
    if value:
        print(f"{consts.package_name} version: {consts.version}")
        print("Please visit https://github.com/dylanhogg/gptauthor for more info.")
        raise typer.Exit()


@typer_app.command()
def run(
    story: Annotated[str, typer.Option(help="The name of the yaml file defining the story and prompts")],
    llm_provider: Annotated[
        str,
        typer.Option(
            help="LLM provider: openai | deepseek | openrouter | anthropic",
        ),
    ] = "openai",
    llm_model: Annotated[str, typer.Option(help="The model name")] = consts.default_llm_model,
    llm_temperature: Annotated[
        float, typer.Option(help="LLM temperature value (0 to 2, OpenAI default is 1)")
    ] = consts.default_llm_temperature,
    llm_top_p: Annotated[
        float, typer.Option(help="LLM top_p probability value (0 to 2, OpenAI default is 1)")
    ] = consts.default_llm_top_p,
    llm_use_localhost: Annotated[
        int, typer.Option(help="LLM use localhost:8081 instead of openai")
    ] = consts.default_llm_use_localhost,
    llm_base_url: Annotated[
        str, typer.Option(help="LLM base URL for OpenAI-compatible providers (e.g., https://api.deepseek.com)")]
    = consts.default_llm_base_url,
    llm_api_key: Annotated[
        str,
        typer.Option(
            help="LLM API key override (if not set via environment variable)",
        ),
    ] = "",
    llm_max_tokens: Annotated[
        int, typer.Option(help="LLM max tokens per response (provider-specific limit)")] = 0,
    total_chapters: Annotated[int, typer.Option(help="Total chapters to write")] = consts.default_write_total_chapters,
    allow_user_input: Annotated[bool, typer.Option(help="Allow command line user input")] = True,
    version: Annotated[
        Optional[bool],
        typer.Option("--version", help=f"Display {consts.package_name} version", callback=version_callback),
    ] = None,
) -> None:
    """
    gptauthor entry point
    """

    try:
        log.configure()
        example_usage = f"Example usage: [bold green]{consts.package_name} --story prompts-openai-drama --total-chapters 3 --llm-model gpt-3.5-turbo --llm-temperature 0.1 --llm-top-p 1.0[/bold green]"

        provider = llm_provider.lower()
        if not llm_api_key:
            if provider == "openai":
                llm_api_key = env.get("OPENAI_API_KEY", "")
            elif provider == "deepseek":
                llm_api_key = env.get("DEEPSEEK_API_KEY", "")
            elif provider == "openrouter":
                llm_api_key = env.get("OPENROUTER_API_KEY", "")
            elif provider == "anthropic":
                llm_api_key = env.get("ANTHROPIC_API_KEY", "")
            else:
                llm_api_key = env.get("OPENAI_API_KEY", "")  # fallback

        if not llm_use_localhost and not llm_api_key:
            raise AppUsageException(
                "Expected an environment variable for the selected provider to be set."
                "\nOpenAI: set OPENAI_API_KEY"
                "\nDeepSeek: set DEEPSEEK_API_KEY"
                "\nOpenRouter: set OPENROUTER_API_KEY"
                "\nAnthropic (Claude): set ANTHROPIC_API_KEY"
                "\nAlternatively you can use the '--llm_use_localhost 1' argument to use a local OpenAI-compatible LLM server."
            )

        story_file = f"{story}.yaml"
        base_url_value = llm_base_url or env.get("LLM_BASE_URL", "")
        llm_config = OmegaConf.create(
            {
                "version": consts.version,
                "api_key": llm_api_key,
                "provider": provider,
                "model": llm_model,
                "temperature": llm_temperature,
                "top_p": llm_top_p,
                "total_chapters": total_chapters,
                "use_localhost": llm_use_localhost,
                "localhost_sleep": int(env.get("LLM_USE_LOCALHOST_SLEEP", 0)),
                "default_output_folder": consts.default_output_folder,
                "story_file": story_file,
                "allow_user_input": allow_user_input,
                "base_url": base_url_value,
                "max_tokens": llm_max_tokens,
            }
        )

        engine.do_writing(llm_config)
        raise typer.Exit(0)

    except AppUsageException as ex:
        print(example_usage)
        print(f"[bold red]{str(ex)}[/bold red]")
        print("")
        print(f"For more information, try '{consts.package_name} --help'.")
        logger.exception(ex)

    except typer.Exit as ex:
        if ex.exit_code == 0:
            print()
            print(
                "[bold green]Goodbye and thanks for using gptauthor! Please visit https://github.com/dylanhogg/gptauthor for more info.[/bold green]"
            )
            return
        print(example_usage)
        print(f"[bold red]Unexpected error code: {str(ex)}[/bold red]")
        print("")
        print(f"For more information, try '{consts.package_name} --help'.")
        logger.exception(ex)

    except Exception as ex:
        print(example_usage)
        print(f"[bold red]Unexpected exception: {str(ex)}[/bold red]")
        print("")
        print(f"For more information, try '{consts.package_name} --help'.")
        logger.exception(ex)
