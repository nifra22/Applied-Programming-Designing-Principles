from abc import ABC, abstractmethod
import pandas as pd
from process import ImportFactory, CsvImportFactory, import_data

# Strategy classes
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data):
        pass

class TotalSalesByRegion(AnalysisStrategy):
    def __init__(self, sort_order=None):
        self.sort_order = sort_order

    def analyze(self, data):
        result = data.groupby('Region')['Total sales'].sum().reset_index()
        if self.sort_order:
            sort_map = {region: index for index, region in enumerate(self.sort_order)}
            result['sort_order'] = result['Region'].map(sort_map)
            result = result.sort_values('sort_order').drop(columns='sort_order')
        return result

class BestSellingProduct(AnalysisStrategy):
    def analyze(self, data):
        result = data.groupby('Product')['Unit sold'].sum().reset_index().sort_values(by='Unit sold', ascending=False)
        return result

class TotalSales(AnalysisStrategy):
    def __init__(self, period='M'):
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
        result = data.groupby([data['Invoice date'].dt.to_period('M'), 'Sales Method'])['Total sales'].sum().reset_index()
        return result

# Analyzer context class
class SalesAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AnalysisStrategy):
        self._strategy = strategy

    def analyze(self, data):
        return self._strategy.analyze(data)

def main(file_path, column_names=None):
    # Import the data using the factory
    csv_factory = CsvImportFactory()
    data = import_data(csv_factory, file_path, column_names)

    # Create instances of the strategies
    total_sales_by_region_strategy = TotalSalesByRegion(sort_order=['North', 'South', 'East', 'West'])
    best_selling_product_strategy = BestSellingProduct()
    total_sales_strategy = TotalSales(period='M')
    sales_method_each_month_strategy = SalesMethodEachMonth()

    # Create the SalesAnalyzer with a specific strategy
    analyzer = SalesAnalyzer(total_sales_by_region_strategy)
    print("Total Sales by Region:")
    print(analyzer.analyze(data))

    # Change the strategy to BestSellingProduct
    analyzer.set_strategy(best_selling_product_strategy)
    print("\nBest Selling Product:")
    print(analyzer.analyze(data))

    # Change the strategy to TotalSales with monthly period
    analyzer.set_strategy(total_sales_strategy)
    print("\nTotal Sales per Month:")
    print(analyzer.analyze(data))

    # Change the strategy to SalesMethodEachMonth
    analyzer.set_strategy(sales_method_each_month_strategy)
    print("\nSales Method Each Month:")
    print(analyzer.analyze(data))

if __name__ == "__main__":
    column_names = ["Retailer", "Retailer ID", "Invoice date", "Region", "State", "City", "Product", "Price per unit", "Unit sold", "Total sales", "Operating Profit", "Operating Margin", "Sales Method"]
    main('C:/Users/97150/OneDrive/Desktop/APDP/Data_new.csv', column_names)
