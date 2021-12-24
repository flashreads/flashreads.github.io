---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [python]
date: '2020-06-01T23:22:13+02:00'
id: 007-string-isspace.md
image: assets/images/python/empty.svg
keywords: python, strings
layout: post
meta-description: Check if the string is empty or contains tabs, carriage return,
  newline with one built-in string method
tags: [python, strings]
template: post
title: How to check for empty space, tab or newline in Python
---



The built-in string method `isspace()` checks if there are only whitespace characters in the string, otherwise it will return False.

The best use case of this method is to check if the string contains characters as:



* '\n' - new line



```python

mystring = '\n'

mystring.isspace()

>>>True

```



* ' ' - whitespace



```python

mystring = ' '

mystring.isspace()

>>>True

```



* '\t' - tab



```python

mystring = '\t'

mystring.isspace()

>>>True

```



* '\r' - carriage return



```python

mystring = '\r'

mystring.isspace()

>>>True

```



* '\f' - form feed



```python

mystring = '\f'

mystring.isspace()

>>>True

```



Or combination:



```python

mystring = ' \t'

anotherstring = '\n\t'

mystring.isspace()

anotherstring.isspace()

>>>True

>>>True

```



>Note that `isspace()` will not return True for '', so always check with `not mystring or mystring.isspace()`.