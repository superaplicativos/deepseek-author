# DeepSeekAuthor (Fork with Multi‑Provider Support)

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/gptauthor.svg?1)](https://badge.fury.io/py/gptauthor)
[![Build](https://github.com/dylanhogg/gptauthor/workflows/build/badge.svg)](https://github.com/dylanhogg/gptauthor/actions/workflows/python-poetry-app.yml)
[![Latest Tag](https://img.shields.io/github/v/tag/dylanhogg/gptauthor)](https://github.com/dylanhogg/gptauthor/tags)
[![Downloads](https://static.pepy.tech/badge/gptauthor)](https://pepy.tech/project/gptauthor)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/gptauthor/blob/master/notebooks/gptauthor_colab_custom_story.ipynb)

This repository is a fork of [dylanhogg/gptauthor](https://github.com/dylanhogg/gptauthor), enhanced to work not only with OpenAI‑compatible models (like DeepSeek and OpenRouter) but also with Claude (Anthropic). In our practical experience, Claude often delivers more consistent and higher‑quality writing.

DeepSeekAuthor is a command‑line tool for long‑form, multi‑chapter stories from a structured prompt. Multi‑provider support: OpenAI, DeepSeek, OpenRouter, and Anthropic (Claude).

![Header image](https://github.com/dylanhogg/gptauthor/blob/main/docs/img/header.jpg?raw=true)

## How It Works

- Human‑written story description: outline, style, and characters in a YAML file ([example](https://github.com/dylanhogg/gptauthor/blob/main/gptauthor/prompts-openai-drama.yaml)).
- Run the tool: choose model, temperature, and number of chapters.
- AI‑generated synopsis: turns your prompt into a chapter‑level synopsis.
- Human review of the synopsis: optionally edit before continuing.
- Iterative chapter writing: each chapter uses the shared synopsis and the previous chapter. Outputs in Markdown/HTML under `./_output/`.

## Example Outputs

- [OpenAI leadership crisis (Nov/2023)](https://github.com/dylanhogg/gptauthor/blob/main/samples/openai-drama-20240131-224810-v0.5.0-gpt-4-0125-preview.md)
- [Echoes of Atlantis](https://github.com/dylanhogg/gptauthor/blob/main/samples/echoes-of-atlantis--v1.0.0-gpt-4-0125-preview.md)

## Installation

Install [gptauthor](https://pypi.org/project/gptauthor/) via pip (preferably in a Python virtual environment).

```bash
pip install gptauthor
```

Or run the sample notebook on Google Colab:

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/gptauthor/blob/master/notebooks/gptauthor_colab_custom_story.ipynb)

## Run

### Quick Start and API Key

OpenAI example:

```bash
# Mac/Linux
export OPENAI_API_KEY="sk-<your_key>"
# Windows
setx OPENAI_API_KEY "sk-<your_key>"

gptauthor --story prompts-openai-drama --total-chapters 3 --llm-model gpt-3.5-turbo --llm-temperature 0.1
```

Note: Claude (Anthropic) often yields better long‑form writing quality. Try different providers/models for your use case.

### Required Arguments

- `--story TEXT`: Name of the YAML file defining the story and prompts

### Optional Arguments

- `--llm-provider TEXT`: LLM provider: openai | deepseek | openrouter | anthropic [default: openai]
- `--llm-model TEXT`: Model name [default: gpt-3.5-turbo]
- `--llm-temperature FLOAT`: Temperature (0 to 2) [default: 1]
- `--llm-top-p FLOAT`: Top‑p (0 to 2) [default: 1]
- `--llm-use-localhost INTEGER`: Use localhost:8081 (OpenAI‑compatible) [default: 0]
- `--llm-base-url TEXT`: Base URL for OpenAI‑compatible providers (e.g., https://api.deepseek.com)
- `--llm-api-key TEXT`: API key override (if not using environment variables)
- `--llm-max-tokens INTEGER`: Max tokens per response (provider‑specific)
- `--total-chapters INTEGER`: Total chapters [default: 3]
- `--allow-user-input / --no-allow-user-input`: Allow terminal input [default: allow-user-input]
- `--version`: Show version
- `--help`: Show help

## Output Files

- Progress and final output in `./_output/<prompt>/<model>/<date>-<params>-<title>/`
- Main files: `_whole_book.md` (Markdown) and `_whole_book.html` (HTML)

## Creating Your Own Prompts

- Copy and edit the [prompts-openai-drama.yaml](https://github.com/dylanhogg/gptauthor/blob/main/gptauthor/prompts-openai-drama.yaml) example
- Run in the same directory as your YAML:

```bash
export OPENAI_API_KEY="sk-<your_key>"
gptauthor --story prompts-my-story --total-chapters 5 --llm-model gpt-3.5-turbo --llm-temperature 0.1
```

## Multi‑Provider Support

Supports OpenAI‑compatible providers via `base_url` (OpenAI, DeepSeek, OpenRouter) and Anthropic (Claude).

- OpenAI: `OPENAI_API_KEY`
- DeepSeek: `DEEPSEEK_API_KEY` and `LLM_BASE_URL=https://api.deepseek.com`
- OpenRouter: `OPENROUTER_API_KEY` and `LLM_BASE_URL=https://openrouter.ai/api/v1`
- Anthropic (Claude): `ANTHROPIC_API_KEY`

DeepSeek example:

```bash
# Windows
setx DEEPSEEK_API_KEY "<your_deepseek_key>"
setx LLM_BASE_URL "https://api.deepseek.com"
# Run
gptauthor --story prompts-openai-drama --llm-provider deepseek --total-chapters 3 --llm-model deepseek-chat --llm-temperature 0.1 --llm-base-url https://api.deepseek.com
```

Anthropic / Claude example:

```bash
# Windows
setx ANTHROPIC_API_KEY "<your_anthropic_key>"
# Mac/Linux
# export ANTHROPIC_API_KEY="<your_anthropic_key>"

gptauthor --story prompts-openai-drama --llm-provider anthropic --total-chapters 3 --llm-model claude-3-7-sonnet --llm-temperature 0.1 --llm-max-tokens 4096
```

Notes:
- OpenAI‑compatible providers use `--llm-base-url`. Anthropic does not require `base_url`.
- `--llm-use-localhost 1` allows using a local OpenAI‑compatible server (e.g., vLLM at `http://localhost:8081`).
- Claude often provides better quality in long‑form narratives.

## Known Issues

- Occasional provider API errors; restart the app (responses are cached for identical parameters).
- Chapter continuity can vary due to the iterative approach (synopsis + previous chapter).
- Windows path differences may occur; please report issues.
- Token cost estimation is approximate; confirm in your provider billing.
- Use AI responsibly.

## Contributing

- Fork the repository
- Create a branch for your feature/fix
- Commit your changes
- Open a Pull Request with a clear description

## License

Licensed under [MIT](https://github.com/dylanhogg/gptauthor/blob/main/LICENSE).

---

# Versão em Português

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/gptauthor.svg?1)](https://badge.fury.io/py/gptauthor)
[![Build](https://github.com/dylanhogg/gptauthor/workflows/build/badge.svg)](https://github.com/dylanhogg/gptauthor/actions/workflows/python-poetry-app.yml)
[![Latest Tag](https://img.shields.io/github/v/tag/dylanhogg/gptauthor)](https://github.com/dylanhogg/gptauthor/tags)
[![Downloads](https://static.pepy.tech/badge/gptauthor)](https://pepy.tech/project/gptauthor)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/gptauthor/blob/master/notebooks/gptauthor_colab_custom_story.ipynb)

Este repositório é um fork de [dylanhogg/gptauthor](https://github.com/dylanhogg/gptauthor), aprimorado para funcionar não somente com modelos OpenAI‑compatíveis (como DeepSeek e OpenRouter), mas também com Claude (Anthropic). Na prática, Claude frequentemente entrega escrita mais consistente e de maior qualidade.

DeepSeekAuthor é uma ferramenta de linha de comando para escrever histórias longas, multi‑capítulos, a partir de um prompt estruturado. Suporte multi‑provedor: OpenAI, DeepSeek, OpenRouter e Anthropic (Claude).

![Imagem de cabeçalho](https://github.com/dylanhogg/gptauthor/blob/main/docs/img/header.jpg?raw=true)

## Como Funciona

- Descrição humana da história: defina outline, estilo e personagens em um YAML ([exemplo](https://github.com/dylanhogg/gptauthor/blob/main/gptauthor/prompts-openai-drama.yaml)).
- Execução: escolha modelo, temperatura e quantidade de capítulos.
- Sinopse gerada por IA: o modelo transforma seu prompt em sinopse por capítulos.
- Revisão humana: você pode editar a sinopse antes de continuar.
- Escrita iterativa: cada capítulo usa a sinopse e o capítulo anterior. Saída em Markdown/HTML em `./_output/`.

## Exemplos de Saída

- [Crise de liderança da OpenAI (Nov/2023)](https://github.com/dylanhogg/gptauthor/blob/main/samples/openai-drama-20240131-224810-v0.5.0-gpt-4-0125-preview.md)
- [Echoes of Atlantis](https://github.com/dylanhogg/gptauthor/blob/main/samples/echoes-of-atlantis--v1.0.0-gpt-4-0125-preview.md)

## Instalação

Instale [gptauthor](https://pypi.org/project/gptauthor/) via pip, preferencialmente em um ambiente virtual.

```bash
pip install gptauthor
```

Notebook de exemplo no Google Colab:

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/gptauthor/blob/master/notebooks/gptauthor_colab_custom_story.ipynb)

## Executar

### Uso Rápido e API Key

Exemplo com OpenAI:

```bash
# Mac/Linux
export OPENAI_API_KEY="sk-<sua_chave>"
# Windows
setx OPENAI_API_KEY "sk-<sua_chave>"

gptauthor --story prompts-openai-drama --total-chapters 3 --llm-model gpt-3.5-turbo --llm-temperature 0.1
```

Observação: Claude (Anthropic) costuma produzir textos de melhor qualidade em escrita longa.

### Argumentos Obrigatórios

- `--story TEXT`: Nome do arquivo YAML com a história e prompts

### Argumentos Opcionais

- `--llm-provider TEXT`: openai | deepseek | openrouter | anthropic [default: openai]
- `--llm-model TEXT`: Nome do modelo [default: gpt-3.5-turbo]
- `--llm-temperature FLOAT`: Temperatura (0 a 2) [default: 1]
- `--llm-top-p FLOAT`: Top‑p (0 a 2) [default: 1]
- `--llm-use-localhost INTEGER`: Usa localhost:8081 [default: 0]
- `--llm-base-url TEXT`: Base URL para provedores compatíveis (ex.: https://api.deepseek.com)
- `--llm-api-key TEXT`: API key (override)
- `--llm-max-tokens INTEGER`: Máximo de tokens por resposta
- `--total-chapters INTEGER`: Total de capítulos [default: 3]
- `--allow-user-input / --no-allow-user-input`: Permite input [default: allow-user-input]
- `--version`: Versão
- `--help`: Ajuda

## Arquivos Gerados

- Progresso e saída final em `./_output/<prompt>/<modelo>/<data>-<parâmetros>-<título>/`
- Principais arquivos: `_whole_book.md` e `_whole_book.html`

## Criar Seus Próprios Prompts

```bash
export OPENAI_API_KEY="sk-<sua_chave>"
gptauthor --story prompts-minha-historia --total-chapters 5 --llm-model gpt-3.5-turbo --llm-temperature 0.1
```

## Suporte Multi‑Provedor

- OpenAI: `OPENAI_API_KEY`
- DeepSeek: `DEEPSEEK_API_KEY` e `LLM_BASE_URL=https://api.deepseek.com`
- OpenRouter: `OPENROUTER_API_KEY` e `LLM_BASE_URL=https://openrouter.ai/api/v1`
- Anthropic (Claude): `ANTHROPIC_API_KEY`

Exemplo (DeepSeek):

```bash
setx DEEPSEEK_API_KEY "<sua_chave_deepseek>"
setx LLM_BASE_URL "https://api.deepseek.com"
gptauthor --story prompts-openai-drama --llm-provider deepseek --total-chapters 3 --llm-model deepseek-chat --llm-temperature 0.1 --llm-base-url https://api.deepseek.com
```

Exemplo (Anthropic / Claude):

```bash
setx ANTHROPIC_API_KEY "<sua_chave_anthropic>"
gptauthor --story prompts-openai-drama --llm-provider anthropic --total-chapters 3 --llm-model claude-3-7-sonnet --llm-temperature 0.1 --llm-max-tokens 4096
```

Notas:
- Provedores compatíveis usam `--llm-base-url`. Anthropic não exige `base_url`.
- `--llm-use-localhost 1` permite servidor local compatível (ex.: vLLM).
- Claude tende a melhor qualidade em narrativas longas.

## Problemas Conhecidos

- Erros ocasionais da API; reinicie o app (cache por parâmetros).
- Continuidade pode variar devido à abordagem iterativa.
- Diferenças de caminho no Windows; reporte problemas.
- Estimativa de custo é aproximada; confirme no billing.
- Uso responsável de IA.

## Contribuição

- Fork, branch de feature/correção, commit e Pull Request com descrição.

## Licença

MIT: [LICENSE](https://github.com/dylanhogg/gptauthor/blob/main/LICENSE).
