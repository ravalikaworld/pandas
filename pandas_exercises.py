# Kaggle Pandas Exercises
# Ravalika - Data Analyst
# github.com/ravalikaworld

import pandas as pd

# Exercise 1 - Fruits DataFrame
fruits = pd.DataFrame({
    "Apples": [30],
    "Bananas": [21]
})
print("Exercise 1 - Fruits:")
print(fruits)

# Exercise 2 - Fruit Sales
fruit_sales = pd.DataFrame({
    "Apples": [35, 41],
    "Bananas": [21, 34]
}, index=["2017 Sales", "2018 Sales"])
print("\nExercise 2 - Fruit Sales:")
print(fruit_sales)

# ---- EXERCISE 3 ----
# Create ingredients Series
ingredients = pd.Series(
    ["4 cups", "1 cup", "2 large", "1 can"],
    index=["Flour", "Milk", "Eggs", "Spam"],
    name="Dinner"
)
print("\nExercise 3 - Ingredients Series:")
print(ingredients)

# ---- EXERCISE 4 ----
# Read CSV file into DataFrame
reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data_first150k.csv",
    index_col=0
)
print("\nExercise 4 - Wine Reviews CSV:")
print(f"Total rows: {len(reviews)}")
print(reviews.head())
