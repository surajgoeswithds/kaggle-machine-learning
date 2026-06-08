#You're a real estate agent in Iowa. You have a spreadsheet of 1,460 houses with their features and sale prices. Your boss says: "Build me something that predicts house prices so we can estimate new listings."
#You have these columns available: LotArea, YearBuilt, 1stFlrSF, 2ndFlrSF, FullBath, BedroomAbvGr, TotRmsAbvGrd, SalePrice.
#Your job: write the entire pipeline — loading to MAE — from memory. Treat SalePrice as what you're predicting

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#load data
home_data = pd.read_csv('home_data.csv')

#defining y
y = home_data.SalePrice

#defining X
features = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
X = home_data[features]

#splitting data
train_X , val_X , train_y , val_y = train_test_split(X , y , random_state=1)
my_model = DecisionTreeRegressor(random_state=1) #In the model, random_state ensures the model builds the same tree every time you run it. Decision trees have some internal randomness in how they're built. Locking it means reproducible results.
my_model.fit(train_X , train_y)

#Predict and calculate MAE
predict_hp = my_model.predict(val_X) #You're predicting house prices for houses the model has never seen before.
#The model learned patterns from train_X and train_y. Now you give it val_X — the features of the 25% held-back houses — and ask it to guess their prices.
#Those guesses you then compare against val_y — the real prices of those same houses — to calculate MAE.
#The model doesn't "know" it's predicting prices during .predict(). It learned the relationship between features and prices during .fit(train_X, train_y). That's where the learning happened.
#When you call .predict(val_X), you're just feeding it feature combinations. The model says "I've seen patterns like this before — a house with these features was worth around $X" and outputs a number. That number happens to be a price because that's what it learned to output during training.
#Think of it like this — you teach a student that: big house + new build + good location = high price. Later you show them just the house details (features). They output a price estimate. They don't need to be told "output a price" — they already learned that's what the output means.
MAE = mean_absolute_error(predict_hp , val_y )
print(MAE)
