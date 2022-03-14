---
author: Rohit Geddam
author_email: 48797475+rohitgeddam@users.noreply.github.com
categories: [databases]
date: '2020-10-27T22:02:14+05:30'
id: 003-install-postgres-on-linux.md
image: assets/images/install.svg
keywords: linux, database, postgres
layout: post
meta-description: See How to install postgres on your linux machine
tags: [linux, database, postgres]
template: post
title: How to install Postgres on Linux (Debian)
title_new: Install-postgres-on-linux.md
---



## How to Install Postgres On Linux (Debian)

***

### **Step-1**

*Install using apt.*

```bash

$ sudo apt update

$ sudo apt install postgresql postgresql-contrib

```



### **Step-2**

*Test your Installation*

```bash

sudo -u posgtres psql

```

*You will see: `postgres=#`*

*To quit type `\q`*



### **Step-3**

*Create Postgres User*

```bash

$ sudo -u postgres createuser --interactive

```

*You will see:*

```bash

Enter name of role to add: test

Shall the new role be a superuser? (y/n) y

```



### **Step-4**

*Create a Database*

```bash

$ sudo -u postgres createdb test

```

*Now create the same linux user as postgres user*

```bash

$ sudo adduser test

```

*Now login to your postgres database*

```bash

$ sudo -u test psql

```



### **Step-5**

*Assign Password to postgres user*

```bash

$ sudo -u postgres psql



postgres=# ALTER USER test with PASSWORD 'your-new-password';

```

*The connection string for the above database will be `postgres://test:your-new-password@localhost:5432/test`*
