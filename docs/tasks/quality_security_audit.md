# Task: Auditoria de Segurança e Variáveis de Ambiente

## Descrição
Reforçar a segurança do projeto removendo segredos do código e garantindo que as configurações de produção sejam rigorosas.

## Sub-tarefas
- [ ] Remover a `SECRET_KEY` hardcoded do `settings.py` e garantir que o Django falhe se ela não estiver no `.env`.
- [ ] Implementar validação de tipos no `django-environ` para todas as variáveis críticas.
- [ ] Verificar as configurações de `SECURE_BROWSER_XSS_FILTER` e `SECURE_CONTENT_TYPE_NOSNIFF`.
- [ ] Criar um arquivo `.env.example` completo para novos desenvolvedores.
- [ ] Garantir que as chaves de criptografia (`FIELD_ENCRYPTION_KEY`) sejam geradas de forma segura e documentada.

## Critérios de Aceite
- Nenhuma informação sensível no sistema de controle de versão (Git).
- Configurações de produção validadas via `python manage.py check --deploy`.
