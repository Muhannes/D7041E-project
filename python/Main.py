from DataReader import *
from DataCluster import *
from Classifier import *

import numpy as np

def Main():
    dataReader = DataReader()
    allUserData = dataReader.loadData("DSL-StrongPasswordData") #loads all users data
    
    classifier = Classifier()
    scalar = 1.0
    scalarCap = 1.6
    
    dimDeviation = 1
    dimCap = 21
    
    while(dimDeviation < dimCap):
        print "testing dims: "+str(dimDeviation)
        for k in range(0,50):
            correct_person_accuracy = []
            wrong_person_accuracy = []
            owner_index = k # index for the user that is to be tested
            first_time = True # temp variable for checking if first time creating test_data_wrong
            #print "testing for person "+str(k)+" created!"
            for i in range(0,50):
                userDataRaw = allUserData[i] #data from 1 user
                userData = dataReader.formatData(userDataRaw) #formats data (strips user and session ids etc), returns Matrix.
                if i == owner_index:
                    np.random.shuffle(userData) # Shuffle to get data from different sessions
                    person1 = DataCluster(userData[0:300], scalar) # creates the person to be tested
                    test_data_right = userData[300:]
                    # print test_data_right
                else:
                    if first_time:
                        test_data_wrong = userData
                        first_time = False
                    else:
                        test_data_wrong = np.concatenate((test_data_wrong,userData), axis=0)
            correct_person_accuracy.append(classifier.compare_all(person1, test_data_right, True, dimDeviation))
            wrong_person_accuracy.append(classifier.compare_all(person1, test_data_wrong, False, dimDeviation))
            
        print "False recognition rate: " + str(1-np.mean(correct_person_accuracy))
        print "False acceptance rate: " + str(1-np.mean(wrong_person_accuracy))
#       scalar += 0.1
        dimDeviation += 1
            
    
    
    
    

    
    
Main()