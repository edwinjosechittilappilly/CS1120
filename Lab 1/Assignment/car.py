class Car:
    def __init__(self, brand, color, maxspeed, accelaration_rate):
        self.brand = brand
        self.color = color
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.accelaration_rate = accelaration_rate
        self.mile = 0

    def get_brand(self):
        return self.brand

    def get_color(self):
        return self.color

    def get_maxspeed(self):
        return self.maxspeed
    
    def get_currentspeed(self):
        return self.currentspeed
    
    def get_accelaration_rate(self):
        return self.accelaration_rate

    def get_mile(self):
        return self.mile


    def set_brand(self, newbrand):
        self.brand = newbrand

    def set_color(self, newcolor):
        self.color = newcolor

    def set_maxspeed(self, newmaxspeed):
        self.maxspeed = newmaxspeed

    def set_currentspeed(self, newcurrentspeed):
        self.currentspeed = newcurrentspeed
    
    def set_accelaration_rate(self, newrate):
        self.accelaration_rate = newrate
    
    def increase_speed(self):
        self.currentspeed = self.currentspeed + self.accelaration_rate

    def increase_mile(self):
        self.mile = self.mile + self.currentspeed
        