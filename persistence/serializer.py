# Utility functions for saving and loading serialized data.
import pickle


class Serializer:
# Save Python object to a file.
    @staticmethod
    def save_data(data, filename):
        with open(filename, "wb") as file:
            pickle.dump(data, file)
            
# Load Python object from a file.

    @staticmethod
    def load_data(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)


