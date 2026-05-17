# Task: Ordenação Manual (Drag-and-Drop) no Admin

## Descrição
Permitir que o usuário defina a ordem de exibição de projetos e stacks manualmente no Admin, sem depender da data de criação.

## Sub-tarefas
- [ ] Adicionar `django-adminsortable2` às dependências.
- [ ] Adicionar campo `order` (IntegerField/PositiveIntegerField) nos modelos `Project`, `Stack` e `GroupStack`.
- [ ] Configurar as classes Admin para herdar de `SortableAdminMixin` ou similar.
- [ ] Atualizar as queries na View para ordenar pelos novos campos.

## Critérios de Aceite
- Interface de arrastar e soltar funcionando no Admin.
- A ordem definida no Admin deve ser refletida exatamente no frontend.
