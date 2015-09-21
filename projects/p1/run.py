import binary
import util
import datasets
import runClassifier
import dt

runClassifier.trainTestSet(dt.DT({'maxDepth': 5}), datasets.GenderData)
