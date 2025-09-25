# 🧥 BaxaOptom — Premium Telegram Admin Panel

**BaxaOptom** — bu erkaklar kiyimi uchun mo‘ljallangan premium Telegram bot va Mini App. Bu admin panel orqali mahsulotlar, kategoriya, narxlar, brend sozlamalari va buyurtmalar to‘liq boshqariladi.

---

## 🚀 Imkoniyatlar

- Mahsulot qo‘shish (`admin-add.html`)
- Mahsulot ro‘yxatini ko‘rish (`admin-products.html`)
- Mahsulotni tahrirlash (`admin-edit.html`)
- Buyurtmalarni ko‘rish (`admin-orders.html`)
- Brend nomi, karta raqami, kategoriya sozlamalari (`admin-setting.html`)
- Statistika va grafiklar (`admin.html`)
- Premium dizayn va grid layout (`admin-style.css`)

---

## 📁 Papka tuzilmasi
baxaoptom_admin/ ├── admin.html              # Dashboard statistikasi ├── admin-add.html          # Mahsulot qo‘shish sahifasi ├── admin-edit.html         # Mahsulotni tahrirlash sahifasi ├── admin-orders.html       # Buyurtmalar ro‘yxati ├── admin-products.html     # Mahsulotlar grid ko‘rinishi ├── admin-setting.html      # Sozlamalar (brend, karta, til) ├── admin-login.html        # Kirish sahifasi ├── admin-style.css         # Barcha sahifalar uchun yagona dizayn ├── images/                 # Mahsulot rasmlari └── README.md               # Loyihani tushuntiruvchi hujjat

---

## 🛠 Texnologiyalar

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Ma’lumotlar**: `products.json`, `orders.json`, `settings.json`
- **Hosting**: Lokal yoki serverga deploy qilish mumkin

---

## 🔗 Backend endpointlar

- `GET /products` — mahsulotlar ro‘yxati
- `POST /products/add` — mahsulot qo‘shish
- `PUT /products/update/<id>` — mahsulotni tahrirlash
- `GET /products/stats` — statistik ma’lumotlar
- `GET /order-list` — buyurtmalar ro‘yxati
- `POST /order` — buyurtma qabul qilish
- `GET /settings` — sozlamalarni o‘qish
- `POST /settings/update` — sozlamalarni saqlash

---

## 📦 Ishga tushirish

1. `baxaoptom_backend/app.py` faylni ishga tushiring:
   ```bash
   python app.py