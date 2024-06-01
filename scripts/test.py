import matplotlib.pyplot as plt

class Expense():
    total_expanse = 0
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        Expense.total_expanse += amount

    
    def get_name(self):
        return self.name
    
    def get_amount(self):
        return self.amount
    
    def add_amount(self, amount):
        self.amount += amount
        Expense.total_expanse += amount

    def get_total_expenses(self):
        return Expense.total_expanse
    
class Expenses(list):
    def __init__(self):
        super().__init__()

        
        self.append(Expense('eating', 0))
        self.append(Expense('grocery', 0)) 
        self.append(Expense('study', 0))
        self.append(Expense('travel', 0) )
        self.append(Expense('shoping', 0))
        

    def add_expense(self, name, amount):
        self.append(Expense(name=name, amount=amount))


def create_pie_chart(income, expenses):
    total_expenses = expenses[0].get_total_expenses()
    remaining_income = income - total_expenses

    labels = [f"{i.get_name()}" for i in expenses] + ["Remaining Income"]

    sizes = [i.get_amount() for i in expenses] + [remaining_income]

    if remaining_income < 0:
        print("Warning: Expenses exceed income!")
        labels[-1] = "Debt"

    colors = plt.cm.Paired(range(len(sizes)))

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.axis('equal')

    plt.title("Income and Expenses Distribution")

    file_path = "./assets/graph.png"

    print("executed")
    plt.savefig(file_path)
    print("picture saved")
