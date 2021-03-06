class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.SALE_PRICE_MULTIPLIER
      
    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_PRICE_MULTIPLIER * self.miles)


class Car(Vehicle):
    SALE_PRICE_MULTIPLIER = 1.2
    PURCHASE_PRICE_MULTIPLIER = 0.004
    LEASE_PRICE_MULTIPLIER = 1.2
    INTEREST_PRICE_MULTIPLIER = 1.07
    
class Motorcycle(Vehicle):
    SALE_PRICE_MULTIPLIER = 1.1
    PURCHASE_PRICE_MULTIPLIER = 0.009
    LEASE_PRICE_MULTIPLIER = 1
    INTEREST_PRICE_MULTIPLIER = 1.03

class Truck(Vehicle):
    SALE_PRICE_MULTIPLIER = 1.6
    PURCHASE_PRICE_MULTIPLIER = 0.02
    LEASE_PRICE_MULTIPLIER = 1.7
    INTEREST_PRICE_MULTIPLIER = 1.11