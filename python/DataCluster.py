import numpy as np

#Holds the data of a user.
class DataCluster(object):
    def __init__(self, userData):
        self.train(userData)

    def train(self, X):
        # standard deviation( could come in handy.)
        self.std = np.std(X)
        # mean value of every dimension
        self.mean = np.mean(X, axis=0)
        # print("std: " + str(self.std))
        # print("mean: " + str(self.mean))
        

        
    
