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

#strategy classes
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data):
        pass


class TotalSalesByRegion(AnalysisStrategy):
    def __init__(self, sort_order = None):
        self.sort_order = sort_order

    def analyze(self, data):
        result = data.groupby('Region')['Total sales'].sum().reset_index()
        if self.sort_order:
            sort_map = {region: index for index, region in enumerate(self.sort_order)}
            result['sort_order'] = result['Region'].map(sort_map)
            result = result.sort_values('sort_order').drop(columns = 'sort_order')
        return result


class BestSellingProduct(AnalysisStrategy):
    def analyze(self, data):
        result = data.groupby('Product')['Unit sold'].sum().reset_index().sort_values(by='Unit sold', ascending=False)
        return result


class TotalSales(AnalysisStrategy):
    def __init__(self, period = 'M'):
        self.period = period

    def analyze(self, data):
        data['Invoice date'] = pd.to_datetime(data['Invoice date'])
        if self.period == 'W':
            period = data['Invoice date'].dt.to_period('W')
        elif self.period == 'Y':
            period = data['Invoice date'].dt.to_period('Y')
        else:
            period = data['Invoice date'].dt.to_period('M')
        result = data.groupby(period)['Total sales'].sum().reset_index()
        return result

class SalesMethodEachMonth(AnalysisStrategy):
    def analyze(self, data):
        data['Invoice date'] = pd.to_datetime(data['Invoice date'])
        result = data.groupby([data['Invoice date'].dt.to_period('M'), 'Sales Method'])[
            'Total sales'].sum().reset_index()
        return result

# Analyzer context class
class SalesAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AnalysisStrategy):
        self._strategy = strategy

    def analyze(self, data):
        return self._strategy.analyze(data)

if __name__ == "__main__":
    csv_factory = CsvImportFactory()
    # excel_factory = ExcelImporterFactory()

    column_names = ["Retailer", "Retailer ID", "Invoice date", "Region", "State", "City", "Product", "Price per unit", "Unit sold", "Total sales", "Operating Profit", "Operating Margin", "Sales Method"]

    csv_data = import_data(csv_factory, 'C:/Users/97150/OneDrive/Desktop/APDP/Data_new.csv', column_names)

    sort_order = ['Northeast', 'South', 'West', 'Midwest', 'Southeast']
    analyzer = SalesAnalyzer(TotalSalesByRegion(sort_order))
    print("Total Sales By Region:")
    print(analyzer.analyze(csv_data))

    analyzer.set_strategy(BestSellingProduct())
    print("\nBest Selling Product:")
    print(analyzer.analyze(csv_data))

    analyzer.set_strategy(TotalSales('W'))  # Weekly
    print("\nTotal Sales Per Week:")
    print(analyzer.analyze(csv_data))

    analyzer.set_strategy(TotalSales('M'))  # Monthly
    print("\nTotal Sales Per Month:")
    print(analyzer.analyze(csv_data))

    analyzer.set_strategy(TotalSales('Y'))  # Annually
    print("\nTotal Sales Per Year:")
    print(analyzer.analyze(csv_data))

    analyzer.set_strategy(SalesMethodEachMonth())
    print("\nSales Method Each Month:")
    print(analyzer.analyze(csv_data))