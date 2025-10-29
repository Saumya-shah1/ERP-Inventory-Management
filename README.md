 ERP Inventory Management System

A lightweight Inventory Management Web Application built with Python (Flask) and SQLite.
It helps users efficiently manage products, stock levels, and orders through an interactive dashboard.

Features:

Add and manage product details (name, category, price, quantity)

 Create customer orders and automatically update stock levels

 View total inventory value in real time

 Persistent data storage using SQLite

Clean and responsive web interface using HTML and CSS

| Component | Technology                             |
| --------- | -------------------------------------- |
| Backend   | Python, Flask                          |
| Database  | SQLite (SQLAlchemy ORM)                |
| Frontend  | HTML, CSS                              |
| Libraries | Flask-SQLAlchemy                       |
| Tools     | VS Code, GitHub, DB Browser for SQLite |


ERP-Inventory-Management/
│
├── app.py                 # Main Flask application
├── models.py              # Database models (Product, Supplier, Order)
├── database.db            # SQLite database (auto-created)
│
├── templates/             # HTML templates for UI
│   ├── base.html
│   ├── index.html
│   ├── add_product.html
│   └── add_order.html
│
├── static/                # CSS and JS files
│   └── style.css
│
└── README.md              # Project documentation


