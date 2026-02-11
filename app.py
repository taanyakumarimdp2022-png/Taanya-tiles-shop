# app.py
from flask import Flask,request
render_template_string, 

app = Flask(__name__)

# Sample product data
products = {
    1: {"name": "Tiles", "price": 450, "stock": 100},
    2: {"name": "Marble", "price": 800, "stock": 50}
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Taanya Tiles & Marble</title>
</head>
<body>
    <h1>Taanya Tiles & Marble</h1>

    <h2>Available Products:</h2>
    <ul>
        {% for id, product in products.items() %}
            <li>
                ID: {{ id }} |
                {{ product.name }} |
                Price: ₹{{ product.price }} |
                Stock: {{ product.stock }}
            </li>
        {% endfor %}
    </ul>

    <h2>Generate Bill</h2>
    <form method="POST">
        Product ID: <input type="number" name="product_id" required><br><br>
        Quantity: <input type="number" name="quantity" required><br><br>
        Customer Name: <input type="text" name="customer" required><br><br>
        <button type="submit">Generate Bill</button>
    </form>

    {% if bill %}
        <h3>Bill for {{ bill.customer }}</h3>
        <p>Product: {{ bill.product }}</p>
        <p>Quantity: {{ bill.quantity }}</p>
        <p>Total Amount: ₹{{ bill.total }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    bill = None
    if request.method == "POST":
        product_id = int(request.form["product_id"])
        quantity = int(request.form["quantity"])
        customer = request.form["customer"]

        if product_id in products and products[product_id]["stock"] >= quantity:
            product = products[product_id]
            total = product["price"] * quantity
            products[product_id]["stock"] -= quantity

            bill = {
                "customer": customer,
                "product": product["name"],
                "quantity": quantity,
                "total": total
            }
        else:
            bill = {
                "customer": customer,
                "product": "Not Available",
                "quantity": quantity,
                "total": 0
            }

    return render_template_string(html, products=products, bill=bill)

if __name__ == "__main__":
    app.run(debug=True)
Added Flask shop app
