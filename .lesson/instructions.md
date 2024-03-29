# Classes

## Introduction

We have mentioned that everything in Python is an object, but Python typically hides the nuts and bolts when using the pre-defined types; in this lesson we will learn to make our own objects.

An _object_ is a data structure that contains both data (_attributes_) and functions (_methods_). Think of object as _nouns_, attributes as _adjectives_, and methods as _verbs_.

## Simple objects

To create a new object, we first must define a _class_. If an object is a plastic box, a class is the mold that makes that box. We may want to define a class called `Car` as the mold (we will use the _CamelCaps_ convention for classes).

We will create two "cars", which will be _instances_ of the `Car` class.

```python
class Car:
    pass
model3 = Car()
diablo = Car()
model3
diablo
```

We can assign, and then access, a few attributes to our first object, even if we have not defined them in the class.

```python
model3.maxspeed = 225
model3.passengers = 5
model3.manufacturer = 'Tesla'
```

```python
model3.maxspeed
model3.passengers
model3.manufacturer
```

If we want to assign object attributes at creation time, we need the special Python object initialization method __init__():

```python
class Car:
    def __init__(self):
        pass
```

The `__init__` and the `self` are not intuitive. `__init__` is the special method that initializes an individual object from its class definition. `self` is the name given by convention to the argument that refers to the individual object itself (you could use another name, but `self` is commonplace).

Now let's add a parameter to the initialization method.

```python
class Car:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('This is a car')
impreza = Car('Subaru Impreza')
```

This is the logic behind the last line:
- look up the definition of the `Car` class
- create a new _instance_ of the class, i.e. a new object
- call the `__init__()` method, passing the newly created object as `self` and the other argument as `name`
- store the value of `name`in the object
- return the object
- attach the variable (think of it as a tag) to the object

```python
print(f'I want to buy a {impreza.name}')
```

Although `__init__` is not necessary, it helps us do anything that is needed to distinguish this object from other created from the same class.

Finally, if `self` sounds confusing, think that we could explicitly pass the object (`impreza`) to the class (`Car`) so that the object is passed on to the method `introduce` as the `self` parameter.

```python
impreza.introduce()
Car.introduce(impreza) # equivalent, but less often used
```

## Inheritance

Often, we will find that we want to modify an existing class without overcomplicating its definition or breaking what already works. One solution to this is _inheritance_, which creates a new class from an existing class, with some changes. The original class is called a _parent_, _superclass_, or _base class_, and the new one is called a _child_, _subclass_, or _derived class_.

Let's create a subclass of our `Car()` class to illustrate this.

```python
class SportsCar(Car):
    pass
issubclass(SportsCar, Car)
viper = SportsCar('Dodge Viper')
viper.name
viper.introduce()
```

As we see, `SportsCar` inherites the `name` attribute from `car`; otherwise the last two lines would not have worked. Experience recommends, though, not to overuse inheritance despite these advantages.

### Override a method

Let's add a method to `SportsCar` to make it more useful. We can also override an existing method, such as `__init__()` in the example.

```python
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
```

What if we want to retrive the original method? In the case, we may want to use the `__init__()` from the parent class instead of the `__init__()` from the child. We achieve this with `super()`.

```python
class SportsCar(Car):
    def __init__(self, name, top_speed, ad):
        super().__init__(name)
        self.topspeed = top_speed
        self.ad = ad
    def full_name(self):
        print(f'{self.name} - {self.ad}')
porsche = SportsCar(name='Porsche GT3', top_speed=230, ad=None)
porsche.name
```

Note that `super()` takes care of passing the `self` argument to the superclass.

The benefit seems small now, because we could just have used `self.name = name` but, if the definition of `Car` changes in the future, using `super()` ensures that the inherited attributes and methods reflect the change.

(You may think of `super()` as a child requesting help from his parent for a specific task).

### Multiple inheritance

Objects can inherit from multiple parent classes, using _method resolution order_ to resolve conflicts when more than one of the parents have a method or attribute with the same name. The list/tuple of classes that would be visited is obtained with `mro()`/`__mro__`, and the first one has priority.

```python
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
```

If we look for a method of `Boy`, Python will look at the object itself, then at `Boy`, then at `Mom`, then at `Dad`, then at `Grandpa`. Note the conflict resolution with methods that have the same name.

```python
boy = Boy()
girl = Girl()
boy.speaks()
girl.speaks()
```

A note on nomenclature: when a parent class does not share any method with the other parent classes, it is sometimes called a _mixin class_.

## Attribute access

### Properties for access

Sometimes we want objects to ban modification of certain attributes in order to prevent accidental changes.

