class Company:
    def __init__(self, name):
        self.__name = name
        self.__finance = self.__Finance()
        self.__sales = self.__Sales()
    def get_finance(self):
        return self.__finance
    def get_sales(self):
        return self.__sales
    def __str__(self):
        return f"Company: {self.__name}"

    class __Finance:
        def __init__(self):
            self.__budget = 0
        def set_budget(self, amount):
            if amount < 0:
                return ValueError("Budget cannot be accepted as it is in negative")
            self.__budget = amount

        def get_budget(self):
            return self.__budget
        def __str__(self):
            return f"Finance section with budget: {self.__budget}"

    class __Sales:
        def __init__(self):
            self.__sales_data = []
        def record_sales(self, amount):
            if amount < 0:
                return ValueError("Sales cannot be accepted as it is negative value")
            self.__sales_data.append(amount)
        def total_sales(self):
            return sum(self.__sales_data)
        def __str__(self):
            return f"Sales section with total sales: {self.total_sales()}"

if __name__ == "__main__":
    my_company = Company("Phonyt")
    print(my_company)

    finance_section = my_company.get_finance()
    finance_section.set_budget(100000)
    print(finance_section)
    print(f"Finance budget: {finance_section.get_budget()}")

    sales_sectiom = my_company.get_sales()
    sales_sectiom.record_sales(15000)
    sales_sectiom.record_sales(20000)
    print(sales_sectiom)
    print(f"Total Sales: {sales_sectiom.total_sales()}")
