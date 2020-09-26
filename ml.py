from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import datasets
import pandas

dataset = pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=0.2,
                                                                                random_state=5)

models = [('LR', LogisticRegression()), ('KNN', KNeighborsClassifier()), ('SVM', SVC())]
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=12, shuffle=True)
    result = model_selection.cross_val_score(model, x_train, y_train, cv=kfold)
    print(result)
    print('*' * 10)
    results.append(result)
    names.append(name)
