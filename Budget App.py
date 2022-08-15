class Category:

  someList = []
  
  #default constructor
  def __init__(self, ledger):
    self.ledger = someList

  def deposit(self, amount, description):
    self.amount = amount
    self.description = description

  def withdraw(self, amount, description):
    self.amount = amount
    self.description = description

  def get_balance(self):
    # balance -> deposit-withdraw
    print('asf')

  def transfer(self, amount, anotherBudgetCategory):
    self.amount = amount
    self.anotherBudgetCategory = anotherBudgetCategory

  def check_funds(self, amount):
    self.amount = amount

    
def create_spend_chart(categories):
  # categories -> [food, clothing, auto]
  print(categories)


# create object of the class
obj = Category()

# calling the instance method using the object obj
print(obj.test())
