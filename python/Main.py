from DataReader import *
from DataCluster import *
from Classifier import *

import numpy as np;

def Main():
    dataReader = DataReader()
    allUserData = dataReader.loadData("DSL-StrongPasswordData") #loads all users data
    
    userDataRaw = allUserData[0] #data from 1 user
    userData = dataReader.formatData(userDataRaw); #formats data (strips user and session ids etc), returns Matrix.
    print userData
    # second person for comparison
    userDataRaw = allUserData[1] #data from 1 user
    userData2 = dataReader.formatData(userDataRaw); #formats data (strips user and session ids etc), returns Matrix.
    
    
    person1 = DataCluster(userData[:300])
    
    classifier = Classifier()
    distances = classifier.compare_all(person1, userData[300:])
    print("Mean distance for correct user: " + str(np.mean(distances)))
    distances2 = classifier.compare_all(person1, userData2)
    print("Mean distance for incorrect user: " + str(np.mean(distances2)))
    
    
Main()