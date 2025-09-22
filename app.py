from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Mahsulotlar
@app.route('/products', methods=['GET'])
def get_products():
    with open('products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/products/add', methods=['POST'])
def add_product():
    new_product = request.json
    with open('products.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        new_product['id'] = len(data) + 1
        data.append(new_product)
        f.seek(0)
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "success"})

# Sozlamalar
@app.route('/settings', methods=['GET'])
def get_settings():
    with open('settings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/settings/update', methods=['POST'])
def update_settings():
    new_settings = request.json
    with open('settings.json', 'w', encoding='utf-8') as f:
        json.dump(new_settings, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "updated"})

if __name__ == '__main__':
    app.run(debug=True)