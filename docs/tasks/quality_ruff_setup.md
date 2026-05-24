# Task: Configuração de Linter e Formatter (Ruff)

## Descrição
Padronizar o estilo de código e garantir a qualidade estática do projeto utilizando o Ruff, que é extremamente rápido e compatível com as ferramentas atuais do ecossistema Python (uv).

## Sub-tarefas
- [x] Adicionar `ruff` às dependências de desenvolvimento no `pyproject.toml`.
- [x] Criar arquivo de configuração `ruff.toml` ou adicionar seção no `pyproject.toml`.
- [x] Configurar regras de linting (ex: isort, flake8, pyupgrade).
- [x] Rodar o formatador em todo o projeto para alinhar o código atual.
- [x] Adicionar um script no `pyproject.toml` para facilitar a execução (ex: `uv run ruff check .`).

## Critérios de Aceite
- Código seguindo os padrões PEP 8 e as regras definidas.
- Nenhuma falha de linting detectada no projeto atual.
- Formatação consistente em todos os arquivos `.py`.
