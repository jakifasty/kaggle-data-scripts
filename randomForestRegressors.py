from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('datasets/melb_data.csv')

features_data = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']

X = data[features_data] #fetures for the model to use
y = data.Price #target, we want to predict the price

train_X, train_y, test_X, test_y = train_test_split(X, y, random_state=1)
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(test_y, melb_preds))