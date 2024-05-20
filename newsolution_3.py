# -*- coding: utf-8 -*-
"""NewSolution-3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1773lSm7TJ9nabc7XDIYGMvC9vgTr-o-e

## Task 1: Import libraries
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

"""## Task 2: Load the dataset

"""

#Load the Dataset
data = pd.read_csv("/content/housing.csv")
# After loading the dataset, print the first five rows of the dataset
data.head()

"""## Task 3: Explore the Dataset"""

#Use the following structure to get the summary statistics of the dataset.
data.iloc[:, :-1].describe()

"""## Task 4: Explore Variables"""

# Find the correlation between longitude,	latitude,	housing_median_age, total_rooms,	total_bedrooms,	population,	households,	median_income, median_house_value
data.iloc[:, :-1].corr()

"""## Task 5: Check for Null Values"""

# Check for Null values within your Dataset
data.isnull().sum()

data = data.dropna()
data.iloc[:, :-1].isnull().sum()

"""## Task 6: Remove Unnecessary Columns"""

data = pd.get_dummies(data)
data = data.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12,13, 8]]
data.head()

"""## Task 7: Create Dependent Variable  """

y = data.iloc[:, -1] # median value of homes
print(y[0:5]) # print the first five values of your dependent variable

"""## Task 8: Create Independent Variable"""

X = data.iloc[:, :-1] # Create dependent variables

X.head()  # print the first five values of your dependent variables

"""## Task 9: Train Test Split data"""

# Train test split your data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=43)

X_test.shape

"""## Task 10:  Add a constant and Fit your Model"""

# Add a constant to X_traing dataset and give a new variable name.
X_train_new = sm.add_constant(X_train)
# Creates an Ordinary Least Squares (OLS) regression model using the sm.OLS()
model = sm.OLS(y_train, X_train_new.astype('float') ).fit()

X_test_new = sm.add_constant(X_test)
predictions = model.predict(X_test_new.astype('float'))

"""## Task 11: Run Summary and Interpret findings"""

# Produce Summary
model.summary()

"""- Multicollinearity is a statistical concept where several independent variables in a model are correlated. Two variables are considered perfectly collinear if their correlation coefficient is +/- 1.0. Multicollinearity among independent variables will result in less reliable statistical inferences.
- 67.6\% of the variance in price can be explained by the independant variables. R-squared is a measure of how well a linear regression model “fits” a dataset. A R-squared between 0.50 to 0.99 is acceptable when most of the explanatory variables are statistically significant.
- The F-test of overall significance indicates whether your linear regression model provides a better fit to the data than a model that contains no independent variables.
  - The null hypothesis states that the model with no independent variables fits the data as well as your model.
  - The alternative hypothesis says that your model fits the data better than the intercept-only model.
  - An F statistic of at least 3.95 is needed to reject the null hypothesis at an alpha level of 0.1. At this level, you stand a 1% chance of being wrong.
- Log Likelihood value is a measure of goodness of fit for any model. Higher the value, better is the model.
- The residual degrees of freedom are the remaining "dimensions" that you could use to generate a new data set that "looks" like your current data set.
- A t-test is an inferential statistic used to determine if there is a significant difference between the means of two groups and how they are related. The greater the magnitude of T, the greater the evidence against the null hypothesis.
- The Durbin-Watson statisticlies in the range 0-4. A value of 2 or nearly 2 indicates that there is no first-order autocorrelation. An acceptable range is 1.50 - 2.50. Where successive error differences are small, Durbin-Watson is low (less than 1.50); this indicates the presence of positive autocorrelation.
- The Jarque-Bera test is a goodness-of-fit test that measures if sample data has skewness and kurtosis that are similar to a normal distribution. The Jarque-Bera test statistic is always positive, and if it is not close to zero, it shows that the sample data do not have a normal distribution.
- Acceptable values of skewness fall between − 3 and + 3
- Acceptable values of kurtosis is appropriate from a range of − 10 to + 10

# Task 12 Plot findiings
"""

X_train_new.shape

X_test.shape

# check scatter plot between median_income and median_house_value
plt.figure(figsize=(10,5))
plt.scatter(data["median_income"],data["median_house_value"], alpha=0.3)
plt.xlabel('median_income')
plt.ylabel('Median house value')
plt.title('Linear correlation median_income/Median House value')

X_test_new = sm.add_constant(X_test)
predictions = model.predict(X_test_new)

df = pd.DataFrame({"Y_test": y_test , "Y_pred" : predictions})
df.sort_values(by=['Y_test', 'Y_pred'], inplace=True, ignore_index=True)
df['idx'] = range(len(df))
plt.scatter(df.idx, df.Y_pred, c="blue", alpha=0.5, marker="+")
plt.scatter(df.idx, df.Y_test, c="green", alpha=0.4, marker="x")
plt.show()

"""df = pd.DataFrame({"Y_test": y_test , "Y_pred" : predictions})
plt.plot(df[:3000])
plt.legend(['Actual','Predicted'])
"""

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

import numpy as np

score = np.sqrt(mse)

print("The Root Mean Squared Error of our Model is {}".format(round(score, 2)))

from sklearn.metrics import mean_absolute_error

score = mean_absolute_error(y_test,predictions)

print("The Mean Absolute Error of our Model is {}".format(round(score, 2)))

"""We can see that the RMSE value is larger than the MAE. This is a result of some significant errors in the dataset."""