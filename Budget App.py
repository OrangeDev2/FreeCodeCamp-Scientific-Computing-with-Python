class Category:

  ledger = []
  
  #default constructor
  #def __init__(self):
  #  self.ledger = ledger

  def deposit(self, amount, description):
    self.amount = amount
    self.description = description

    print('amount is...', self.amount)
    print('desicrioptn is...', description)

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
  print('test', categories)


# create object of the class
obj = Category()

# calling the instance method using the object obj
print(obj.deposit(58198, 'something'))
