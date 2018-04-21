import numpy
import os
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import plot_model


# defined variabes
numpy.random.seed(1)
numEpochs = 100
batchSize = 32
dirOfNetwork = os.path.dirname(__file__)


# load and setup dataset
my_data = numpy.loadtxt("C:\\Users\\jdc10\\floobits\\share\\Royalcows9\\NeuralProject2\\Datasets\\mainData_Normalized.csv",
                        delimiter=",")
X = my_data[:, 0:28]
Y = my_data[:, 28:29]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)


# model code
main_model = Sequential()
main_model.add(Dense(32, activation="relu", input_dim=28))
# main_model.add(Dropout(0.2))
main_model.add(Dense(10, activation="relu"))
main_model.add(Dense(10, activation="relu"))
# main_model.add(Dropout(0.2))
main_model.add(Dense(1, activation="linear"))


# Compile the model
main_model.compile(optimizer='Adam',
    loss='mean_squared_error',
    metrics=['accuracy'])


# train the model
main_model.fit(X_train, Y_train,
    batch_size=batchSize,
    epochs=numEpochs,
    verbose=1,
    validation_data=(X_test, Y_test))


# data about model
score = main_model.evaluate(X, Y, verbose=0)
accuracyOutput = "%s: %.2f%%" % (main_model.metrics_names[1], score[1]*100)
print(accuracyOutput)

main_model.output_shape
main_model.summary()
main_model.get_config()
main_model.get_weights()


# Save Model to disk if user wants
userSaveDec = input("Do you want to save the model with an accuracy of: " + accuracyOutput + "? Y/N")
if userSaveDec == "Y":
    networkSaveFilename = input("Give filename for network save file:")
    model_json = main_model.to_json()
    with open(networkSaveFilename + ".json", "w") as json_file:
        json_file.write(model_json)
    main_model.save_weights(networkSaveFilename + ".h5")
    print("Saved model to disk")


