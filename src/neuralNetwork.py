# A neural network will be trained on the data provided through e.g. the Json-file.
# An alternative would be using a Scraping-mechanism.

import json
import tensorflow
import tensorflow.keras

eventtypes = json.loads(open('eventtypes.json').read())

class neuralNetwork:

    def train(eventtypes):
        pass