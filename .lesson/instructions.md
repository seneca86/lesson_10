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

## Inheritance

Often, we will find that we want to modify an existing class without overcomplicating its definition or breaking what already works. One solution to this is _inheritance_, which creates a new class from an existing class, with some changes. The original class is called a _parent_, _superclass_, or _base class_, and the new one is called a _child_, _subclass_, or _derived class_.

Let's create a subclass of our `Car()` class to illustrate this.

```python
class SportsCar(Car):
    pass
issubclass(SportsCar, Car)
viper = SportsCar('Dodge Viper')
viper.name
```

As we see, `SportsCar` inherites the `name` attribute from `car`; otherwise the last two lines would not have worked. Experience recommends, though, not to overuse inheritance despite these advantages.

### Override a method

Let's add a method to `SportsCar` to make it more useful. We can also override an existing method, such as `__init__()` in the example.



