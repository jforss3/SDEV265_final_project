from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "items.json"

# Load and save items
def load_items():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_items(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=4)

# Inventory List Page
@app.route("/")
def items_page():
    items = load_items()
    return render_template("items.html", items=items)

# Add Item Page
@app.route("/add-item", methods=["GET", "POST"])
def add_item():
    items = load_items()
    if request.method == "POST":
        new_item = {
            "id": max([i["id"] for i in items], default=0) + 1,
            "name": request.form["name"],
            "production_price": float(request.form["production_price"]),
            "sell_price": float(request.form["sell_price"]),
            "current_stock": int(request.form["current_stock"]),
            "min_stock": int(request.form["min_stock"]),
            "max_stock": int(request.form["max_stock"])
        }
        items.append(new_item)
        save_items(items)
        return redirect("/")
    return render_template("add_item.html")

# Edit Item Page (each item)
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    items = load_items()
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return redirect("/")  # Item not found

    if request.method == "POST":
        item["name"] = request.form["name"]
        item["production_price"] = float(request.form["production_price"])
        item["sell_price"] = float(request.form["sell_price"])
        item["current_stock"] = int(request.form["current_stock"])
        item["min_stock"] = int(request.form["min_stock"])
        item["max_stock"] = int(request.form["max_stock"])
        save_items(items)
        return redirect("/")  # back to inventory list

    return render_template("edit_item.html", item=item)

# Change Stock
def change_stock(item_id: int, change_amount: int):
    """Meant to be used by other systems (such as an online ordering system) to change the current stock."""
    items = load_items()
    item = next((i for i in items if i["id"] == item_id), None)
    
    if not item:
        raise ValueError("item_id not found")
    
    item["current_stock"] += change_amount
    save_items(items)

# Delete Item
@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    items = load_items()
    items = [i for i in items if i["id"] != item_id]
    save_items(items)
    return redirect("/")

# Overview Page
@app.route("/overview")
def overview():
    items = load_items()
    total_cost_value = sum(i["current_stock"] * i["production_price"] for i in items)
    total_sell_value = sum(i["current_stock"] * i["sell_price"] for i in items)

    low_stock = [i for i in items if i["current_stock"] < i["min_stock"]]
    high_stock = [i for i in items if i["current_stock"] > i["max_stock"]]

    return render_template("overview.html",
                           total_cost_value=total_cost_value,
                           total_sell_value=total_sell_value,
                           low_stock=low_stock,
                           high_stock=high_stock)

if __name__ == "__main__":
    app.run(debug=True)
