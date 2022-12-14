import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Binarizer

input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# Binarization
data_binarized = preprocessing.Binarizer(threshold = 0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)


# Mean Removal
print("Mean = ", input_data.mean(axis = 0))
print("Std deviation = ", input_data.std(axis = 0))

# Mean and Standar deviation removed
data_scaled = preprocessing.scale(input_data)
print("Mean =", data_scaled.mean(axis = 0))
print("Std deviation =", data_scaled.std(axis = 0))
