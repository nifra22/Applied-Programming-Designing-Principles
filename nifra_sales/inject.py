from abc import ABC, abstractmethod
import csv
import pandas as pd

# Interface for data injection
class IDataInjection(ABC):
    @abstractmethod
    def data_inject(self, path):
        pass

# CSV data injector implementation
class CSVDataInjector(IDataInjection):
    def data_inject(self, path):
        with open(path, "r") as c:
            csv_reader = csv.reader(c)
            csv_data = [row for row in csv_reader]
            return csv_data

# Excel data injector implementation
class ExcelDataInjector(IDataInjection):
    def data_inject(self, path):
        excel_data = pd.read_excel(path)
        return excel_data

# Factory class for creating data injectors
class DataInjectorFactory:
    @staticmethod
    def get_data_injector(file_type):
        if file_type == "csv":
            return CSVDataInjector()
        elif file_type == "excel":
            return ExcelDataInjector()
        else:
            raise ValueError("Unsupported file type")

# Example usage
if __name__ == "__main__":
    factory = DataInjectorFactory()

    # For CSV file
    csv_injector = factory.get_data_injector("csv")
    csv_data = csv_injector.data_inject('C:/Users/97150/OneDrive/Desktop/APDP/Data_new.csv')
    print("CSV Data:", csv_data)

    '''# For Excel file
    excel_injector = factory.get_data_injector("excel")
    excel_data = excel_injector.data_inject("path/to/your/file.xlsx")
    print("Excel Data:")
    print(excel_data)'''
