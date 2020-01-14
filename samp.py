

from sklearn import tree
X=[[181,123,100],[100,100,100],[123,500,400],]
Y=['male','female','male']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([[90,90,90]])
print(prediction)







