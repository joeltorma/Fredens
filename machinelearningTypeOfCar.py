from sklearn import tree
# första värdet är hästkrafter, andra värdet är antalet säten
features = [[300, 2], [450, 2], [200, 8], [150, 9]]
# 0 är sportbil och 1 är minivan
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

myPrediction = clf.predict([[200,7]])

if myPrediction == 0:
     print("Jag tror att dethär är en sportbil")
else:
     print("Detta är nog en minivan")