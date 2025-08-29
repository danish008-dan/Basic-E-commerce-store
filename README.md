# Basic-E-commerce-store
An E-commerce store that let you buy items, add items to stock and gives your bill of your order.

🛒 E-Commerce Store (Python Console App)
📌 Overview

This is a simple E-Commerce Store simulation built using Python dictionaries and functions.
It allows users to:

View available items in stock

Place an order and generate an order summary

Make payments and validate them

Add new items dynamically to the store

This project is useful for learning Python basics, functions, dictionaries, loops, and user input handling.

🚀 Features

✔ Show all available items with prices
✔ Place orders with quantity and get the total bill
✔ Payment system (validates exact amount)
✔ Add new products dynamically into the store
✔ Beginner-friendly Python project

📂 Project Structure
EcommerceStore/
│── ecommerce.py      # Main Python file (code of the store)
│── README.md         # Project Documentation

🔧 How It Works

Show_all() → Displays all items in stock with their prices.

order_now(product_name, quantity) → Places an order and calculates the bill.

payment_option(total_price) → Takes payment input and verifies if correct.

add_item() → Lets admin add new products into the store dynamically.

🖥️ Example Run
Available items:
bread: 30
milk: 22
lassi: 35
ice cream: 50
biscuits: 20
munchies: 50

Enter the product name to order: milk
Enter the product quantity: 2

order summary:
Item: milk
Quantity: 2
total price: 44

Enter the amount for payment: 44
payment successfully completed

Do you want to add new items to stock? (yes/no): no

📦 Installation & Usage

Clone the repository:

git clone https://github.com/<your-username>/ecommerce-store.git


Navigate to the project folder:

cd ecommerce-store


Run the program:

python ecommerce.py
