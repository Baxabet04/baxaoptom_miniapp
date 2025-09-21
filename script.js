// Telegram WebApp API’ni ishga tushiramiz
window.Telegram.WebApp.ready();
window.Telegram.WebApp.expand();

// Har bir mahsulot tugmasiga event qo‘shamiz
document.querySelectorAll('.card button').forEach(btn => {
  btn.addEventListener('click', () => {
    alert("Mahsulot savatga qo‘shildi!");
  });
});