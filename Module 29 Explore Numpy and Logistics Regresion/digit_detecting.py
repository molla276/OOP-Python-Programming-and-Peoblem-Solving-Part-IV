from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
digits = load_digits()
# print(digits.data.size)
# print(dir(digits))
# print(digits.data[0])
plt.gray()
# plt.matshow(digits.images[0])
# plt.show()

#data split
X = digits.data
Y = digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# print(X_train.shape)
# print(Y_train.shape)

model = LogisticRegression()
model.fit(X_train, Y_train)

# print('target value of the test', digits.target[1705])
result = model.predict([digits.data[1705]])
# print('test result', result)

accuracy = model.score(X_test, Y_test)
# print('model accuracy', accuracy)

Y_predicted = model.predict(X_test)
confusion = confusion_matrix(Y_test, Y_predicted)
#print(confusion)

plot_confusion_matrix(model, X_test,Y_test)
plt.show()
