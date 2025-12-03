# Inventory Tracker

A Flask web application for tracking inventory items, quantities, costs, and stock levels.

## Features

- **Add Items** - Add new products with name, quantity, cost per item, and min/max stock limits
- **Edit Items** - Update existing item details anytime
- **Delete Items** - Remove items from inventory with confirmation
- **View Items** - See all items in a table with individual total values
- **Inventory Overview** - Check total inventory value, low stock items, and items exceeding max limits

## Requirements

- Python 3.x installed on your system

## Setup & Installation

### 1. Install Dependencies

Open a terminal/command prompt in the project folder and run:

```
pip install -r requirements.txt
```

### 2. Run the Application

Start the Flask app by running:

```
python app.py
```

### 3. Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

## How to Use

- **Main Page** (`/`) - View all inventory items and edit or delete existing items
- **Overview Page** (`/overview`) - See inventory summary, low stock alerts, and overstock items
- **Add Item Page** (`/add-item`) - Add a new item to the inventory
- **Edit Item** - Click "Edit" next to any item to modify its details
- **Delete Item** - Click "Delete" next to any item to remove it (confirmation required)

## Data Storage

All inventory data is stored in `items.json` file in the project directory.
