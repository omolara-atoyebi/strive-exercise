class Vehicle:
    def __init__(self, brand_name, price, year, colour):
        self.brand_name = brand_name
        self.price = price
        self.year = year
        self.colour = colour
    def selling_price(self):
        return self.price
vehincle_model = Vehicle('toyota', 100 , 2020, 'black' )
print(vehincle_model.selling_price())
