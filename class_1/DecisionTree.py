from sklearn import tree, linear_model, naive_bayes

decisionTreeClassifier = tree.DecisionTreeClassifier()
sgdClassifier = linear_model.SGDClassifier(loss="hinge", penalty="l2")
gaussianNB = naive_bayes.GaussianNB()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38],
     [154, 54, 37], [166, 65, 40], [190, 90, 47],
     [175, 64, 39], [177, 70, 40], [159, 55, 37],
     [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female',
     'female', 'male', 'male',
     'female', 'female', 'female',
     'male', 'male']

decisionTreeClassifier = decisionTreeClassifier.fit(X, Y)
sgdClassifier = sgdClassifier.fit(X, Y)
gaussianNB = gaussianNB.fit(X, Y)

decisionTreeClassifierPrediction = decisionTreeClassifier.predict([[190, 70, 43]])
sgdClassifierPrediction = sgdClassifier.predict([[190, 70, 43]])
gaussianNBPrediction = gaussianNB.predict([[190, 70, 43]])

print('sgdClassifierPrediction: ')
print(sgdClassifierPrediction)
print('')
print('decisionTreeClassifierPrediction: ')
print(decisionTreeClassifierPrediction)
print('')
print('gaussianNBPrediction: ')
print(gaussianNBPrediction)