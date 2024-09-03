from flask import Flask, render_template
import random

app = Flask(__name__)

starters = ["Soup", "Salad", "Bruschetta", "Wings", "Cheese Balls", "Carpaccio", "Garlic Bread", "Smash Potatoes", "Egg Rolls"]
main_dishes = ["Steak", "Pasta", "Pizza", "Burger", "Shawarma", "Lasagna", "Wraps", "Rice And Meat", "Falafel"]
desserts = ["Ice Cream", "Cake", "Fruit Salad", "Soufflé", "Donut", "Jello", "Macarons"]

@app.route('/')
def home():
    starter = random.choice(starters)
    main_dish = random.choice(main_dishes)
    dessert = random.choice(desserts)
    return render_template('index.html', starter=starter, main_dish=main_dish, dessert=dessert)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)