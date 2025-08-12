// Configuração inicial do sistema
const DESCONTO_CUPOM = 0.1; // 10% de desconto
const CUPONS_VALIDOS = ['ESCOLA10', 'MATERIAL20', 'UNIFORME15'];
const ESTOQUE_MINIMO = 5;

// Estado da aplicação
let produtos = [];
let carrinho = [];
let totalVendas = 0;

// Classes principais
class Produto {
    constructor(nome, preco, estoque, categoria) {
        this.id = Date.now();
        this.nome = nome;
        this.preco = preco;
        this.estoque = estoque;
        this.categoria = categoria;
        this.vendidos = 0;
    }

    atualizarEstoque(quantidade) {
        if (this.estoque + quantidade >= 0) {
            this.estoque += quantidade;
            return true;
        }
        return false;
    }

    verificarEstoqueBaixo() {
        return this.estoque <= ESTOQUE_MINIMO;
    }
}

class GerenciadorProdutos {
    static adicionarProduto(event) {
        event.preventDefault();
        
        const produto = new Produto(
            document.getElementById('nome').value,
            parseFloat(document.getElementById('preco').value),
            parseInt(document.getElementById('estoque').value),
            document.getElementById('categoria').value
        );

        produtos.push(produto);
        this.salvarProdutos();
        Interface.atualizarGrid();
        Interface.fecharModalProduto();
        
        if (produto.verificarEstoqueBaixo()) {
            Interface.mostrarAlerta(`Atenção: Produto ${produto.nome} cadastrado com estoque baixo!`);
        }
    }

    static buscarProdutos(termo) {
        if (!termo) return produtos;
        
        const termoBusca = termo.toLowerCase();
        return produtos.filter(produto => 
            produto.nome.toLowerCase().includes(termoBusca) ||
            produto.categoria.toLowerCase().includes(termoBusca)
        );
    }

    static salvarProdutos() {
        localStorage.setItem('produtos', JSON.stringify(produtos));
    }

    static carregarProdutos() {
        const produtosSalvos = localStorage.getItem('produtos');
        if (produtosSalvos) {
            produtos = JSON.parse(produtosSalvos);
        }
    }
}

class GerenciadorCarrinho {
    static adicionarItem(produtoId) {
        const produto = produtos.find(p => p.id === produtoId);
        
        if (produto && produto.estoque > 0) {
            produto.atualizarEstoque(-1);
            
            const itemCarrinho = carrinho.find(item => item.id === produtoId);
            if (itemCarrinho) {
                itemCarrinho.quantidade++;
            } else {
                carrinho.push({
                    id: produto.id,
                    nome: produto.nome,
                    preco: produto.preco,
                    quantidade: 1
                });
            }

            GerenciadorProdutos.salvarProdutos();
            Interface.atualizarGrid();
            Interface.atualizarContadorCarrinho();
            this.salvarCarrinho();
        }
    }

    static removerItem(produtoId) {
        const index = carrinho.findIndex(item => item.id === produtoId);
        if (index > -1) {
            const item = carrinho[index];
            const produto = produtos.find(p => p.id === produtoId);
            
            if (item.quantidade > 1) {
                item.quantidade--;
            } else {
                carrinho.splice(index, 1);
            }

            if (produto) {
                produto.atualizarEstoque(1);
            }

            GerenciadorProdutos.salvarProdutos();
            this.salvarCarrinho();
            Interface.atualizarGrid();
            Interface.atualizarCarrinho();
            Interface.atualizarContadorCarrinho();
        }
    }

    static aplicarDesconto(cupom) {
        if (CUPONS_VALIDOS.includes(cupom)) {
            return this.calcularTotal() * (1 - DESCONTO_CUPOM);
        }
        return this.calcularTotal();
    }

    static calcularTotal() {
        return carrinho.reduce((total, item) => 
            total + (item.preco * item.quantidade), 0
        );
    }

