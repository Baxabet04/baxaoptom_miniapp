window.Telegram.WebApp.ready();
window.Telegram.WebApp.expand();

document.querySelectorAll('.product-card button').forEach(btn => {
  btn.addEventListener('click', () => {
    const id = btn.dataset.id;
    const name = btn.dataset.name;
    const price = parseInt(btn.dataset.price);
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push({ id, name, price, quantity: 1 });
    localStorage.setItem('cart', JSON.stringify(cart));
    alert(`${name} savatchaga qo‘shildi!`);
  });
});