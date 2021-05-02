import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression


# create rmse function to test rmse of model on training data
def rmse(prediction, actual):
    """
    Paramters:
        prediction: list of numbers representing predictions
        actual: list of numbers representing actual data
    Returns:
        A value representing the root mean squared error calculated on prediction and actual.
    """
    numerator = 0
    for index in range(len(prediction)):
        numerator += (prediction[index] - actual[index]) ** 2
    return math.sqrt(numerator / len(prediction))


# read in train and test data
train_df = pd.read_csv("PredictiveModelingAssessmentData.csv")
test_df = pd.read_csv("TestData.csv")
# print(train_df.head())
# print()
# print(test_df.head())
# print()

# create list of lists to hold x1 and x2 values in training data
x_train = []
for index in range(len(list(train_df['y']))):
    x1_element = train_df.loc[index]['x1']
    x2_element = train_df.loc[index]['x2']
    x_train.append([x1_element, x2_element])

# create list of lists to hold x1 and x2 values in testing data
x_test = []
for index in range(len(list(test_df['ID']))):
    x1_element = test_df.loc[index]['x1']
    x2_element = test_df.loc[index]['x2']
    x_test.append([x1_element, x2_element])
# print(x_test)

# create list to hold y values in training data
y = list(train_df['y'])

# turn lists into np arrays to pass into LinearRegression().fit() function
x_train = np.array(x_train)
x_test = np.array(x_test)
y = np.array(y)

# create linear regression model using training data
model = LinearRegression().fit(x_train, y)
print('Coefficients:', model.coef_, 'Intercept:', model.intercept_)
print()

# test out model on training data and print predicted y values
y_pred_train = model.predict(x_train)
print(y_pred_train)
print()

# calculate RMSE when model is ran on training data
print('RMSE:', rmse(list(y_pred_train), list(y)))
print()

# run model on testing data
y_pred_test = model.predict(x_test)
print(y_pred_test)

# create a new df to hold prediction of testing data
final_df = test_df.copy()
final_df.insert(test_df.shape[1], 'prediction', y_pred_test)
print(final_df)

final_df.to_csv('TestDataPredictions.csv')
