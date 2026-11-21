
import pandas as pd
import numpy as np

# Read dataset
data = pd.read_csv("data/ott_ratings.csv")

# 1. Display dataset
print("\n----- OTT RATING DATA -----")
print(data.head())

# 2. Total number of movies and shows
print("\nTotal Titles:", len(data))

# 3. Total OTT platforms
print("\nOTT Platforms:")
print(data["platform"].unique())

# 4. Average rating
print("\nAverage Rating:")
print(data["rating"].mean())

# 5. Highest rated title
print("\nHighest Rated Title:")
print(data[data["rating"] == data["rating"].max()])

# 6. Lowest rated title
print("\nLowest Rated Title:")
print(data[data["rating"] == data["rating"].min()])

# 7. Platform wise average rating
print("\nPlatform Wise Average Rating:")
print(data.groupby("platform")["rating"].mean())

# 8. Genre wise average rating
print("\nGenre Wise Average Rating:")
print(data.groupby("genre")["rating"].mean())

# 9. Number of titles on each platform
print("\nNumber of Titles on Each Platform:")
print(data["platform"].value_counts())

# 10. Top 5 highest rated titles
print("\nTop 5 Highest Rated Titles:")
print(data.sort_values("rating", ascending=False).head(5))

# 11. NumPy calculations
ratings = np.array(data["rating"])

print("\n----- NUMPY ANALYSIS -----")
print("Mean Rating:", np.mean(ratings))
print("Median Rating:", np.median(ratings))
print("Maximum Rating:", np.max(ratings))
print("Minimum Rating:", np.min(ratings))
print("Standard Deviation:", np.std(ratings))

print("\nAnalysis Completed Successfully!")
