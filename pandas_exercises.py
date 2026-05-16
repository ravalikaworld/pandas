# ================================================
# KAGGLE PANDAS COMPLETE EXERCISES
# Data Analyst: Ravalika
# GitHub: github.com/ravalikaworld
# Course: Kaggle Pandas (Completed ✅)
# ================================================

import pandas as pd

# ================================================
# LESSON 1 — CREATING, READING & WRITING
# ================================================

# Exercise 1 — Create fruits DataFrame
fruits = pd.DataFrame({
    "Apples": [30],
    "Bananas": [21]
})
print("Exercise 1 - Fruits:")
print(fruits)

# Exercise 2 — Create fruit_sales DataFrame
fruit_sales = pd.DataFrame({
    "Apples": [35, 41],
    "Bananas": [21, 34]
}, index=["2017 Sales", "2018 Sales"])
print("\nExercise 2 - Fruit Sales:")
print(fruit_sales)

# Exercise 3 — Create ingredients Series
ingredients = pd.Series(
    ["4 cups", "1 cup", "2 large", "1 can"],
    index=["Flour", "Milk", "Eggs", "Spam"],
    name="Dinner"
)
print("\nExercise 3 - Ingredients:")
print(ingredients)

# Exercise 4 — Read CSV file
# reviews = pd.read_csv(
#     "../input/wine-reviews/winemag-data_first150k.csv",
#     index_col=0
# )

# Exercise 5 — Save to CSV
animals = pd.DataFrame({
    'Cows': [12, 20],
    'Goats': [22, 19]
}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")
print("\nExercise 5 - Saved animals to CSV!")

# ================================================
# LESSON 2 — INDEXING, SELECTING & ASSIGNING
# ================================================

# Setup data for indexing exercises
data = {
    "country": ["Italy","Portugal","US","US","US"],
    "description": ["Aromas include tropical",
                    "This is ripe and fruity",
                    "Tart and snappy",
                    "Pineapple rind",
                    "Much like the regular"],
    "points": [87, 87, 87, 87, 87],
    "price": [None, 15.0, 14.0, 13.0, 65.0],
    "variety": ["White Blend","Portuguese Red",
                "Pinot Gris","Riesling","Pinot Noir"]
}
reviews = pd.DataFrame(data)

# Select one column
desc = reviews["description"]
print("\nLesson 2 - Description column:")
print(desc)

# Select first row using iloc
first_row = reviews.iloc[0]
print("\nFirst row:")
print(first_row)

# Select first column using iloc
first_descriptions = reviews.iloc[:, 1]
print("\nFirst descriptions:")
print(first_descriptions)

# Select specific rows
sample_reviews = reviews.iloc[[1,2,3,5,8]]
print("\nSample reviews:")
print(sample_reviews)

# Select country and variety columns
cols = ['country', 'variety']
df = reviews.loc[:, cols]
print("\nCountry and variety:")
print(df)

# ================================================
# LESSON 3 — SUMMARY FUNCTIONS & MAPS
# ================================================

# Median points
median_points = reviews["points"].median()
print(f"\nMedian points: {median_points}")

# Unique countries
countries = reviews["country"].unique()
print(f"\nUnique countries: {countries}")

# Reviews per country
reviews_per_country = reviews["country"].value_counts()
print("\nReviews per country:")
print(reviews_per_country)

# Center points around mean using map
mean_points = reviews["points"].mean()
centered = reviews["points"].map(
    lambda p: p - mean_points
)
print("\nCentered points:")
print(centered)

# ================================================
# LESSON 4 — GROUPING & SORTING
# ================================================

# Count reviews per country
country_counts = reviews.groupby(
    "country")["points"].count()
print("\nLesson 4 - Reviews per country:")
print(country_counts)

# Best wine per country
best_wine = reviews.groupby(
    "country")["points"].max()
print("\nBest points per country:")
print(best_wine)

# Sort by points
sorted_reviews = reviews.sort_values(
    "points", ascending=False)
print("\nSorted by points:")
print(sorted_reviews[["country","points"]])

# ================================================
# LESSON 5 — DATA TYPES & MISSING VALUES
# ================================================

# Check data types
print("\nLesson 5 - Data types:")
print(reviews.dtypes)

# Find missing values
print("\nMissing values:")
print(reviews.isnull().sum())

# Fill missing price with mean
reviews["price"] = reviews["price"].fillna(
    reviews["price"].mean()
)
print("\nAfter filling missing price:")
print(reviews["price"])

# Drop missing values
reviews_clean = reviews.dropna()
print(f"\nRows after dropna: {len(reviews_clean)}")

# ================================================
# LESSON 6 — RENAMING & COMBINING
# ================================================

# Rename column
reviews_renamed = reviews.rename(
    columns={"points": "score",
             "country": "nation"}
)
print("\nLesson 6 - Renamed columns:")
print(reviews_renamed.columns.tolist())

# Combine two DataFrames
df1 = reviews.iloc[:3]
df2 = reviews.iloc[3:]
combined = pd.concat([df1, df2])
print(f"\nCombined DataFrame rows: {len(combined)}")

print("\n" + "="*50)
print("KAGGLE PANDAS COURSE - COMPLETED! ✅")
print("All 6 lessons done!")
print("="*50)



commit message: "complete Kaggle Pandas exercises"
