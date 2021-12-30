# %%
print('Hi')
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
# %%
impreza = Car('Subaru Impreza')
# %%
print(f'I want to buy a {impreza.name}')
# %%
class SportsCar(Car):
    pass
issubclass(SportsCar, Car)
# %%
viper = SportsCar('Dodge Viper')
viper.name
# %%
class SportsCar(Car):
    def __init__(self, name, top_speed):
        self.name = f'{name} Gran Turismo'
        self.topspeed = top_speed
    def full_name(self, ad):
        print(ad)
mustang = SportsCar(name='Ford Mustang', top_speed='250', ad='The only slow part is the fuel gauge')
mustang.topspeed
mustang.name
mustang.full_name
# %%
