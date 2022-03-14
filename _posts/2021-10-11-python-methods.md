---
author: null
author_email: ephraimleo16@gmail.com
categories: [python]
date: '2021-10-11T18:38:42-07:00'
id: 037-python-Methods
image: assets/images/python/python.svg
keywords: python
layout: post
meta-description: Creating Object Oriented Methods
tags: [python, random]
template: post
title: Creating Object Oriented methods
title_new: python-methods.md
---



# Methods

Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are a key concept of the OOP paradigm. They are essential to dividing responsibilities in programming, especially in large applications.



You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.



Let's go through an example of creating a Circle class:





```python

class Circle:

    pi = 3.14



    # Circle gets instantiated with a radius (default is 1)

    def __init__(self, radius=1):

        self.radius = radius 

        self.area = radius * radius * Circle.pi



    # Method for resetting Radius

    def setRadius(self, new_radius):

        self.radius = new_radius

        self.area = new_radius * new_radius * self.pi



    # Method for getting Circumference

    def getCircumference(self):

        return self.radius * self.pi * 2





c = Circle()



print('Radius is: ',c.radius)

print('Area is: ',c.area)

print('Circumference is: ',c.getCircumference())

```





In the _init_ method above, in order to calculate the area attribute, we had to call Circle.pi. This is because the object does not yet have its own .pi attribute, so we call the Class Object Attribute pi instead.

In the setRadius method, however, we'll be working with an existing Circle object that does have its own pi attribute. Here we can use either Circle.pi or self.pi.



Now let's change the radius and see how that affects our Circle object:



```python

c.setRadius(2)



print('Radius is: ',c.radius)

print('Area is: ',c.area)

print('Circumference is: ',c.getCircumference())

```



Great! Notice how we used self. notation to reference attributes of the class within the method calls. Review how the code above works and try creating your own method.