import numpy as np

#Holds the data of a user.
class DataCluster(object):
    def __init__(self, userData):
        self.train(userData)

    def train(self, X):
        # standard deviation( could come in handy.)
        self.std = np.std(X)
        self.min = np.min(X)
        self.max = np.max(X)
        self.average = (self.max - self.min)/2
        # mean value of every dimension
        self.mean = np.mean(X, axis=0)
        print("std: " + str(self.std))
        print("min: " + str(self.min))
        print("max: " + str(self.max))
        print("(max - min)/2: " + str(self.average))
        # print("mean: " + str(self.mean))
        

        
    
