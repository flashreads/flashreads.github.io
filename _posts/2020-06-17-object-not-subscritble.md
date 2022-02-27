---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [python]
date: '2020-06-17T22:56:36+02:00'
id: 012-object-not-subscritble.md
image: assets/images/python/python1.svg
keywords: python, python3, type-error, list, dict
layout: post
meta-description: How to easily resolve the object is not subscriptable error in Python
tags: [python, python3, type-error, list, dict]
template: post
title: TypeError 'NoneType' object is not subscriptable
---



This error is quite self-descriptive: 



```python

Traceback (most recent call last):

  File "users.py", line 25, in <module>

    user = users[0]

TypeError: 'NoneType' object is not subscriptable

```



It means that you are trying to subscript (index) the object that actually is None. In the above example, the `users` list is empty so you can't get the first user from it since None object doesn't define the [`__getitem__`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) method. This simply can be fixed by finding out `Why the list is None`.