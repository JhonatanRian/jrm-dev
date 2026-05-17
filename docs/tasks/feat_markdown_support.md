# Task: Suporte a Markdown nas Descrições

## Descrição
Trocar os campos de texto simples por suporte a Markdown para permitir formatações ricas (negrito, listas, links) nas descrições de projetos e "Sobre Mim".

## Sub-tarefas
- [ ] Adicionar `django-markdownify` ou `markdown` às dependências.
- [ ] Criar ou ajustar o campo `description` no `Project` e `about` no `Portfolio` para suportar textos longos.
- [ ] Implementar template tags para renderizar o Markdown no HTML com segurança (escapando HTML malicioso).
- [ ] (Opcional) Adicionar um editor de Markdown (SimpleMDE ou similar) no Django Admin.

## Critérios de Aceite
- Descrições formatadas com Markdown aparecendo corretamente no site.
- Suporte a links e listas dentro da descrição dos projetos.
