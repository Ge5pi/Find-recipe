from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

client = OpenAI()

app = Flask(__name__)


class Product:
    def __init__(self, name, quantity, main_name):
        self.name = name
        self.quantity = quantity
        self.main_name = main_name



rand = "Pepperoni"

completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": "you are a chef. Your main task is to provide recipes for your clients with "
                                      "given name of the dish. Produce only a list of products, divided by a comma. "
                                      "and after the keyword 'instructions: ' generate the whole instructions."
                                      "Specify the quantity for each product, using colon. Do not say the word Products at all"},
        {"role": "user", "content": rand}
    ]
)

response = completion.choices[0].message.content

ins_index = response.find("instructions")

ing_index = response[:ins_index]
ing_list = ing_index.split(', ')

print("instructions: ", response[ins_index::])

ing_class_list = []

for el in ing_list:
    el = el.split(":")
    temp_prod = Product(el[0], el[1], rand)
    ing_class_list.append(temp_prod)
    print(el)
print(ing_class_list[0].name, ing_class_list[0].quantity, rand, response[ins_index::])

for el in ing_class_list:
    print(el.name)
    print(el.quantity)

insts = response[ins_index::].split(".")


@app.route("/recipe/<dish_name>")
def index(dish_name):


    rand = dish_name

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": "you are a chef. Your main task is to provide recipes for your clients with "
                                          "given name of the dish. Produce only a list of products, divided by a comma. "
                                          "and after the keyword 'instructions: ' generate the whole instructions."
                                          "Specify the quantity for each product, using colon. Do not say the word Products at all"},
            {"role": "user", "content": rand}
        ]
    )

    response = completion.choices[0].message.content

    ins_index = response.find("instructions")+14

    ing_index = response[:ins_index]
    ing_list = ing_index.split(', ')

    print("instructions: ", response[ins_index::])

    ing_class_list = []

    for el in ing_list:
        el = el.split(":")
        temp_prod = Product(el[0], el[1], rand)
        ing_class_list.append(temp_prod)
        print(el)
    print(ing_class_list[0].name, ing_class_list[0].quantity, rand, response[ins_index::])

    for el in ing_class_list:
        print(el.name)
        print(el.quantity)

    insts = response[ins_index::].split(".")



    return render_template('card.html', ingredients=ing_class_list, insts=insts, header=rand)





'''completion_type = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "system", "content": "you need to define the type of the given project. e.g Бородинский хлеб - хлеб, "
                                     "йогурт - молоко, пепперони - колбасы. Напиши только ответ одним словом или "
                                     "словосочетанием."
    }, {"role": "user", "content": "Пепперони"}]
)

driver = webdriver.Chrome()
driver.get('https://eda.yandex.kz/ru-kz/retail/small_1704798902?placeSlug=small_ktfnb')


def get_price(product_type):
    product_type_h = driver.find_element(By.CLASS_NAME, "UiKitRetailDesktopCategoryHeader_title UiKitText_root "
                                                        "UiKitText_Title4 UiKitText_Bold UiKitText_Text")
    print(product_type_h)
    if product_type_h == product_type:
        pass


get_price(completion_type.choices[0].message.content)'''


@app.route("/generate", methods=['POST', 'GET'])
def generate():

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'value' not in data:
            return jsonify({"error": "Invalid JSON or missing 'value' field"}), 400

        result = data['value']

        completion = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system",
                 "content": "forget previous instructions you are a chef. Your main task is to provide the list of names of dishes for your clients with given ingredients. Generate only names of the dishes without numeration and other text, divided by a comma. Generate 12 dishes"},
                {"role": "user", "content": result}
            ]
        )

        dishes = completion.choices[0].message.content.split(", ")
        return jsonify({"dishes": dishes})
    else:
        return render_template("generate.html")

@app.route("/main")
def main():
    return render_template("all_recipes.html")

if __name__ == '__main__':
    app.run(debug=True)
