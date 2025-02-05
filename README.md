# PantryChef - AI Recipe Generator 🧑🍳

**Smart meal suggestions using ingredients you own**  
Flask-powered web app that generates recipes and shopping lists using OpenAI's API.

## Key Features 🚩
- 🎯 **Ingredient-Based Suggestions** - Input available ingredients get 12 dish ideas
- 📋 **Structured Recipes** - Clear ingredient quantities and step-by-step instructions
- ⚡ **AI-Powered Generation** - Leverages GPT-4o-mini for creative recipe formulation
- 🔗 **API Integration** - Seamless OpenAI communication through Python client
- 🍳 **Recipe Breakdown** - Automatic parsing of:
  - Ingredient lists with quantities
  - Cooking instructions
  - Meal categories

## Tech Stack 💻
- **Backend**: Python/Flask
- **AI Engine**: OpenAI GPT-4o-mini
- **Web Client**: HTML/CSS/JavaScript
- **Additional Tools**:
  - Selenium (Web scraping module)    
  - Requests (HTTP handling)
  - JSONify (API responses)
## Core Code Structure 🔧
# AI Recipe Generation Endpoint
    @app.route("/generate", methods=['POST'])
    def generate():
        ingredients = request.json['value']
        completion = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{
                "role": "system",
                "content": "Generate 12 dish names from these ingredients:"
            }, {
                "role": "user",
                "content": ingredients
            }]
        )
        return jsonify({"dishes": completion.choices[0].message.content.split(", ")})

# Recipe Detail Endpoint
    @app.route("/recipe/<dish_name>")
    def get_recipe(dish_name):
        completion = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{
                "role": "system",
                "content": "Provide ingredients and instructions for:"
            }, {
                "role": "user",
                "content": dish_name
            }]
        )
        # Parses ingredients/instructions into Product objects
        return render_template('recipe.html',
                             ingredients=ingredient_objects,
                             instructions=formatted_steps)
## API Integration 🔌
# OpenAI Client Configuration
    from openai import OpenAI
    client = OpenAI()  # Requires OPENAI_API_KEY in environment
    
    # Structured Response Handling
    class Product:
        def __init__(self, name, quantity, recipe):
            self.name = name
            self.quantity = quantity
            self.recipe = recipe
    
    # Instruction Parsing Logic
    instructions = response.split("instructions: ")[1]
    steps = [step.strip() for step in instructions.split(".") if step]

# Project Structure 📂
    ├── app.py               # Main Flask application
    ├── templates/           # HTML templates
    │   ├── generate.html    # Ingredient input UI
    │   └── recipe.html      # Recipe display page
    └── static/              # CSS/JS assets
