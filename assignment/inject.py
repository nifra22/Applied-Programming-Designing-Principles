from process import preprocessor

class Data:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        filter = [record for record in self.data if condition(record)]
        return filter
class Inject:
    def __init__(self, preprocessor):
        self.preprocessor = preprocessor
    def analyze(self, filter):
        pass

data = [r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv']
data1 = [{'PRODUCTLINE': 'Motorcycles'}, {'PRODUCTLINE': 'Cars'}, {'PRODUCTLINE': 'Motorcycles'}]
preprocessor = Data(data1)
analyzer = Inject(preprocessor)

filter = preprocessor.filter(lambda record: record['PRODUCTLINE'] == 'Motorcycles')
analyzer.analyze(filter)
