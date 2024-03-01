#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,total=0,items=None):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    
  @property
  def discount(self):
    return self._discount
  @discount.setter
  def discount(self,discount):
    self._discount = discount
    
  @property
  def total(self):
    return self._total 
  @total.setter
  def total(self,total):
    self._total = total
    
  @property
  def items(self):
    return self._items
  @items.setter
  def items(self,items):
    self._items = items
    
  def add_item(self,title,price, quantity=1):
    self._total += (price * quantity)
    for i in range(quantity):
      self._items.append(title)
    self.last_transaction = price * quantity
    return self._items,self.last_transaction
  
  def apply_discount(self):
    if (self._discount !=0):
      discounted_total = self._total - (self._total * (self._discount / 100))
      self._total = int(discounted_total) 
      print(f'After the discount, the total comes to ${self._total}.')
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
     if self.last_transaction != 0:
            self._total -= self.last_transaction
            self.last_transaction = 0
            self._items.pop()
    
    
      
    
