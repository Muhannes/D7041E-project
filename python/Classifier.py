import numpy as np

class Classifier(object):
    def __init__(self):
        pass
    
    # Check L2 distance to user mean, see if close enough
    def compare(self, user, testData, max_distance):
        # The L2 distance
        distance = np.sqrt(np.sum(np.power(user.mean - testData, 2)))
        return distance < max_distance
        

    
    def compare_all(self, user, testData, label):
        predictions = []
        for data in testData:
            prediction = self.compare(user, data, user.std*4)
            if prediction == label:
                predictions.append(1)
            else:
                predictions.append(0)
        return np.mean(predictions)    
