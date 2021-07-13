# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix

# https://towardsdatascience.com/knn-in-python-835643e2fb53

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset)
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Scale Features because age has smaller increments than salary
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# find and optimize k

df_results = pd.DataFrame()
k_list = []
f1_list = []
accuracy_list = []

k = 1
while k < 11:
    classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
    classifier.fit(X_train, y_train)
    Y_pred = classifier.predict(X_test)
    f1_value = metrics.f1_score(y_test, Y_pred, average='weighted')
    accuracy = metrics.accuracy_score(y_test, Y_pred)
    k_list.append(k)
    f1_list.append(f1_value)
    accuracy_list.append(accuracy)
    k += 1

# print(k_list)
# print(f1_list)
# print(accuracy_list)

df_results['k'] = k_list
df_results['f1'] = f1_list
df_results['accuracy'] = accuracy_list

# print(df_results)

# Fitting classifier to the Training set
classifier = KNeighborsClassifier(n_neighbors = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

#print(y_pred)

X_trans = sc.transform(X)
y_pred_trans = classifier.predict(X_trans)
#print(y_pred_trans)
dataset['results'] = y_pred_trans
dataset.to_csv('dataset.csv')

test_data = [[29, 43000]]
test_trans = sc.transform(test_data)
y_pred_test = classifier.predict(test_trans)
print(y_pred_test)
