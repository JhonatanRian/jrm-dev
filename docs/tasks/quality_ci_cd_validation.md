# Task: Melhoria do Pipeline CI/CD (GitLab)

## Descrição
Aprimorar o arquivo `.gitlab-ci.yml` para incluir etapas automáticas de validação de qualidade em cada commit ou Merge Request.

## Sub-tarefas
- [ ] Adicionar etapa de `lint` usando o Ruff.
- [ ] Adicionar etapa de `test` para rodar a suíte de testes do Pytest.
- [ ] Configurar o cache do `uv` no GitLab CI para acelerar as builds.
- [ ] Adicionar verificação de vulnerabilidades conhecidas em dependências (ex: `uv pip compile` + algum scanner).
- [ ] Garantir que a build do Docker seja testada no pipeline.

## Critérios de Aceite
- Pipeline falhando caso existam erros de lint ou testes quebrados.
- Relatórios de cobertura de testes visíveis no GitLab.
- Tempo de execução do pipeline otimizado.
