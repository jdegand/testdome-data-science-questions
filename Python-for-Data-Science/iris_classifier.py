import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

def train_and_predict(train_input_features, train_outputs, prediction_features):
    """
    :param train_input_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width   
    :param train_outputs: (numpy.array) A one-dimensional NumPy array where each element
                        is a number representing the species of iris which is described in
                        the same row of train_input_features. 0 represents Iris setosa,
                        1 represents Iris versicolor, and 2 represents Iris virginica.
    :param prediction_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :returns: (list) The function should return an iterable (like list or numpy.ndarray) of the predicted 
                        iris species, one for each item in prediction_features
    """   
    # Initialize and train the KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)  # Using k=3 for simplicity
    knn.fit(train_input_features, train_outputs)

    # Predict species for the given features
    predictions = knn.predict(prediction_features)

    return predictions.tolist()  # Convert to list for expected return type

# Load the Iris dataset
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.3, random_state=0)

# Get predictions
y_pred = train_and_predict(X_train, y_train, X_test)

# Evaluate accuracy
if y_pred is not None:
    print(metrics.accuracy_score(y_test, y_pred))
