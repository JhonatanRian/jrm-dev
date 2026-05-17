# Task: Implementação de Testes (Unitários e Integração)

## Descrição
Garantir que as funcionalidades principais do portfólio e das contas de usuário funcionem conforme esperado e não quebrem com futuras alterações.

## Sub-tarefas
- [ ] Configurar o `pytest-django` como runner de testes.
- [ ] Criar testes para o modelo `Portfolio` (validação de único ativo).
- [ ] Criar testes para o modelo `Project` (geração automática de slug).
- [ ] Implementar testes de integração para a `PortfolioView` (verificar carregamento correto do contexto).
- [ ] Criar testes para o `CustomUserManager` no app `accounts`.
- [ ] Adicionar cobertura de testes no `pyproject.toml` usando `pytest-cov`.

## Critérios de Aceite
- Pelo menos 80% de cobertura nos apps `portfolio` e `accounts`.
- Todos os testes passando no ambiente local.
- Banco de dados de teste (SQLite em memória) configurado corretamente.
