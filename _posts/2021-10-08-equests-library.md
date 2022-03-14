---
author: Javier Gonzalez
author_email: gonzalezbodasjavier@yahoo.es
categories: [python]
date: '2021-10-08T16:30:00-07:00'
id: 030requests-library.md
image: assets/images/python/req.svg
keywords: python
layout: post
meta-description: null
tags: [python]
template: post
title: Requests library in Python
title_new: equests-library.md
---



## Python Requests Library



Sometimes we need with a script written in Python accessing to an API or download the content of a web page.



For that we can use the [Requests Library](https://docs.python-requests.org/en/latest)



First we need to install the library:



```console

pip install requests

```



Code Example : 



```python



import requests



# The requests module provides us different methods (get, post, update, delete)

r = requests.get('http://www.google.com')



# In the request method also it is possible to specify the headers, the cookies and the data sent

headers = { 'accept' : '*/*' }

payload = { 'title' : 'Download web page with python' }

cookies = dict(example_cookie='value')



r = requests.post('https://reqres.in/api/posts', data=payload, headers=headers, cookies=cookies)



# With the object returned 

# We could check the status code of the response

r.status_code



# We could obtain the content of the page as a string

r.text



# Or if the url is an API, we could obtain the response in json format

r.json()





```
