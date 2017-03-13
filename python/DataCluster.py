import numpy as np
from Classifier import *

#Holds the data of a user.
class DataCluster(object):
    def __init__(self, userData, scalar):
        self.train(userData, scalar)

    def train(self, X, scalar):
        # standard deviation( could come in handy.)
        self.accepted_deviation = np.std(X, axis=0) * scalar
        #print self.accepted_deviation
        self.min = np.min(X)
        self.max = np.max(X)
        self.average = (self.max - self.min)/2
        # mean value of every dimension
        self.mean = np.mean(X, axis=0)
#         print("std: " + str(self.accepted_deviation))
#         print("min: " + str(self.min))
#         print("max: " + str(self.max))
#         print("(max - min)/2: " + str(self.average))
        # print("mean: " + str(self.mean))
        
        classifier = Classifier()
        accuracy = 0
        accepted_accuracy = 0.8
        learning_rate = 1.05
#         
#         while(accuracy < accepted_accuracy):
#             accuracy = classifier.compare_all(self, X, True)
#             #print str(accuracy)
#             self.accepted_deviation = self.accepted_deviation*learning_rate

        
    
