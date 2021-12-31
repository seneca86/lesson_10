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
class Coin:
    def __init__(self, input_metal):
        self.metal = input_metal
storehold = Coin('gold')
storehold.metal = 'tin'
# %%
class Coin:
    def __init__(self, input_metal):
        self.hidden_metal = input_metal
    @property
    def metal(self):
        print('Getter method')
        return self.hidden_metal
    @metal.setter
    def metal(self, input_metal):
        print('Setter method')
        self.hidden_metal = input_metal
storehold = Coin('gold')
print(storehold.metal)
storehold.metal = 'silver'
print(storehold.metal)
# %%
import math
class sphere():
    def __init__(self, radius):
        self.radius = radius
    @property
    def volume(self):
        return (4/3)*math.pi*self.radius**3
ball = sphere(radius=1)
ball.radius
ball.volume
# %%
ball.radius = 2
ball.volume
# %%
class Furniture:
    material = 'wood'
chair = Furniture()
Furniture.material == chair.material
# %%
chair.material = 'iron'
Furniture.material
# %%
Furniture.material = 'plastic'
chair.material
# %%
table = Furniture()
table.material
# %%
class Mom():
    children = 0
    def __init__(self):
        Mom.children += 1 # This is the class attribute
        #self.children += 1 # If we did this, it would be an object attribute
    def state(self):
        print('I belong to the family')
    @classmethod
    def kids(cls):
        print(f'We are {cls.children} kids') # Mom.children would also work
kid1 = Mom()
Mom.kids()
kid2 = Mom()
Mom.kids()
kid3 = Mom()
Mom.kids()
# %%
class Warning():
    @staticmethod
    def dog():
        print('Beware the dog')
Warning.dog()
# %%
class Player():
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def player_name(self):
        return self.name
    def player_position(self):
        return f'Plays as {self.position}'
class Soccer(Player):
    def player_position(self):
        return f'Plays soccer as {self.position}'
class Basketball(Player):
    def player_position(self):
        return f'Plays basketball as {self.position}'

federer = Player(name='Roger Federer', position='N/A')
ronaldo = Soccer(name='Cristiano Ronaldo', position='forward')
lebron = Basketball(name='LeBron James', position='shooting guard')

print(f'{federer.name} - {federer.player_position()}')
print(f'{ronaldo.name} - {ronaldo.player_position()}')
print(f'{lebron.name} - {lebron.player_position()}')
# %%
class Fans():
    def player_name(self):
        return 'anonymous'
    def player_position(self):
        return 'located in the stands of the arena'
fans = Fans()
print(f'{fans.player_name()} - {fans.player_position()}')
print(f'{lebron.player_name()} - {lebron.player_position()}')
# %%
