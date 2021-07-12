import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# https://medium.datadriveninvestor.com/k-nearest-neighbors-knn-7b4bd0128da7

dataset_1 = pd.read_csv('car.csv')

dataset_1 = dataset_1.dropna()

# print(dataset_1)

le  = preprocessing.LabelEncoder()
dataset_1['Buying_1'] = le.fit_transform(dataset_1['buying'])
dataset_1['Maint_1'] = le.fit_transform(dataset_1['maint'])
dataset_1['doors_1'] = le.fit_transform(dataset_1['doors'])
dataset_1['persons_1'] = le.fit_transform(dataset_1['persons'])
dataset_1['lug_boot_1'] = le.fit_transform(dataset_1['lug_boot'])
dataset_1['safety_1'] = le.fit_transform(dataset_1['safety'])

# print(dataset_1)

X= dataset_1.iloc[:,[7,8,9,10,11,12]]
Y=dataset_1.iloc[:,6]

X_train, X_test,Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

df_results = pd.DataFrame()
k_list = []
f1_list = []
accuracy_list = []

# print(df_results)

k = 1
while k < 11:
    classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    f1_value = metrics.f1_score(Y_test, Y_pred, average='weighted')
    accuracy = metrics.accuracy_score(Y_test, Y_pred)
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

print(df_results)

# k = 5
#
# classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
# classifier.fit(X_train, Y_train)
#
# Y_pred= classifier.predict(X_test)
#
# f1_value = metrics.f1_score(Y_test, Y_pred, average='weighted')
#
# print(f'\nk = {k}')
#
# print(f'accuracy =  {metrics.accuracy_score(Y_test, Y_pred)}')
#
# print(f'F1 value = {f1_value}')
#
# k = 6
#
# classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
# classifier.fit(X_train, Y_train)
#
# Y_pred= classifier.predict(X_test)
#
# f1_value = metrics.f1_score(Y_test, Y_pred, average='weighted')
#
# print(f'\nk = {k}')
#
# print(f'accuracy =  {metrics.accuracy_score(Y_test, Y_pred)}')
#
# print(f'F1 value = {f1_value}')
#
# k = 4
#
# classifier = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=2)
# classifier.fit(X_train, Y_train)
#
# Y_pred= classifier.predict(X_test)
#
# f1_value = metrics.f1_score(Y_test, Y_pred, average='weighted')
#
# print(f'\nk = {k}')
#
# print(f'accuracy =  {metrics.accuracy_score(Y_test, Y_pred)}')
#
# print(f'F1 value = {f1_value}')
