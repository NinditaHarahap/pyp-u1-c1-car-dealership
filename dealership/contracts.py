class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer
        
    def total_value(self):
        if self.customer.is_employee() == True:
          return self.original_price() * 0.9
        else:
          return self.original_price()
        
    def monthly_value(self):
        return self.total_value() / self.monthly_count

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        self.monthly_count = monthly_payments
    
    def original_price(self):
        return self.vehicle.sale_price() + (self.vehicle.INTEREST_PRICE_MULTIPLIER * self.monthly_payments * self.vehicle.sale_price() / 100) 
                
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        self.monthly_count = length_in_months
        
    def lease_multiplier(self):
        return self.vehicle.sale_price() * (self.vehicle.LEASE_PRICE_MULTIPLIER / self.length_in_months)
      
    def original_price(self):
        return self.vehicle.sale_price() + self.lease_multiplier()