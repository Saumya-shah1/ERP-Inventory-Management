from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Supplier, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    total_value = sum([p.quantity * p.price for p in products])
    return render_template('index.html', products=products, total_value=total_value)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        new_product = Product(name=name, category=category, price=price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        quantity = int(request.form['quantity'])
        product = Product.query.get(product_id)
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            new_order = Order(product_id=product_id, quantity=quantity)
            db.session.add(new_order)
            db.session.commit()
        return redirect(url_for('index'))
    products = Product.query.all()
    return render_template('add_order.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
