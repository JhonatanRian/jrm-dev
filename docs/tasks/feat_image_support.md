# Task: Suporte a Imagens nos Projetos e Perfil

## Descrição
Implementar campos de imagem nos modelos para permitir uma exibição visual dos projetos e do profissional no portfólio.

## Sub-tarefas
- [ ] Configurar `Pillow` nas dependências (`pyproject.toml`).
- [ ] Adicionar campo `image` no modelo `Project` em `portfolio/models/project.py`.
- [ ] Adicionar campo `profile_image` no modelo `Portfolio` em `portfolio/models/portfolio.py`.
- [ ] Configurar diretórios de upload organizados (ex: `projects/%Y/%m/`).
- [ ] Atualizar o Django Admin para exibir thumbnails das imagens.
- [ ] Ajustar os templates HTML para renderizar as imagens com placeholders caso estejam vazias.

## Critérios de Aceite
- Upload de imagens funcionando via Admin.
- Redimensionamento básico ou validação de tamanho para evitar imagens pesadas.
- Exibição correta no frontend do portfólio.
