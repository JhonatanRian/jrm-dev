# Task: Configuração de Linter e Formatter (Ruff)

## Descrição
Padronizar o estilo de código e garantir a qualidade estática do projeto utilizando o Ruff, que é extremamente rápido e compatível com as ferramentas atuais do ecossistema Python (uv).

## Sub-tarefas
- [ ] Adicionar `ruff` às dependências de desenvolvimento no `pyproject.toml`.
- [ ] Criar arquivo de configuração `ruff.toml` ou adicionar seção no `pyproject.toml`.
- [ ] Configurar regras de linting (ex: isort, flake8, pyupgrade).
- [ ] Rodar o formatador em todo o projeto para alinhar o código atual.
- [ ] Adicionar um script no `pyproject.toml` para facilitar a execução (ex: `uv run ruff check .`).

## Critérios de Aceite
- Código seguindo os padrões PEP 8 e as regras definidas.
- Nenhuma falha de linting detectada no projeto atual.
- Formatação consistente em todos os arquivos `.py`.
