// Estado da aplicação
let produtos = [];
let carrinho = [];
let categoriasFiltradas = new Set();

// Função para renderizar um produto
function renderizarProduto(produto) {
    const estoqueStatus = produto.estoque > 20 ? 'disponivel' : produto.estoque > 5 ? 'baixo' : 'indisponivel';
    const estoqueTexto = produto.estoque > 0 ? `${produto.estoque} unidades em estoque` : 'Fora de estoque';
    
    return `
        <div class="produto-card">
            <div class="produto-imagem">
                <img src="https://via.placeholder.com/200" alt="${produto.nome}">
            </div>
            <div class="produto-info">
                <h3>${produto.nome}</h3>
                <p class="descricao">${produto.descricao}</p>
                <p class="preco">R$ ${produto.preco.toFixed(2)}</p>
                <p class="estoque ${estoqueStatus}">
                    <span class="material-icons">${produto.estoque > 0 ? 'check_circle' : 'error'}</span>
                    ${estoqueTexto}
                </p>
                <button class="btn-adicionar" 
                        onclick="adicionarAoCarrinho(${produto.id})"
                        ${produto.estoque === 0 ? 'disabled' : ''}>
                    ${produto.estoque > 0 ? 'Adicionar ao Carrinho' : 'Indisponível'}
                </button>
            </div>
        </div>
    `;
}

// Buscar produtos da API
fetch('http://localhost:5000/produtos')
    .then(res => res.json())
    .then(data => {
        produtos = data;
        const grid = document.getElementById('produtos-grid');
        
        // Renderizar produtos
        grid.innerHTML = produtos.map(renderizarProduto).join('');

        // Criar filtros de categoria
        const categorias = [...new Set(produtos.map(p => p.categoria))];
        const categoriasDiv = document.getElementById('categorias-filtro');
        categoriasDiv.innerHTML = categorias.map(categoria => `
            <div class="categoria-item">
                <input type="checkbox" id="${categoria}" value="${categoria}" 
                       onchange="filtrarPorCategoria('${categoria}')">
                <label for="${categoria}">${categoria}</label>
            </div>
        `).join('');
    });

// Funções de filtro
function filtrarPorCategoria(categoria) {
    const checkbox = document.getElementById(categoria);
    if (checkbox.checked) {
        categoriasFiltradas.add(categoria);
    } else {
        categoriasFiltradas.delete(categoria);
    }
    
    const grid = document.getElementById('produtos-grid');
    const produtosFiltrados = categoriasFiltradas.size === 0 
        ? produtos 
        : produtos.filter(p => categoriasFiltradas.has(p.categoria));
    
    grid.innerHTML = produtosFiltrados.map(renderizarProduto).join('');
}

// Funções do carrinho
function adicionarAoCarrinho(produtoId) {
    const produto = produtos.find(p => p.id === produtoId);
    if (produto && produto.estoque > 0) {
        carrinho.push(produto);
        atualizarCarrinho();
        
        // Feedback visual
        const btn = event.target;
        btn.textContent = '✓ Adicionado!';
        setTimeout(() => {
            btn.textContent = 'Adicionar ao Carrinho';
        }, 1000);
    }
}

function atualizarCarrinho() {
    const contagem = document.getElementById('cart-count');
    contagem.textContent = carrinho.length;

}

// Modal do carrinho
const cartButton = document.getElementById('cart-button');
const cartModal = document.getElementById('cart-modal');
const closeCart = document.getElementById('close-cart');

cartButton.onclick = () => {
    cartModal.style.display = 'block';
    atualizarModalCarrinho();
};

closeCart.onclick = () => {
    cartModal.style.display = 'none';
};

function atualizarModalCarrinho() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    
    if (carrinho.length === 0) {
        cartItems.innerHTML = '<p class="carrinho-vazio">Seu carrinho está vazio</p>';
        cartTotal.innerHTML = '';
        return;
    }
    
    let total = 0;
    cartItems.innerHTML = carrinho.map((item, index) => {
        total += item.preco;
        return `
            <div class="cart-item">
                <div class="cart-item-info">
                    <h4>${item.nome}</h4>
                    <p>R$ ${item.preco.toFixed(2)}</p>
                </div>
                <button class="btn-remover" onclick="removerDoCarrinho(${index})">
                    Remover
                </button>
            </div>
        `;
    }).join('');
    
    cartTotal.innerHTML = `
        <div class="cart-total">
            <h3>Total</h3>
            <h3>R$ ${total.toFixed(2)}</h3>
        </div>
        <button class="btn-finalizar">Finalizar Compra</button>
    `;
}

function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
    atualizarModalCarrinho();
}
