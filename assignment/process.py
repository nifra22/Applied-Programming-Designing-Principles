import pandas as pd
import dataclasses

data = pd.read_csv(r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv')
print(data.shape)
print(data.head(10))

class Data():
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        pass

    def handle_missing_values(self):
        pass

    def scale_features(self):
        pass

    def encode_categorical_variables(self):
        pass


data = [r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv']
preprocessor = Data(data)
preprocessor.clean_data()
preprocessor.handle_missing_values()
preprocessor.scale_features()
preprocessor.encode_categorical_variables()
