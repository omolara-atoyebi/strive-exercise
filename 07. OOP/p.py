from turtle import clear
from v import Vehicle
class Car(Vehicle):
    def __init__(self,brand_name, price, year, colour,country):
        super().__init__(brand_name, price, year, colour)
        self.country = country
    def country_of_production(self):
        print('The country of production is:' , self.country)
        return 
car_model = Car('Volvo', 20000, 2020, 'red', 'japan')

#car_model.country_of_production()
