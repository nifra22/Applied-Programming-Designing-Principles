from abc import ABC, abstractmethod

class Company(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_details(self):
        pass

class Finance(Company):
    def __init__(self, name, budget):
        super().__init__(name)
        self.budget = budget

    def get_details(self):
        return f"Company: {self.name} Finance section with budget: {self.budget}"

class Sales(Company):
    def __init__(self, name, total_sales):
        super().__init__(name)
        self.total_sales = total_sales

    def get_details(self):
        return f"Company: {self.name} Sales section with total sales: {self.total_sales}"

if __name__ == "__main__":
    finance_section = Finance("Phonyt", 150000)
    sales_section = Sales("Phonyt", 50000)

    print(finance_section.get_details())
    print(sales_section.get_details())