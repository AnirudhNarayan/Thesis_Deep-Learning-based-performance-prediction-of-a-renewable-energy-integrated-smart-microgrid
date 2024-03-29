# -*- coding: utf-8 -*-
"""Solar_Power_Thesis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHWSMu9X6R8mjCvFPJH30BC0TfckQyGh
"""

import pandas as pd;
import matplotlib.pyplot as plt
from numpy import array
from numpy import hstack
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

df = pd.read_csv('Grid_updated_extended.csv', header=None)

df[0] = pd.to_datetime(df[0]).dt.hour * 60 + pd.to_datetime(df[0]).dt.minute

X = df[[0]].values
y = df[1].values

scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score


mlp = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=1)
mlp.fit(X_train, y_train.ravel())

y_pred = mlp.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (Original X-axis, Original y-axis): {mse}")
print(f"R-squared: {r2}")

# Plotting the graph
X_test_original = scaler_X.inverse_transform(X_test)
y_test_original = scaler_y.inverse_transform(y_test)
y_pred_original = scaler_y.inverse_transform(y_pred.reshape(-1, 1))
plt.scatter(X_test_original, y_test_original, color='blue', label='Actual Values', s=10, marker='o')
plt.scatter(X_test_original, y_pred_original, color='red', label='Predicted Values', s=10, marker='x')
plt.title('Actual vs Predicted Values')
plt.xlabel('Original X-axis')
plt.ylabel('Original y-axis')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt



# Reshape the data to be 3D (samples, time steps, features) for LSTM
X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

# Initialize and train the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model (you can use different metrics based on your problem)
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
import matplotlib.pyplot as plt



# Reshape the data to be 3D (samples, time steps, features) for GRU
X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

# Initialize and train the GRU model
model = Sequential()
model.add(GRU(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model (you can use different metrics based on your problem)
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
import matplotlib.pyplot as plt


X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

model = Sequential()
model.add(SimpleRNN(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the CSV file
csv_file = 'Power_Flow_Sunny_updated_extended.csv'  # Replace with the path to your updated CSV file
df = pd.read_csv(csv_file)

# Extract the X and Y data
x_values = df[df.columns[0]]  # Assuming the X-axis is the first column
y_values = df[df.columns[1]]  # Assuming the Y-axis is the second column

# Create a line plot with smaller markers
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed
ax.plot(x_values, y_values, marker='o', markersize=5, linestyle='-')  # Adjust markersize as desired
ax.set_xlabel('Time (HH:MM)')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot of Data')

# Adjust X-axis tick spacing for visibility
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(rotation=45)  # Rotate X-axis labels for better visibility

# Show the plot
plt.tight_layout()
plt.grid(True)
plt.show()