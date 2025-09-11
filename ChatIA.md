# ChatIA

Este arquivo registra as conversas com a IA (Copilot/ChatGPT) usadas durante o
desenvolvimento do projeto. Inclua aqui todas as interações relevantes —
perguntas, prompts e respostas aceitas/ajustadas. Esta documentação é parte da
avaliação e deve conter apenas conteúdo autoral.

Exemplo de entrada:

- 2025-09-11: Solicitei à IA para gerar um backend em FastAPI com endpoints de
  produtos e carrinho. Aceitei a maior parte do código, ajustei validações e
  adicionei o seed manualmente.

Prompts usados (exemplos):

1. "Crie um backend em FastAPI com SQLAlchemy para gerenciar produtos (CRUD) e um endpoint para confirmar carrinho aplicando cupom ALUNO10" — resultado: criei `backend/app.py` e ajustei validações.
2. "Gerar seed.py com 20 produtos com nomes, descrição, preço, estoque e imagem" — aceitei e refinei as descrições e URLs.
3. "Criar frontend responsivo em HTML/CSS/JS para listar produtos em grid e gerenciar carrinho em localStorage" — adaptei o layout e adicionei acessibilidade.
4. "Adicionar modal de detalhe do produto e funcionalidade de export CSV/JSON" — implementei modal e botões de export.
5. "Criar tests.http para chamadas principais da API" — adicionei arquivo `tests.http`.
6. "Sugerir .gitignore e organização com pasta instance para o banco" — adotei `instance/app.db`.

Para cada prompt adicione aqui o trecho de código gerado e explique o que foi aceito e o que foi alterado.

-- FIM --
