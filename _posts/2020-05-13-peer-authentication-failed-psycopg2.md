---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [python]
date: '2020-05-13T20:57:40+02:00'
id: 002-peer-authentication-failed-psycopg2.md
image: assets/images/python/auth.svg
keywords: psycopg2, postgresql, python, database
layout: post
meta-description: Simple steps to avoid psycopg2 Peer authentication
tags: [psycopg2, postgresql, python, database]
template: post
title: Psycopg Peer authentication failed for user "postgres"
title_new: peer-authentication-failed-psycopg2.md
---



# psycopg2.OperationalError: FATAL: Peer authentication failed for user "postgres"



The [Psycopg](https://www.psycopg.org/docs/usage.html) is one of the most popular and widely used python database adapters for the [PostgreSQL database](https://www.postgresql.org/).

The basic example shows how easy it is to connect to the existing database with psycopg. But, it doesn't provide all of the 

required arguments to the [connect](https://www.psycopg.org/docs/module.html#psycopg2.connect) function that usually leads to the above error. The basic module usage example:



```python

import psycopg2

# Connect to an existing database

conn = psycopg2.connect("dbname=test user=postgres")

```

Since the `psycopg2.OperationalError` error is quite generic to avoid it make sure you are providing the following arguments:



* user - the database user used to authenticate

* password - the password for the database user

* database - the database name

* host - the database host address



The basic example with the required arguments:

```python

conn = psycopg2.connect(dbname='db', user='postgres', host='localhost', password='postgres')

```

>Note: the connection parameters can be added as a connection string or as a set of keyword arguments.
