import numpy as np

class DataReader(object):
    def __init__(self):
        pass

    #loads data from all users and puts it in a list of lists.
    def loadData(self, fileName):
        fileRef = "../dataSet/"+fileName+".txt"
        file = open(fileRef, "r")
        file.readline() #reads out the first line (non-data line)
        
        allUserData = [] 
        prevUser = "s002"
        userNumber = 0
                
        userData = []
        for line in file.readlines(): 
            line = line.split()
            if(line[0] == prevUser):
                userData.append(line)
            else:
                prevUser = line[0]
                allUserData.append(userData)
                userData = []
                userData.append(line)
        
        file.close()
        
        return allUserData
        
    #formats data into matrix of NxD (num of data by dimension)
    def formatData(self, Data):
        newData = []
        for line in Data:
            line = [float(i) for i in line[3:]]
            newData.append(line) #strips away userId, sessionId, repId and converts to float
            
        return np.matrix(newData)
        
        
        
        
        
        
        
        
        
        
        