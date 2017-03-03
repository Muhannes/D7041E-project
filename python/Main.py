from DataReader import *
from DataCluster import *
from Classifier import *

import numpy as np

def Main():
    dataReader = DataReader()
    allUserData = dataReader.loadData("DSL-StrongPasswordData") #loads all users data
    
    classifier = Classifier()
    
    for k in range(0,50):
        correct_person_accuracy = []
        wrong_person_accuracy = []
        owner_index = k # index for the user that is to be tested
        first_time = True # temp variable for checking if first time creating test_data_wrong
        for i in range(0,50):
            userDataRaw = allUserData[i] #data from 1 user
            userData = dataReader.formatData(userDataRaw) #formats data (strips user and session ids etc), returns Matrix.
            if i == owner_index:
                print "person1 created!"
                np.random.shuffle(userData) # Shuffle to get data from different sessions
                person1 = DataCluster(userData[0:300]) # creates the person to be tested
                test_data_right = userData[300:]
                # print test_data_right
            else:
                if first_time:
                    test_data_wrong = userData
                    first_time = False
                else:
                    test_data_wrong = np.concatenate((test_data_wrong,userData), axis=0)
        correct_person_accuracy.append(classifier.compare_all(person1, test_data_right, True))
        wrong_person_accuracy.append(classifier.compare_all(person1, test_data_wrong, False))
            
    
    
    
    
    print "correct person: " + str(np.mean(correct_person_accuracy))
    print "wrong person: " + str(np.mean(wrong_person_accuracy))
    
    
Main()