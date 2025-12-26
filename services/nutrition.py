FOOD_NUTRITION = {
    "dal": {
        "protein": 9,
        "carbs": 20,
        "fat": 2,
        "iron": 2
    },
    "rice": {
        "protein": 3,
        "carbs": 45,
        "fat": 1
    },
    "egg": {
        "protein": 6,
        "fat": 5,
        "vitamin_b12": 1
    },
    "milk": {
        "protein": 8,
        "fat": 5,
        "calcium": 300
    }
}

# app/services/nutrition.py

def analyze_food_text(text: str) -> dict:
    words = text.lower().split()
    total_nutrition = {}

    for word in words:
        if word in FOOD_NUTRITION:
            nutrients = FOOD_NUTRITION[word]

            for nutrient, value in nutrients.items():
                total_nutrition[nutrient] = (
                    total_nutrition.get(nutrient, 0) + value
                )

    return total_nutrition
