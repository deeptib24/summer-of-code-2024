# app/product/views.py

from flask import Blueprint, request, jsonify
from app.models import Product, db

# Define the Blueprint
product_bp = Blueprint('product_bp', __name__)

# Create a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        sku=data.get('sku'),
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        quantity=data.get('quantity')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully!'}), 201

# Retrieve a list of all products
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'sku': product.sku,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity
        }
        product_list.append(product_data)
    return jsonify(product_list), 200

# Retrieve a specific product by ID
@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    product_data = {
        'id': product.id,
        'sku': product.sku,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    }
    return jsonify(product_data), 200

# Update an existing product
@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.sku = data.get('sku')
    product.name = data.get('name')
    product.description = data.get('description')
    product.price = data.get('price')
    product.quantity = data.get('quantity')
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'}), 200

# Delete a product from the database
@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'}), 200
