class Company:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def __str__(self):
        return f"Company: {self.name}"

class Finance(Company):
    def __init__(self, name, budget = 0):
        super().__init__(name)
        self.budget = budget

    def set_budget(self, amount):
        if amount < 0:
            return ValueError("Budget cannot be negative value")
        self.budget = amount

    def get_budget(self):
        return self.budget

    def __str__(self):
        return f"{super(). __str__()} Finance section with budget: {self.budget}"
class Sales(Company):
    def __init__(self, name, sales_data = None):
        super().__init__(name)
        if sales_data is None:
            sales_data = []
        self.sales_data = sales_data

    def record_sales(self, amount):
        if amount < 0:
            return ValueError("Sales amount cannot be negative value")
        self.sales_data.append(amount)

    def total_sales(self):
        return sum(self.sales_data)

        def __str__(self):
            return f"{super().__str__()} | Sales Department with total sales: {self.total_sales()}"

if __name__ == "__main__":
    finance_section = Finance("Phonyt", 100000)
    print(finance_section )
    finance_section.set_budget(150000)
    print(f"Updated Finance Budget: {finance_section.get_budget()}")

    sales_section = Sales("Phonyt")
    sales_section.record_sales(15000)
    sales_section.record_sales(25000)
    print(sales_section)
    print(f"Total Sales: {sales_section.total_sales()}")

