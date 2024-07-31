import pytest
import pandas as pd
from process import CsvImportFactory, ExcelImporterFactory, import_data

@pytest.fixture
def sample_csv_file(tmp_path):
    data = """Retailer,Retailer ID,Invoice date,Region,State,City,Product,Price per unit,Unit sold,Total sales,Operating Profit,Operating Margin,Sales Method
Retailer1,001,2023-01-01,North,State1,City1,Product1,10,5,50,5,10%,Method1"""
    file_path = tmp_path / "sample.csv"
    file_path.write_text(data)
    return str(file_path)

def test_csv_import(sample_csv_file):
    factory = CsvImportFactory()
    data = import_data(factory, sample_csv_file)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (1, 13)
    assert data['Retailer'].iloc[0] == 'Retailer1'

def test_excel_import(tmp_path):
    data = {
        "Retailer": ["Retailer1"],
        "Retailer ID": [1],
        "Invoice date": ["2023-01-01"],
        "Region": ["North"],
        "State": ["State1"],
        "City": ["City1"],
        "Product": ["Product1"],
        "Price per unit": [10],
        "Unit sold": [5],
        "Total sales": [50],
        "Operating Profit": [5],
        "Operating Margin": ["10%"],
        "Sales Method": ["Method1"]
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "sample.xlsx"
    df.to_excel(file_path, index=False)

    factory = ExcelImporterFactory()
    imported_data = import_data(factory, str(file_path))
    assert isinstance(imported_data, pd.DataFrame)
    assert imported_data.shape == (1, 13)
    assert imported_data['Retailer'].iloc[0] == 'Retailer1'
