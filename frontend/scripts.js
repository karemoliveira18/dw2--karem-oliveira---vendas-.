const API = "http://127.0.0.1:8000"

const $products = document.getElementById('products')
const $search = document.getElementById('search')
const $categoria = document.getElementById('categoriaFilter')
const $sort = document.getElementById('sortSelect')
const $cartBtn = document.getElementById('cartBtn')
const $cartCount = document.getElementById('cartCount')
const $cartDrawer = document.getElementById('cartDrawer')
const $cartItems = document.getElementById('cartItems')
const $cupom = document.getElementById('cupom')
const $applyCoupon = document.getElementById('applyCoupon')
const $confirmOrder = document.getElementById('confirmOrder')

let cart = JSON.parse(localStorage.getItem('cart') || '[]')
let appliedCoupon = null
const $exportCsv = document.getElementById('exportCsv')
const $exportJson = document.getElementById('exportJson')
const $productModal = document.getElementById('productModal')
const $modalClose = document.getElementById('modalClose')
const $modalImage = document.getElementById('modalImage')
const $modalTitle = document.getElementById('modalTitle')
const $modalDescription = document.getElementById('modalDescription')
const $modalPrice = document.getElementById('modalPrice')
const $modalStock = document.getElementById('modalStock')
const $modalQty = document.getElementById('modalQty')
const $modalAdd = document.getElementById('modalAdd')

// persist sort in localStorage
const savedSort = localStorage.getItem('sortOrder')
if(savedSort) $sort.value = savedSort

function updateCartCount(){
  const total = cart.reduce((s,i)=>s+i.quantidade,0)
  $cartCount.textContent = total
}

function saveCart(){
  localStorage.setItem('cart', JSON.stringify(cart))
  updateCartCount()
}

async function fetchProdutos(){
  const params = new URLSearchParams()
  if($search.value) params.set('search',$search.value)
  if($categoria.value) params.set('categoria',$categoria.value)
  if($sort.value) params.set('sort',$sort.value)
  const res = await fetch(`${API}/produtos?${params.toString()}`)
  const data = await res.json()
  renderProdutos(data)
  populateCategorias(data)
}

function populateCategorias(produtos){
  const cats = new Set(produtos.map(p=>p.categoria).filter(Boolean))
  $categoria.innerHTML = '<option value="">Todas</option>'
  cats.forEach(c=>{
    const opt = document.createElement('option')
    opt.value = c
    opt.textContent = c
    $categoria.appendChild(opt)
  })
}

function renderProdutos(produtos){
  $products.innerHTML = ''
  produtos.forEach(p=>{
    const el = document.createElement('article')
    el.className = 'card'
    el.innerHTML = `
      <img src="${p.image_url || 'https://via.placeholder.com/400x300?text='+encodeURIComponent(p.nome)}" alt="Imagem de ${p.nome}" />
      <h3>${p.nome}</h3>
      <p>${p.descricao || ''}</p>
      <div class="meta">
        <div class="price">R$ ${formatPrice(p.preco)}</div>
        <div>
          <small>Estoque: ${p.estoque}</small>
        </div>
      </div>
      <div class="actions">
        <button ${p.estoque===0? 'disabled' : ''} data-id="${p.id}">Adicionar</button>
        <button class="btn-link" data-view="${p.id}">Detalhes</button>
      </div>
    `
    const btn = el.querySelector('button[data-id]')
    btn.addEventListener('click', ()=>{
      openModal(p)
    })
    const viewBtn = el.querySelector('button[data-view]')
    viewBtn.addEventListener('click', ()=> openModal(p))
    $products.appendChild(el)
  })
}

function openModal(p){
  $productModal.setAttribute('aria-hidden','false')
  $modalImage.src = p.image_url || ('https://via.placeholder.com/800x600?text='+encodeURIComponent(p.nome))
  $modalTitle.textContent = p.nome
  $modalDescription.textContent = p.descricao || ''
  $modalPrice.textContent = 'R$ ' + p.preco.toFixed(2)
  $modalStock.textContent = p.estoque
  $modalQty.value = 1
  $modalAdd.onclick = ()=>{
    const qtd = parseInt($modalQty.value,10) || 1
    addToCartWithQty(p.id,qtd)
    closeModal()
  }
}

