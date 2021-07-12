from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

# Print the information contained within the dataset
print(data.keys(),"\n")
#Print the feature names
count=0
for f in data.feature_names:
	count+=1
	print(count,"-",f)
#Print the classes
print("Target Names: ",data.target_names,"\n")
#Printing the Initial Few Rows
print("Data Sample:\n",data.data[0:3], "\n")
#Print the class values of first 30 datapoints
print("Target Sample(First 30): ",data.target[0:30], "\n")
#Print the dimensions of data
print("Data Shape: ",data.data.shape, "\n")

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, test_size=0.1) # 90% training and 10% test


# HEATMAP
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data1 = pd.DataFrame(data.data)
data1.columns = data.feature_names
NUM_POINTS = 7
features_mean= list(data1.columns[1:NUM_POINTS+1])
feature_names = data.feature_names[1:NUM_POINTS+1]
print(feature_names)
f,ax = plt.subplots(1,1) #plt.figure(figsize=(10,10))
sns.heatmap(data1[features_mean].corr(), annot=True, square=True, cmap='coolwarm')
# Set number of ticks for x-axis
ax.set_xticks([float(n)+0.5 for n in range(NUM_POINTS)])
# Set ticks labels for x-axis
ax.set_xticklabels(feature_names, rotation=25, rotation_mode="anchor",fontsize=10)
# Set number of ticks for y-axis
ax.set_yticks([float(n)+0.5 for n in range(NUM_POINTS)])
# Set ticks labels for y-axis
ax.set_yticklabels(feature_names, rotation='horizontal', fontsize=10)
plt.title("Correlation between various features")
plt.show()
plt.close()

#SCATTER MATRIX
#Color Labels - 0 is benign and 1 is malignant
color_dic = {0:'red', 1:'blue'}
target_list = list(data['target'])
colors = list(map(lambda x: color_dic.get(x), target_list))
#Plotting the scatter matrix
sm = pd.plotting.scatter_matrix(data1[features_mean], c= colors, alpha=0.4, figsize=((10,10)))
plt.suptitle("How well a feature separates the Malignant Points from the Benign Ones")
plt.show()


#ACCURACY & MODEL BUILDING
#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#Create KNN Classifiers
knn1 = KNeighborsClassifier(n_neighbors=1)
knn5 = KNeighborsClassifier(n_neighbors=5)
knn10 = KNeighborsClassifier(n_neighbors=10)

#Train the model using the training sets
knn1.fit(X_train, Y_train)
#Predict the response for test dataset
Y_pred = knn1.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("\n\nK=1, Accuracy:",round(metrics.accuracy_score(Y_test, Y_pred)*100,1), "%")

#Train the model using the training sets
knn5.fit(X_train, y=Y_train)
#Predict the response for test dataset
Y_pred = knn5.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("K=5 Accuracy:",round(metrics.accuracy_score(Y_test, Y_pred)*100,1), "%")

#Train the model using the training sets
knn10.fit(X_train, Y_train)
#Predict the response for test dataset
Y_pred = knn10.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("K=10 Accuracy:",round(metrics.accuracy_score(Y_test, Y_pred)*100,1), "%")
