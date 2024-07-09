from abc import ABC, abstractmethod
import pandas as pd

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
