class Company:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Comapany: {self.name}"

class Finance(Company):
    def __init__(self, name, budget):
        super().__init__(name)
        self.budget = budget

    def get_details(self):
        return f"{super().get_details()} Finanace section with budget:{self.budget}"

class Sales(Company):
    def __init__(self, name, total_sales):
        super().__init__(name)
        self.total_sales = total_sales

    def get_details(self):
        return f"{super().get_details()} Sales section with total sales: {self.total_sales}"

def print_details(section):
    print(section.get_details())

if __name__ == "__main__":
    finance_section = Finance("Phonyt Solution", 150000)
    sales_section = Sales("Phonyt Solutions", 50000)

    print_details(finance_section)
    print_details(sales_section)