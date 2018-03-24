from NBClassifier import NBClassifier
import project3_functions
import project3_datafunctions
import sys

clf = NBClassifier()

X_raw = project3_functions.read_file(sys.argv[2])
y_raw = None
if len(sys.argv) > 3:
    y_raw = project3_functions.read_file(sys.argv[3])

X = project3_datafunctions.extract_features(X_raw)

means_and_variances, priors = project3_functions.load_model(sys.argv[1])
predictions = clf.predict(X, means_and_variances, priors)
if y_raw != None:
    accuracy = project3_functions.evaluate(predictions, y_raw)
    print "Accuracy: {}".format(accuracy)
else:
    for seq in predictions:
        print("{}".format("".join(seq)))


