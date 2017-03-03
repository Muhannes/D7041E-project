from DataReader import *
from DataCluster import *
from Classifier import *

import numpy as np

def Main():
    dataReader = DataReader()
    allUserData = dataReader.loadData("DSL-StrongPasswordData") #loads all users data
    
    
    
    # second person for comparison
    owner_index = 0
    first_time = True
    for i in range(0,50):
        userDataRaw = allUserData[i] #data from 1 user
        userData = dataReader.formatData(userDataRaw) #formats data (strips user and session ids etc), returns Matrix.
        if i == owner_index:
            print "person1 created!"
            person1 = DataCluster(userData[0:300])
            test_data_right = userData[300:]
            print test_data_right
        else:
            if first_time:
                test_data_wrong = userData
                first_time = False
            else:
                test_data_wrong = np.concatenate((test_data_wrong,userData), axis=0)
            
    
    
    classifier = Classifier()
    
    print "correct person: " + str(classifier.compare_all(person1, test_data_right, True))
    print "wrong person: " + str(classifier.compare_all(person1, test_data_wrong, False))
    
    
Main()