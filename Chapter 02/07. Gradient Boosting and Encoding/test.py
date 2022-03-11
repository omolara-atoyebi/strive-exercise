from tkinter import X
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

data = pd.read_csv("./insurance.csv")

x_train, x_test, y_train, y_test = train_test_split(data.values[:,:-1], data.values[:,-1], test_size=0.2, random_state = 0)


ct = ColumnTransformer( [('ordinal', OrdinalEncoder(handle_unknown= 'use_encoded_value', unknown_value = -1), [1,4,5] )] )

x_train = ct.fit_transform(x_train)
print(x_train)
# x_test = ct.transform(x_test)