    static finalizarCompra() {
        if (carrinho.length === 0) {
            Interface.mostrarAlerta('Adicione itens ao carrinho primeiro!');
            return;
        }

        const cupom = document.getElementById('coupon').value;
        const totalCompra = this.aplicarDesconto(cupom);

        carrinho.forEach(item => {
            const produto = produtos.find(p => p.id === item.id);
            if (produto) {
                produto.vendidos += item.quantidade;
            }
        });

        totalVendas += totalCompra;
        
        Interface.mostrarAlerta(`Compra finalizada! Total: R$ ${totalCompra.toFixed(2)}`);
        carrinho = [];
        this.salvarCarrinho();
        GerenciadorProdutos.salvarProdutos();
        Interface.atualizarCarrinho();
        Interface.atualizarContadorCarrinho();
        Interface.fecharModalCarrinho();
    }

    static salvarCarrinho() {
        localStorage.setItem('carrinho', JSON.stringify(carrinho));
        localStorage.setItem('totalVendas', totalVendas);
    }

    static carregarCarrinho() {
        const carrinhoSalvo = localStorage.getItem('carrinho');
        const totalSalvo = localStorage.getItem('totalVendas');
        
        if (carrinhoSalvo) {
            carrinho = JSON.parse(carrinhoSalvo);
        }
        if (totalSalvo) {
            totalVendas = parseFloat(totalSalvo);
        }
    }
}

// Classe para manipulação da interface
class Interface {
    static atualizarGrid() {
        const grid = document.getElementById('product-grid');
        const termoBusca = document.getElementById('search').value;
        const produtosFiltrados = GerenciadorProdutos.buscarProdutos(termoBusca);
        
        grid.innerHTML = '';

        produtosFiltrados.forEach(produto => {
            const card = document.createElement('div');
            card.className = 'product-card';
            if (produto.verificarEstoqueBaixo()) {
                card.classList.add('estoque-baixo');
            }
            
            card.innerHTML = `
                <h3>${produto.nome}</h3>
                <p>R$ ${produto.preco.toFixed(2)}</p>
                <p>Estoque: ${produto.estoque}</p>
                <p>Categoria: ${produto.categoria}</p>
                <p>Vendidos: ${produto.vendidos}</p>
                <button onclick="GerenciadorCarrinho.adicionarItem(${produto.id})" 
                        ${produto.estoque <= 0 ? 'disabled' : ''}>
                    ${produto.estoque <= 0 ? 'Sem Estoque' : 'Adicionar ao Carrinho'}
                </button>
            `;
            grid.appendChild(card);
        });
    }

    static atualizarCarrinho() {
        const listaCarrinho = document.getElementById('cart-items');
        const totalElement = document.getElementById('cart-total');
        
        listaCarrinho.innerHTML = '';

        carrinho.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${item.nome} - ${item.quantidade}x R$ ${item.preco.toFixed(2)}
                <button onclick="GerenciadorCarrinho.removerItem(${item.id})">❌</button>
            `;
            listaCarrinho.appendChild(li);
        });

        const total = GerenciadorCarrinho.calcularTotal();
        totalElement.textContent = `Total: R$ ${total.toFixed(2)}`;
    }

    static atualizarContadorCarrinho() {
        const total = carrinho.reduce((sum, item) => sum + item.quantidade, 0);
        document.getElementById('cart-count').textContent = total;
    }

    static mostrarAlerta(mensagem) {
        alert(mensagem); // Em uma versão mais elaborada, poderia ser um modal personalizado
    }

    static abrirModalProduto() {
        document.getElementById('product-modal').classList.remove('hidden');
    }

    static fecharModalProduto() {
        document.getElementById('product-modal').classList.add('hidden');
        document.getElementById('product-form').reset();
    }

    static abrirModalCarrinho() {
        this.atualizarCarrinho();
        document.getElementById('cart-modal').classList.remove('hidden');
    }

    static fecharModalCarrinho() {
        document.getElementById('cart-modal').classList.add('hidden');
    }
}

// Inicialização e Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Carregar dados salvos
    GerenciadorProdutos.carregarProdutos();
    GerenciadorCarrinho.carregarCarrinho();
    
    // Inicializar interface
    Interface.atualizarGrid();
    Interface.atualizarContadorCarrinho();

    // Event listeners
    document.getElementById('product-form').addEventListener('submit', GerenciadorProdutos.adicionarProduto);
    document.getElementById('cart-btn').addEventListener('click', () => Interface.abrirModalCarrinho());
    document.getElementById('search').addEventListener('input', () => Interface.atualizarGrid());
    document.getElementById('checkout-btn').addEventListener('click', () => GerenciadorCarrinho.finalizarCompra());
});
