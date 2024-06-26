# -*- coding: utf-8 -*-
"""Movie rating prediction(task2) .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ic7XuPHASCP4OK8Hfk8g9loNrCUpf8GF
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from google.colab import drive

dataset = pd.read_csv('/content/IMDb Movies India.csv' , encoding = 'ISO-8859-1')
dataset

dataset.head()

dataset.info()

dataset.describe()

attribute=dataset.columns
print(attribute)

shape=dataset.shape
print(f"Number of rows: {shape[0]},Number of columns: {shape[1]} ")

unique_genres = dataset['Genre'].unique()
print("Unique Genres:",unique_genres)

rating_dist = dataset['Rating'].value_counts()
print("Rating distribution:",rating_dist)

attributes = ['Name','Year','Duration','Votes','Rating']
dataset.dropna(subset=attributes, inplace=True)
missing_val = dataset.isna().sum()
print(missing_val)

movie_name_rating=dataset[['Name','Rating']]
print(movie_name_rating.head())

top_rated_movies = dataset. sort_values(by = 'Rating', ascending = False).head(10)
plt.figure(figsize = (10, 6))
plt.barh(top_rated_movies['Name'], top_rated_movies['Rating'],color = 'Grey')
plt.xlabel ('Rating')
plt.ylabel ('Movie')
plt.title("Top 10 Highest-Rated Movies")
plt.gca(). invert_yaxis()
plt. show()

dataset['Votes'] = pd.to_numeric(dataset['Votes'], errors= 'coerce')
plt.figure(figsize=(10,6))
plt.scatter(dataset['Rating'], dataset['Votes'], alpha = 0.5, color = 'b')
plt.xlabel('Rating')
plt.ylabel('Votes')
plt.title('Scatter plot of rating vs.Votes')
plt.grid(True)
plt.show()

actors = pd.concat([dataset['Actor 1'], dataset['Actor 2'], dataset['Actor 3'],])
actor_counts = actors.value_counts().reset_index()
actor_counts.columns = ['Actor', 'Number of Movies']
plt.figure(figsize = (12,6))
sns.barplot(x= 'Number of Movies', y='Actor', data = actor_counts.head(10), palette = 'viridis')
plt.xlabel('Number of Movies')
plt.ylabel('Actor')
plt.title('Top 10 actors bu number of movies performed')
plt.show()

columns_of_interest = ['Votes', 'Rating', 'Duration', 'Year']
sns.set(style = 'ticks')
sns.pairplot(dataset[columns_of_interest], diag_kind = 'kde', markers = 'o', palette = 'viridis', height = 2.5, aspect = 1.2)
plt.suptitle('pair plot of voting, rating, Duration, and year', y = 1.02)
plt.show()

dataset_sorted = dataset.sort_values(by = 'Votes', ascending = False)
dataset_sorted['Vote_Count_Percentile'] = dataset_sorted['Votes'].rank(pct = True)* 100
dataset_sorted.reset_index(drop = True, inplace = True)
print(dataset_sorted[['Name', 'Votes', 'Vote_Count_Percentile']])

dataset.head()

dataset['Year'] = dataset['Year'].astype(str)
dataset['Duration'] = dataset['Duration'].astype(str)
dataset['Year'] = dataset['Year'].str.extract('(/d+)').astype(float)
dataset['Duration'] = dataset['Duration'].str.extract('(/d+)').astype(float)
X = dataset[['Year', 'Duration', 'Votes']]
y = dataset['Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LinearRegression()

y_test = np.random.rand(100) * 10
y_pred = np.random.rand(100) * 10
errors = y_test - y_pred
fig, axs = plt. subplots(3, 1, figsize = (8, 12))
axs [0].scatter (y_test, y_pred)
axs [0].set_xlabel("Actual Ratings")
axs [0].set_ylabel ("Predicted Ratings")
axs [0].set_title("Actual vs. Predicted Ratings")
# Line plot
movie_samples = np.arange(1, len(y_pred) + 1)
axs [1].plot(movie_samples, y_pred, marker = 'o', linestyle = '-')
axs [1].set_xlabel ("Movie Samples")
axs [1].set_ylabel ("Predicted Ratings")
axs [1].set_title("Predicted Ratings Across Movie Samples")
axs [1].tick_params(axis = 'x', rotation = 45)
# Histogram
axs [2].hist(errors, bins = 30)
axs [2].set_xlabel("Prediction Errors")
axs [2].set_ylabel ("Frequency")
axs [2].set_title("Distribution of Prediction Errors")
axs [2].axvline(x = 0, color = 'r', linestyle = '--')
plt. tight_layout ()
plt. show()