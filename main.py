# %%
class Car:
    pass
model3 = Car()
diablo = Car()
model3
diablo
# %%
model3.maxspeed = 225
model3.passengers = 5
model3.manufacturer = 'Tesla'
# %%
model3.maxspeed
model3.passengers
model3.manufacturer
# %%
class Car:
    def __init__(self):
        pass

# %%
class Car:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('This is a car')
# %%
impreza = Car('Subaru Impreza')
impreza.introduce()
Car.introduce(impreza) # equivalent, but less often used
# %%
print(f'I want to buy a {impreza.name}')
# %%
class SportsCar(Car):
    pass
issubclass(SportsCar, Car)
# %%
viper = SportsCar('Dodge Viper')
viper.name
viper.introduce()
# %%
class SportsCar(Car):
    def __init__(self, name, top_speed, ad):
        self.name = f'{name} Gran Turismo'
        self.topspeed = top_speed
        self.ad = ad
    def full_name(self):
        print(f'{self.name} - {self.ad}')
mustang = SportsCar(name='Ford Mustang', top_speed='250', ad='The only slow part is the fuel gauge')
mustang.introduce()
mustang.topspeed
mustang.name
mustang.full_name()
# %%
mustang.name
# %%
class SportsCar(Car):
    def __init__(self, name, top_speed, ad):
        super().__init__(name)
        self.topspeed = top_speed
        self.ad = ad
    def full_name(self):
        print(f'{self.name} - {self.ad}')

porsche = SportsCar(name='Porsche GT3', top_speed=230, ad=None)
porsche.name
# %%
class Grandpa:
    def speaks(self):
        return 'I am a grandpa'
class Dad(Grandpa):
    def speaks(self):
        return 'I am a dad'
class Mom(Grandpa):
    def speaks(self):
        return 'I am a mom'
class Boy(Mom, Dad):
    pass
class Girl(Dad, Mom):
    pass
# %%
boy = Boy()
girl = Girl()
boy.speaks()
girl.speaks()
# %%
