from sklearn import tree
# första värdet är vikten, därefter är 0 ojämn och 1 är len yta
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# 0 är äpple och 1 är apelsin
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

myPrediction = clf.predict([[150,0]])

if myPrediction == 0:
     print("Jag tror att dethär är ett äpple")
else:
     print("Detta är nog en apelsin")