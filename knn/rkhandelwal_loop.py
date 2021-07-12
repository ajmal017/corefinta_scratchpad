import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import random

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

# print(df_results)
# print(Y_pred)
# print(dataset_1)
# dataset_1.to_csv('dataset1.csv')
i = 0
test_data = [[3,3,0,0,0,2],[1,0,0,0,0,1],[1,0,0,1,1,2]]
y_pred_test_data = classifier.predict(test_data)
# print(y_pred_test_data)

df_test = pd.DataFrame()
df_test['inputs'] = test_data
df_test['results'] = y_pred_test_data
# print(df_test)
df_test.to_csv('df_test.csv')

# https://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array
df_array = dataset_1[['Buying_1', 'Maint_1', 'doors_1', 'persons_1', 'lug_boot_1', 'safety_1']].values
# print(df_array)

y_pred_test_data_array = classifier.predict(df_array)
# print(y_pred_test_data_array)

# create a random set of test data
rand_lst_n = []
rand_lst_p = []
rand_lst_q = []
rand_lst_r = []
rand_lst_s = []
rand_lst_t = []

for i in range(0,20):
    n = random.randint(0,3)
    p = random.randint(0,3)
    q = random.randint(0,3)
    r = random.randint(0, 2)
    s = random.randint(0, 2)
    t = random.randint(0, 2)
    rand_lst_n.append(n)
    rand_lst_p.append(p)
    rand_lst_q.append(q)
    rand_lst_r.append(r)
    rand_lst_s.append(s)
    rand_lst_t.append(t)
print(rand_lst_n)
print(rand_lst_p)
print(rand_lst_q)
print(rand_lst_r)
print(rand_lst_s)
print(rand_lst_t)

df_rand = pd.DataFrame()
df_rand['Buy2'] = rand_lst_n
df_rand['Maint2'] = rand_lst_p
df_rand['Doors2'] = rand_lst_q
df_rand['Persons2'] = rand_lst_r
df_rand['Lugg2'] = rand_lst_s
df_rand['Safety2'] = rand_lst_t
print(df_rand)

df_rand_array = df_rand[['Buy2', 'Maint2', 'Doors2', 'Persons2', 'Lugg2', 'Safety2']].values
print(df_rand_array)

y_pred_rand_array = classifier.predict(df_rand_array)
print(y_pred_rand_array)

df_rand['results'] = y_pred_rand_array
print(df_rand)

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
