const grid = document.getElementById("produtosGrid");

async function carregarProdutos() {
  try {
    const resp = await fetch("http://127.0.0.1:8000/produtos");
    const produtos = await resp.json();
    grid.innerHTML = "";
    produtos.forEach(p => {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
        <h3>${p.nome}</h3>
        <p>${p.descricao || ""}</p>
        <p><strong>R$ ${p.preco.toFixed(2)}</strong></p>
        <p>Estoque: ${p.estoque}</p>
        <button onclick="adicionarCarrinho(${p.id})">Adicionar</button>
      `;
      grid.appendChild(card);
    });
  } catch (err) {
    console.error(err);
  }
}

function adicionarCarrinho(id) {
  alert("Produto " + id + " adicionado ao carrinho!");
}

carregarProdutos();
arProdutos();
