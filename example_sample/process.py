from abc import ABC, abstractmethod
import pandas as pd

# Abstract factory class
class ImportFactory(ABC):
    @abstractmethod
    def create_importer(self):
        pass

# Abstract importer class
class Importer(ABC):
    @abstractmethod
    def import_data(self, file_path, column_names=None):
        pass

# CSV importer implementation
class CsvImporter(Importer):
    def import_data(self, file_path, column_names=None):
        data = pd.read_csv(file_path)
        if column_names:
            data.columns = column_names
        return data

# Excel importer implementation
class ExcelImporter(Importer):
    def import_data(self, file_path, column_names=None):
        data = pd.read_excel(file_path)
        if column_names:
            data.columns = column_names
        return data

# CSV factory implementation
class CsvImportFactory(ImportFactory):
    def create_importer(self):
        return CsvImporter()

# Excel factory implementation
class ExcelImporterFactory(ImportFactory):
    def create_importer(self):
        return ExcelImporter()

def import_data(factory: ImportFactory, file_path: str, column_names=None):
    importer = factory.create_importer()
    data = importer.import_data(file_path, column_names)
    return data

if __name__ == "__main__":
    csv_factory = CsvImportFactory()
    column_names = ["Retailer", "Retailer ID", "Invoice date", "Region", "State", "City", "Product", "Price per unit", "Unit sold", "Total sales", "Operating Profit", "Operating Margin", "Sales Method"]
    csv_data = import_data(csv_factory, 'C:/Users/97150/OneDrive/Desktop/APDP/Data_new.csv', column_names)
    print(csv_data.head())
