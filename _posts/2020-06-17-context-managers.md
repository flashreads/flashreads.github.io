---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [python]
date: '2020-06-17T22:56:26+02:00'
id: 011-context-managers.md
image: assets/images/python/code.svg
keywords: python, python3, python-with, with statement
layout: post
meta-description: Short introduction to context managers in Python
tags: [python, python3, python-with, with statement]
template: post
title: Python context managers
title_new: context-managers.md
---



Have you ever heard about Context managers in Python and you weren't sure what they are? The name may be strange but I am sure you have already used one. Let's see one example for reading the file in Python:



```python

    f = open(filename)

    try:

        yield f

    finally:

        f.close()



```

In this implementation, the file wouldn't be closed if the exception happened. Let's another example that uses the `with` statement.



```python

with open('file.txt') as f:

    content = f.read()

```



This code example is clean, easier to read and you are sure that the `file` method `close` will be called after execution leaves the `with `context. So, that is the job of the Context Manager. Context managers (objects that perform context management) allows you to release or allocate the resources when you want and can help you to avoid resource leaks. The [contextlib](https://docs.python.org/3/library/contextlib.html) module provides utilities for most of the tasks where the `with` is used. To learn how to create your own context managers check out [](Link to the next blog).




