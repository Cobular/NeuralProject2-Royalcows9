import numpy
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense


numpy.random.seed(1)

my_data = numpy.loadtxt("C:\\Users\\jdc10\\floobits\\share\\Royalcows9\\NeuralProject2\\Datasets\\mainData.csv",
                        delimiter=",")
X = my_data[:, 0:29]
Y = my_data[:, 28:29]

X_train5, X_test5, y_train5, y_test5 = train_test_split(X, Y, test_size=0.20, random_state=42)


main_model = Sequential()
main_model.add(Dense(32, activation="relu", input_dim=28))
main_model.add(Dense(10, activation="relu"))
main_model.add(Dense(2, activation="relu"))

print(X)