function closeModal(){
  $productModal.setAttribute('aria-hidden','true')
}

 $modalClose.addEventListener('click', closeModal)
 $productModal.addEventListener('click', (e)=>{ if(e.target===$productModal) closeModal() })

function addToCartWithQty(produtoId, quantidade){
  const existing = cart.find(i=>i.produto_id===produtoId)
  if(existing){ existing.quantidade += quantidade }
  else { cart.push({produto_id: produtoId, quantidade}) }
  saveCart()
}

function addToCart(produtoId){
  const existing = cart.find(i=>i.produto_id===produtoId)
  if(existing){
    existing.quantidade += 1
  } else {
    cart.push({produto_id: produtoId, quantidade: 1})
  }
  saveCart()
}

function toggleCart(){
  const hidden = $cartDrawer.getAttribute('aria-hidden') === 'true'
  $cartDrawer.setAttribute('aria-hidden', String(!hidden))
  if(!hidden) renderCart()
}

function renderCart(){
  $cartItems.innerHTML = ''
  if(cart.length===0){
    $cartItems.textContent = 'Carrinho vazio'
    return
  }
  // fetch product names to present a friendlier cart
  fetch(`${API}/produtos`).then(r=>r.json()).then(produtos=>{
    cart.forEach(item=>{
      const prod = produtos.find(p=>p.id===item.produto_id)
      const div = document.createElement('div')
      div.className = 'cart-line'
      const name = prod? prod.nome : 'Produto '+item.produto_id
      const subtotal = prod? (prod.preco * item.quantidade) : 0
      div.innerHTML = `${name} <span style="float:right">${item.quantidade} × R$ ${formatPrice(subtotal)}</span>`
      $cartItems.appendChild(div)
    })
    updateCartTotal(produtos)
  })
}

function updateCartTotal(produtos){
  let total = 0
  cart.forEach(item=>{
    const prod = produtos.find(p=>p.id===item.produto_id)
    if(prod) total += prod.preco * item.quantidade
  })
  // aplicar cupom armazenado
  if(appliedCoupon && appliedCoupon.toUpperCase()==='ALUNO10'){
    total = total * 0.9
  }
  document.getElementById('cartTotal').textContent = formatPrice(total)
}

function formatPrice(v){
  return Number(v).toFixed(2).toString().replace('.',',')
}

$cartBtn.addEventListener('click', ()=>{
  toggleCart()
})

$search.addEventListener('input', ()=>fetchProdutos())
$categoria.addEventListener('change', ()=>fetchProdutos())
$sort.addEventListener('change', ()=>fetchProdutos())
// persist sort
$sort.addEventListener('change', ()=> localStorage.setItem('sortOrder', $sort.value))

$applyCoupon.addEventListener('click', ()=>{
  appliedCoupon = $cupom.value || null
  alert('Cupom aplicado: ' + appliedCoupon)
})

$confirmOrder.addEventListener('click', async ()=>{
  if(cart.length===0){ alert('Carrinho vazio'); return }
  const res = await fetch(`${API}/carrinho/confirmar`,{
    method:'POST',headers:{'Content-Type':'application/json'},
    body: JSON.stringify({itens:cart, cupom: appliedCoupon})
  })
  if(!res.ok){ const err = await res.json(); alert(err.detail || 'Erro'); return }
  const data = await res.json()
  alert('Pedido confirmado. Total: R$ ' + data.total_final.toFixed(2))
  cart = []
  saveCart()
  renderCart()
  fetchProdutos()
})

saveCart()
fetchProdutos()

$exportJson.addEventListener('click', async ()=>{
  const res = await fetch(`${API}/produtos`)
  const data = await res.json()
  const blob = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'})
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url; a.download = 'produtos.json'; a.click(); URL.revokeObjectURL(url)
})

$exportCsv.addEventListener('click', async ()=>{
  const res = await fetch(`${API}/produtos`)
  const data = await res.json()
  const header = ['id','nome','descricao','preco','estoque','categoria','sku']
  const rows = data.map(p=> header.map(h=> JSON.stringify(p[h] ?? '')).join(','))
  const csv = header.join(',') + '\n' + rows.join('\n')
  const blob = new Blob([csv], {type: 'text/csv'})
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url; a.download = 'produtos.csv'; a.click(); URL.revokeObjectURL(url)
})
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
