import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class MultiClassPerceptron(object):
    def __init__(self, Learn_Rate=0.01, Iterations=100, n_classes=10):
        self.learn_rate = Learn_Rate
        self.Iterations = Iterations
        self.n_classes = n_classes
        self.weights = None
        self.errors_ = []  # Storing the number of misclassifications for each epoch

    def fit(self, X, y):
        self.weights = np.zeros((self.n_classes, X.shape[1] + 1))
        for _ in range(self.Iterations):
            errors = 0
            for xi, target in zip(X, y):
                actual_class = self.predict(xi)
                if actual_class != target:
                    self.weights[target, 1:] += self.learn_rate * xi
                    self.weights[target, 0] += self.learn_rate
                    self.weights[actual_class, 1:] -= self.learn_rate * xi
                    self.weights[actual_class, 0] -= self.learn_rate
                    errors += 1
            self.errors_.append(errors)

    def net_input(self, X, w):
        return np.dot(X, w[1:]) + w[0]

    def predict(self, X):
        results = np.dot(self.weights[:, 1:], X) + self.weights[:, 0]
        return np.argmax(results)

# Load the digits dataset
digits = load_digits()

# Preparing the data
X, y = digits.data, digits.target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Standardizing the features
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Model training
Classifier = MultiClassPerceptron(Learn_Rate=0.001, Iterations=100)
Classifier.fit(X_train_std, y_train)

# Plotting the number of misclassifications over epochs
plt.plot(range(1, len(Classifier.errors_) + 1), Classifier.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.title('Perceptron - Loss over epochs')
plt.show()

# Evaluating the model accuracy
predictions = np.array([Classifier.predict(x) for x in X_test_std])
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy:.2%}")
