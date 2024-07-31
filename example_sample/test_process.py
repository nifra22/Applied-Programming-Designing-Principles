import pytest
import pandas as pd
from inject import TotalSalesByRegion, BestSellingProduct, TotalSales, SalesMethodEachMonth, SalesAnalyzer

@pytest.fixture
def sample_data():
    data = {
        "Region": ["North", "South", "East", "West"],
        "Total sales": [100, 200, 150, 50],
        "Unit sold": [10, 20, 15, 5],
        "Invoice date": pd.to_datetime(["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"]),
        "Product": ["Product1", "Product2", "Product3", "Product4"],
        "Sales Method": ["Online", "Offline", "Online", "Offline"]
    }
    return pd.DataFrame(data)

def test_total_sales_by_region(sample_data):
    strategy = TotalSalesByRegion()
    analyzer = SalesAnalyzer(strategy)
    result = analyzer.analyze(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Region' in result.columns
    assert 'Total sales' in result.columns
    assert result['Total sales'].sum() == 500

def test_best_selling_product(sample_data):
    strategy = BestSellingProduct()
    analyzer = SalesAnalyzer(strategy)
    result = analyzer.analyze(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Product' in result.columns
    assert 'Unit sold' in result.columns
    assert result['Unit sold'].max() == 20

def test_total_sales(sample_data):
    strategy = TotalSales(period='M')
    analyzer = SalesAnalyzer(strategy)
    result = analyzer.analyze(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Total sales' in result.columns
    assert result['Total sales'].sum() == 500

def test_sales_method_each_month(sample_data):
    strategy = SalesMethodEachMonth()
    analyzer = SalesAnalyzer(strategy)
    result = analyzer.analyze(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Sales Method' in result.columns
    assert 'Total sales' in result.columns
    assert result['Total sales'].sum() == 500
