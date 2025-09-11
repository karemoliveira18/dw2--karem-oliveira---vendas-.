# REPORT

Relatório técnico do projeto "Loja Escolar" — mini-sistema de vendas (tema Vendas de Produtos).

## Arquitetura

- Backend: FastAPI + SQLAlchemy + SQLite (`backend/app.py`, `backend/models.py`, `backend/database.py`).
- Frontend: HTML/CSS/Vanilla JS (`frontend/index.html`, `frontend/styles.css`, `frontend/scripts.js`).
- Banco: `instance/app.db` (SQLite, criado pelo `init_db()` no backend).

Fluxo de requisição:
1. Frontend faz `fetch()` para `/produtos`.
2. FastAPI processa a requisição, usa SQLAlchemy para consultar `instance/app.db`.
3. Resultado em JSON é retornado e renderizado no frontend.

## Tecnologias e versões (sugestão)

- Python 3.10+
- FastAPI (0.95+)
- SQLAlchemy (2.x)
- Uvicorn
- Frontend: Vanilla JS, CSS3 (Grid/Flex)

## Prompts do Copilot (exemplos usados no desenvolvimento)

1. "Gerar um CRUD em FastAPI para entidade Produto com SQLAlchemy e SQLite" — gerei base e ajustei validações.
2. "Criar seed.py que insere 20 produtos plausíveis com imagens" — aceitei e modifiquei URLs e descrições.
3. "Criar frontend HTML/CSS com grid responsivo de cards" — base aceita, ajustei estilo e acessibilidade.
4. "Implementar carrinho em localStorage e endpoint /carrinho/confirmar" — adaptei regras de estoque e cupom.
5. "Adicionar export CSV/JSON no frontend" — implementei botões e lógica de download.
6. "Adicionar modal de detalhe do produto com acessibilidade" — implementei modal com foco e atalhos.

Para cada prompt, descreva no relatório final quais trechos foram mantidos, adaptados e por qual motivo.

## Peculiaridades implementadas (3+)

1. Seed com 20 produtos plausíveis (peculiaridade 7).
2. Acessibilidade básica: `aria-label`, `aria-hidden`, foco visível e navegação por teclado (peculiaridade 1).
3. Export CSV/JSON da lista atual (peculiaridade 6).
4. Ordenação persistida em `localStorage` (peculiaridade 4).

## Validações

- Front: validação de campos, impedir adicionar ao carrinho quando estoque=0 (botão desabilitado), validação de quantidade mínima no modal.
- Back: Pydantic valida `preco > 0`, `estoque >= 0`, validações no endpoint `carrinho/confirmar` para checar estoque e retornar 400 em caso de erro.

## Acessibilidade

- Elementos com `aria-label` e `aria-hidden` no modal e no carrinho.
- Foco visível via CSS e navegação por teclado (inputs e botões acessíveis).

## Como rodar (passo a passo Windows PowerShell)

1. Criar e ativar venv

```powershell
cd C:\Users\costa_ana02\Documents\GitHub\dw2--karem-oliveira---vendas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
```

2. Rodar seed (popula `instance/app.db`)

```powershell
python -c "from backend.seed import seed; seed()"
```

3. Iniciar servidor

```powershell
uvicorn backend.app:app --reload
```

4. Servir frontend (opcional)

```powershell
cd frontend
python -m http.server 8001
# abrir http://127.0.0.1:8001
```

## Checklist para entrega

- [ ] Seed com 20 produtos
- [ ] Endpoints REST (GET/POST/PUT/DELETE) funcionando
- [ ] Endpoint de confirmar carrinho com cupom e atualização de estoque
- [ ] Frontend com fotos, modal, carrinho e exportação
- [ ] `ChatIA.md` com os prompts usados
- [ ] `REPORT.md` preenchido e screenshots


## Arquitetura
- Frontend: HTML, CSS, JS
- Backend: Flask, SQLAlchemy, SQLite

## Tecnologias
- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- Poppins (Google Fonts)

## Prompts do Copilot
- Exemplos de prompts usados para gerar código e estrutura.

## Peculiaridades
- Validações básicas no backend
- Seed de dados

## Como rodar
- Siga o README.md

## Limitações
- Não há autenticação
- Falta testes automatizados
