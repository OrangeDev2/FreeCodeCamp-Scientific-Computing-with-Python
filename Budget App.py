import json

class Category():

  ledger_list = []
  
  def __init__(self, category = str()):
    self.category = category
    title = '*'*int((30-len(category))/2) + category + '*'*int((30-len(category))/2)
    print(title)
    
  def __str__(self):
    return self.category
    
  def deposit(self, amount = int(), description = str()):
    Category.ledger_list.append(f'{{"amount": {amount}, "description": "{description}"}}')
    
    new_description = json.loads(Category.ledger_list[0])['description'][0:23]
    new_amount = str(json.loads(Category.ledger_list[0])['amount'])[0:7]
    space = ' ' * (30 - len(new_description) - len(new_amount))
    
    print(new_description + space + new_amount)
    
    Category.ledger_list.remove(f'{{"amount": {amount}, "description": "{description}"}}')
      

  def withdraw(self, amount = int(), description = str()):
    Category.ledger_list.append(f'{{"amount": {-1 * amount}, "description": "{description}"}}')

    new_description = json.loads(Category.ledger_list[0])['description'][0:23]
    new_amount = str(json.loads(Category.ledger_list[0])['amount'])[0:7]
    space = ' ' * (30 - len(new_description) - len(new_amount))
    
    print(new_description + space + new_amount)
    
    Category.ledger_list.remove(f'{{"amount": {-1 * amount}, "description": "{description}"}}')
    
  def get_balance(self):
    print('')

  def transfer(self, amount = int(), categoryTransfer = str()):
    print('')

  def check_funds(self, amount = int()):
    print('')


def create_spend_chart(categories):
  pass
  #print(categories)
  #for i in Category.ledger_list:
  #  print(json.loads(i)['description'])
