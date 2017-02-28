import numpy as np

class Classifier(object):
    def __init__(self):
        pass
    
    # Check L2 distance to user mean, see if close enough
    def compare(self, user, testData):
        # The L2 distance
        distance = np.sqrt(np.sum(np.power(user.mean - testData, 2)))
        return distance

    
    def compare_all(self, user, testData):
        distances = []
        for data in testData:
            distance = self.compare(user, data)
            distances.append(distance)
        return distances