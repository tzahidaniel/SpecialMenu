from flask import Flask, render_template
import random

app = Flask(__name__)


starters = ["Soup", "Salad", "Bruschetta", "Wings", "Cheese Balls", "Carpaccio", "Garlic Bread", "Smash Potatos", "Egg Rolls"]
main_dishes = ["Steak", "Pasta", "Pizza", "Burger", "Shawarma", "Lazanya", "Wrappers", "Rice And Meat", "Falafel"]
desserts = ["Ice Cream", "Cake", "Fruit Salad", "Souffle", "Donut", "Jello", "Macaroons"]
drinks = ["Coca Cola", "Orange Juice", "Coca Cola Zero", "Grape Juice", "Fresh Lemon Juice", "Apple Juice", "Lemon Sprite", "Watermelon Lemonade", "Iced tea", "Strawberry lemonade"]

@app.route('/')
def home():
    starter = random.choice(starters)
    main_dish = random.choice(main_dishes)
    dessert = random.choice(desserts)
    drinks = random.choice(drinks)
    return render_template('index.html', starter=starter, main_dish=main_dish, dessert=dessert, drinks=drinks)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

