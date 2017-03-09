import numpy as np

class Classifier(object):
    def __init__(self):
        pass
    
    # Check L2 distance to user mean, see if close enough
#     def compare(self, user, testData):
#         # The L2 distance
#         distance = np.sqrt(np.sum(np.power(user.mean - testData, 2)))
#         return distance < max_distance
        
    def compare(self, user, testData):
        counter = 0
        differance = np.subtract(user.mean, testData)
        differance = differance.tolist()
        deviation = user.accepted_deviation.tolist()
        for i in range(0, len(differance[0])) :
            if(abs(differance[0][i]) > deviation[0][i]):
                counter = counter + 1
#                 print "INDEX differs : "+str(i)
                if(counter > 10):
                    return False
        return True
            
    def compare_all(self, user, testData, label):
        predictions = []
        for data in testData:
            prediction = self.compare(user, data)
            if prediction == label:
                predictions.append(1)
            else:
                predictions.append(0)
        return np.mean(predictions)    
