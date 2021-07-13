#Import the load_iris function from datsets module
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#import the KNeighborsClassifier class from sklearn
from sklearn.neighbors import KNeighborsClassifier

#import metrics model to check the accuracy
from sklearn import metrics

import matplotlib.pyplot as plt

# https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
# https://github.com/Msanjayds/Machine_Learning_Projects/blob/master/1.%20KNN%20on%20Iris%20Datset.ipynb

#Create bunch object containing iris dataset and its attributes.
iris = load_iris()

print(type(iris))

# print(iris.data)

print(iris.feature_names)

#Integers representing the species: 0 = setosa, 1=versicolor, 2=virginica
print(iris.target)

# 3 classes of target
print(iris.target_names)

print(type(iris.data))
print(type(iris.target))

# we have a total of 150 observations and 4 features
print(iris.data.shape)

# Feature matrix in a object named X
X = iris.data
# response vector in a object named y
y = iris.target

print(X.shape)
print(y.shape)


# splitting the data into training and test sets (80:20)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)

#shape of train and test objects
print(X_train.shape)
print(X_test.shape)

# shape of new y objects
print(y_train.shape)
print(y_test.shape)

#Try running from k=1 through 25 and record testing accuracy
k_range = range(1,26)
scores = {}
scores_list = []
for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train,y_train)
        y_pred=knn.predict(X_test)
        scores[k] = metrics.accuracy_score(y_test,y_pred)
        scores_list.append(metrics.accuracy_score(y_test,y_pred))

print(scores)

#plot the relationship between K and the testing accuracy

plt.plot(k_range,scores_list)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
# plt.show()

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)

KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')


#0 = setosa, 1=versicolor, 2=virginica
classes = {0:'setosa',1:'versicolor',2:'virginica'}

#Making prediction on some unseen data
#predict for the below two random observations
x_new = [[3,4,5,2],
         [5,4,2,2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])
