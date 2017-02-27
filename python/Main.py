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
    
Main()