```python
class Coin:
    def __init__(self, input_metal):
        self.metal = input_metal
storehold = Coin('gold')
storehold.metal = 'tin'
```

On a more advanced note: this can be solved defining _setter_ and _getter_ methods, which is a bit cumbersome and will not be covered here. Python offers a shortcut which is to use two decorators, one for a method that gets the name and another one for the method that retreives the name.

```python
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
```

### Properties for computed values

Let's see how to apply the properties for access in the case of a class with computed values.

```python
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
```

Interestingly, if we change the radius the volume updates automatically.

```python
ball.radius = 2
ball.volume
```

If we tried to set the value of volume from the outside, the operation would fail, because volume is a property.

```python
ball.volume = 10 # this will not work
```

### Class and object attributes

Attributes can be assigned to classes and be inherited by their child objects.

```python
class Furniture:
    material = 'wood'
chair = Furniture()
Furniture.material == chair.material
```

As expected, changing the value of the attribute in the child object does not affect the class attribute. 
```python
chair.material == 'iron'
Furniture.material
```

Nor changing the class attribute after generating the child will change existing child objects.

```python
Furniture.material = 'plastic'
chair.material
```

But it will affect new ones.

```python
table = Furniture()
table.material
```

## Method types

Some methods are part of the class, some methods are part of the objects that are creates from that class, and some are neither.

- __Instance methods__: where there is no preceding decorator; the first argument must be `self`
- __Class methods__: if there is a preceding `@classmethod` decorator; the first argument should be `cls`, referring to the class itself
- __Static methods__: if there is a preceding `@staticmethod`; the first argument is not an object nor a class

### Instance methods

These are the ones we have covered so far.

### Class methods

They affect the class as a whole, i.e. affect all the objects within the class. 

```python
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
```

### Static methods

A static method does not affect the class or its objects, and lays there just for convenience.

```python
class Warning():
    @staticmethod
    def dog():
        print('Beware the dog')
Warning.dog()
```

We can use a static method without needing to create an object.

## Duck typing

Duck typing refers to Python's implementation of _polymorphism_, which means applying the same operation to different objects. "Duck" comes from the saying "if it walks like a duck and quacks like a duck, it is a duck", meaning that Python will infer the type of the object based on its properties.

Let's define two child classes while keeping the `__init__` method on the parent.

```python
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
```

Note how the different versions of `player_position` provide different
behaviors: this is _polymorphism_. 

If we define a class completely unrelated to the ones before, but that has methods of the same name, Python will know which method to apply to which object.

```python
class Fans():
    def player_name(self):
        return 'anonymous'
    def player_position(self):
        return 'located in the stands of the arena'
fans = Fans()
print(f'{fans.player_name()} - {fans.player_position()}')
print(f'{lebron.player_name()} - {lebron.player_position()}')
```

## Magic Methods

_Magic_ or _Special_ methods are the means by which Python knows that, e.g., `3 + 3` is an arithmetic operation but `'a' + 'b'` is a string concatenation. Magic methods begin and end with a _dunder_ (double underscore).

Let's define a class with an _equal_ method that compares two words and that is not case-sensitive.

```python
class Word():
    def __init__(self, content):
        self.content = content
    def equals(self, other_word):
        return self.content.lower() == other_word.content.lower()
w1 = Word('cloud')
w2 = Word('CLOUD')
w3 = Word('storm')
w1.equals(w2)
w1.equals(w3)
```

This works as expected. But instead of writing `equals`, we may want to use the `==` operator. In order to do that, we need to use the _magic_ method `__eq__`.

```python
class Word():
    def __init__(self, content):
        self.content = content
    def __eq__(self, other_word):
        return self.content.lower() == other_word.content.lower()
w1 = Word('cloud')
w2 = Word('CLOUD')
w3 = Word('storm')
print(w1 == w2)
print(w1 == w3)
```

The most useful magic methods are:

| Method | Description |
|--------|-------------|
| __eq__( self, other ) | self == other |
| __ne__( self, other ) | self != other |
| __lt__( self, other ) | self < other |
| __gt__( self, other ) | self > other |
| __le__( self, other ) | self <= other |
| __ge__( self, other ) | self >= other |
| __add__( self, other ) | self + other |
| __sub__( self, other ) | self – other |
| __mul__( self, other ) | self * other |
| __floordiv__( self, other ) | self // other |
| __truediv__( self, other ) | self / other |
| __mod__( self, other ) | self % other |
| __pow__( self, other ) | self ** other |
| __str__( self ) | str( self ) |
| __repr__( self ) | repr( self ) |
| __len__( self ) | len( self ) |

`__str__` is the magic method you are most likely to use.