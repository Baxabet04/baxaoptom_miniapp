// 🛒 Savatcha obyekt
let cart = [];

// 📦 Mahsulotni savatchaga qo‘shish
function addToCart(productId, name, price, size) {
  cart.push({ id: productId, name, price, size, quantity: 1 });
  alert(`${name} savatchaga qo‘shildi`);
  updateCartIcon();
}

// 🔢 Savat belgisi yangilash
function updateCartIcon() {
  const cartLink = document.querySelector('.bottom-nav a[href="cart.html"]');
  if (cart.length > 0) {
    cartLink.innerHTML = `🛒 Savat (${cart.length})`;
  } else {
    cartLink.innerHTML = `🛒 Savat`;
  }
}

// 🧹 Savatchadan tanlanganlarni o‘chirish
function deleteSelectedItems() {
  const checkboxes = document.querySelectorAll('.cart-item input[type="checkbox"]');
  checkboxes.forEach((cb, index) => {
    if (cb.checked) {
      cart.splice(index, 1);
    }
  });
  alert("Tanlangan mahsulotlar o‘chirildi");
  renderCart();
}

// 📋 Savatchani sahifada ko‘rsatish
function renderCart() {
  const container = document.querySelector('.cart-list');
  container.innerHTML = '';
  let total = 0;

  cart.forEach(item => {
    const div = document.createElement('div');
    div.className = 'cart-item';
    div.innerHTML = `
      <input type="checkbox">
      <div class="cart-info">
        <h3>${item.name}</h3>
        <p>Razmer: ${item.size}</p>
        <p>Narx: ${item.price} UZS</p>
        <p>Soni: ${item.quantity} dona</p>
      </div>
    `;
    container.appendChild(div);
    total += item.price * item.quantity;
  });

  document.querySelector('.cart-summary').innerHTML = `
    <p>${cart.length} ta mahsulot: ${total} UZS</p>
    <p>Umumiy narx: ${total} UZS</p>
  `;
}

// 💳 To‘lovni tasdiqlash
function confirmPayment() {
  const selected = document.querySelector('input[name="payment"]:checked').value;
  if (selected === 'click') {
    alert("Click to‘lov tasdiqlandi. Adminga xabar yuboriladi.");
    sendTelegramMessage("Click orqali to‘lov tasdiqlandi.");
  } else {
    alert("Naqd to‘lov tanlandi. Adminga xabar yuboriladi.");
    sendTelegramMessage("Foydalanuvchi naqd to‘lovni tanladi.");
  }
}

// 📩 Telegramga xabar yuborish (keyinchalik backendga POST)
function sendTelegramMessage(message) {
  fetch('https://your-backend-url.com/send-message', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: message })
  });
}