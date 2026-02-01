# DeepSeekAuthor (Fork com Suporte Multi‑Provedor)

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

- Descrição humana da história: você define o outline, estilo e personagens em um arquivo YAML ([exemplo](https://github.com/dylanhogg/gptauthor/blob/main/gptauthor/prompts-openai-drama.yaml)).
- Execução: escolha o modelo, temperatura e quantidade de capítulos.
- Sinopse gerada por IA: o modelo transforma seu prompt em uma sinopse com resumos de capítulos.
- Revisão humana da sinopse: você pode editar a sinopse antes de continuar.
- Escrita iterativa dos capítulos: cada capítulo usa a sinopse (comum) e o capítulo anterior. A saída é gerada em Markdown e HTML em `./_output/`.

## Exemplos de Saída

- [Crise de liderança da OpenAI (Nov/2023)](https://github.com/dylanhogg/gptauthor/blob/main/samples/openai-drama-20240131-224810-v0.5.0-gpt-4-0125-preview.md)
- [Echoes of Atlantis](https://github.com/dylanhogg/gptauthor/blob/main/samples/echoes-of-atlantis--v1.0.0-gpt-4-0125-preview.md)

## Instalação

Instale [gptauthor](https://pypi.org/project/gptauthor/) com pip, preferencialmente em um ambiente virtual de Python.

```bash
pip install gptauthor
```

Ou execute o notebook de exemplo no Google Colab:

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

Observação: Claude (Anthropic) costuma produzir textos de melhor qualidade em escrita longa. Experimente provedores e modelos conforme seu caso.

### Argumentos Obrigatórios

- `--story TEXT`: Nome do arquivo YAML com a história e prompts

### Argumentos Opcionais

- `--llm-provider TEXT`: Provedor LLM: openai | deepseek | openrouter | anthropic [default: openai]
- `--llm-model TEXT`: Nome do modelo [default: gpt-3.5-turbo]
- `--llm-temperature FLOAT`: Temperatura (0 a 2) [default: 1]
- `--llm-top-p FLOAT`: Top‑p (0 a 2) [default: 1]
- `--llm-use-localhost INTEGER`: Usa localhost:8081 (OpenAI‑compatible) [default: 0]
- `--llm-base-url TEXT`: Base URL para provedores OpenAI‑compatíveis (ex.: https://api.deepseek.com)
- `--llm-api-key TEXT`: API key (override, caso não use variável de ambiente)
- `--llm-max-tokens INTEGER`: Máximo de tokens por resposta (varia por provedor)
- `--total-chapters INTEGER`: Total de capítulos [default: 3]
- `--allow-user-input / --no-allow-user-input`: Permite input no terminal [default: allow-user-input]
- `--version`: Exibe versão
- `--help`: Mostra ajuda

## Arquivos Gerados

- Progresso e saída final em `./_output/<prompt>/<modelo>/<data>-<parâmetros>-<título>/`
- Principais arquivos: `_whole_book.md` (Markdown) e `_whole_book.html` (HTML)

## Criar Seus Próprios Prompts

- Copie e edite o arquivo de exemplo [prompts-openai-drama.yaml](https://github.com/dylanhogg/gptauthor/blob/main/gptauthor/prompts-openai-drama.yaml)
- Execute no mesmo diretório do seu novo YAML:

```bash
export OPENAI_API_KEY="sk-<sua_chave>"
gptauthor --story prompts-minha-historia --total-chapters 5 --llm-model gpt-3.5-turbo --llm-temperature 0.1
```

## Suporte Multi‑Provedor

Suporte a provedores OpenAI‑compatíveis (OpenAI, DeepSeek, OpenRouter) via `base_url`, e a Anthropic (Claude).

- OpenAI: `OPENAI_API_KEY`
- DeepSeek: `DEEPSEEK_API_KEY` e `LLM_BASE_URL=https://api.deepseek.com`
- OpenRouter: `OPENROUTER_API_KEY` e `LLM_BASE_URL=https://openrouter.ai/api/v1`
- Anthropic (Claude): `ANTHROPIC_API_KEY`

Exemplo (DeepSeek):

```bash
# Windows
setx DEEPSEEK_API_KEY "<sua_chave_deepseek>"
setx LLM_BASE_URL "https://api.deepseek.com"
# Execução
gptauthor --story prompts-openai-drama --llm-provider deepseek --total-chapters 3 --llm-model deepseek-chat --llm-temperature 0.1 --llm-base-url https://api.deepseek.com
```

Exemplo (Anthropic / Claude):

```bash
# Windows
setx ANTHROPIC_API_KEY "<sua_chave_anthropic>"
# Mac/Linux
# export ANTHROPIC_API_KEY="<sua_chave_anthropic>"

gptauthor --story prompts-openai-drama --llm-provider anthropic --total-chapters 3 --llm-model claude-3-7-sonnet --llm-temperature 0.1 --llm-max-tokens 4096
```

Notas:
- Provedores OpenAI‑compatíveis usam `--llm-base-url`. Anthropic não exige `base_url`.
- `--llm-use-localhost 1` permite usar servidor local compatível (ex.: vLLM em `http://localhost:8081`).
- Claude costuma ter melhor qualidade de escrita em narrativas longas.

## Problemas Conhecidos

- Erros ocasionais da API: reinicie o app; respostas são cacheadas para os mesmos parâmetros.
- Continuidade entre capítulos pode variar pelo método iterativo (sinopse + capítulo anterior).
- Caminhos em Windows: podem haver diferenças; reportar problemas.
- Estimativa de custo por tokens é aproximada; confirme no painel de billing do provedor.
- Use IA de forma responsável.

## Contribuição

- Faça fork do repositório
- Crie um branch para sua feature/correção
- Comite suas mudanças
- Abra um Pull Request descrevendo suas alterações

## Licença

Projeto licenciado sob [MIT](https://github.com/dylanhogg/gptauthor/blob/main/LICENSE).
