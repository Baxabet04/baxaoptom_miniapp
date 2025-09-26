from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# 📂 Fayl yo‘llari
SETTINGS_FILE = 'settings.json'
PRODUCTS_FILE = 'products.json'
ORDERS_FILE = 'orders.json'

# -------------------- 🔧 Sozlamalar --------------------

@app.route('/settings', methods=['GET'])
def get_settings():
    if not os.path.exists(SETTINGS_FILE):
        return jsonify({})
    with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    return jsonify(settings)

@app.route('/settings/update', methods=['POST'])
def update_settings():
    data = request.get_json()
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "updated"})

# -------------------- 📦 Mahsulotlar --------------------

@app.route('/products', methods=['GET'])
def get_products():
    if not os.path.exists(PRODUCTS_FILE):
        return jsonify([])
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
    return jsonify(products)

@app.route('/products/add', methods=['POST'])
def add_product():
    new_product = request.get_json()
    if not os.path.exists(PRODUCTS_FILE):
        products = []
    else:
        with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
            products = json.load(f)
    products.append(new_product)
    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "added"})

@app.route('/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated = request.get_json()
    with open(PRODUCTS_FILE, 'r+', encoding='utf-8') as f:
        products = json.load(f)
        for i, p in enumerate(products):
            if p['id'] == product_id:
                products[i].update(updated)
                break
        f.seek(0)
        json.dump(products, f, ensure_ascii=False, indent=2)
        f.truncate()
    return jsonify({"status": "updated"})

@app.route('/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    with open(PRODUCTS_FILE, 'r+', encoding='utf-8') as f:
        products = json.load(f)
        products = [p for p in products if p['id'] != product_id]
        f.seek(0)
        json.dump(products, f, ensure_ascii=False, indent=2)
        f.truncate()
    return jsonify({"status": "deleted"})

@app.route('/products/stats', methods=['GET'])
def product_stats():
    if not os.path.exists(PRODUCTS_FILE):
        return jsonify({"total": 0, "categories": {}, "last": None})
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        products = json.load(f)
    total = len(products)
    categories = {}
    for p in products:
        cat = p.get('type', 'no-category')
        categories[cat] = categories.get(cat, 0) + 1
    last = products[-1] if products else None
    return jsonify({
        "total": total,
        "categories": categories,
        "last": last
    })

# -------------------- 🛒 Buyurtmalar --------------------

@app.route('/order', methods=['POST'])
def receive_order():
    order = request.get_json()
    order['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    if not os.path.exists(ORDERS_FILE):
        orders = []
    else:
        with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
            orders = json.load(f)
    orders.append(order)
    with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "received"})

@app.route('/order-list', methods=['GET'])
def list_orders():
    if not os.path.exists(ORDERS_FILE):
        return jsonify([])
    with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
        orders = json.load(f)
    return jsonify(orders)

# -------------------- 🚀 Serverni ishga tushirish --------------------

if __name__ == '__main__':
    app.run(debug=True)