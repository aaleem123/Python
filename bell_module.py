class HairAccessories:

    def __init__(self, color, price, shape, place, strenght):
        self.color = color
        self.price = price
        self.shape = shape
        self.place = place
        self.strenght = strenght


    def where_from(self):
        return(f"I am imported from {self.place}")
    
    def power(self):
        return(f"My grip is {self.strenght}")
    
    def goodlooking(self):
        print("Accesories are unisex, looks good on everyone")
    
class GenderWise(HairAccessories):
    pass

class HairWigs(HairAccessories):

    def __init__(self, color, price, shape, place, strenght, material):
        self.material = material 
        super().__init__(color, price, shape, place, strenght)

