---
author: William Dessert
author_email: 47290046+SaucyGames05@users.noreply.github.com
categories: [python]
date: '2020-10-23T15:41:42-07:00'
id: 015-using-random.md
image: assets/images/python/python1.svg
keywords: python, random, beginner
layout: post
meta-description: Using random to randomize something
tags: [python, random, beginner]
template: post
title: How to make a virtual die roller
---



## What is random?



Random is a python package that comes pre-installed when you install Python. It is a way to generate pseudo-random numbers that can be used in many different ways.



## Making our virtual die



First off, we need to import the package like so:



```python

import random

```



Since a normal die has six sides we want to pick a random number 1-6. We can do that like so:



```python

import random



result = random.randint(1, 6)

```



`random.randint(1,6)` chooses 1-6 at random and stores it in our variable I called `result`.



Now we want to print our result to the console. We can do that by typing this:



```python

import random



result = random.randint(1, 6)



print(f'You rolled a {result}!')



input("Press enter to continue...")

```



I now have added a way to print our result and I put the variable in an f-string so that I can add my value inside the string. I also added an input to prevent the console from closing immediately after running and a way to exit the program.



Thats it! You now have a virtual die!