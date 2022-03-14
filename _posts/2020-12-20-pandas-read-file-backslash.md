---
author: Matteo Buldrini
author_email: 60760187+MatteoBuldrini@users.noreply.github.com
categories: [python]
date: '2020-12-20T14:30:05+02:00'
id: 027-pandas-unicodeescape-error.md
image: assets/images/python/python3.svg
keywords: python, pandas
layout: post
meta-description: How to read in Pandas files that give you unicodeescape error.
tags: [python, pandas]
template: post
title: Pandas read files
title_new: pandas-read-file-backslash.md
---



Sometimes when reading a file in Pandas you may incur in the following error after declaring the path name:



```python

  SyntaxError: (unicode error) ‘unicodeescape’ codec can’t decode bytes in position 2-3:

  truncated \UXXXXXXXX escape.

```



This happens because path names tend to have backslashes in them (e.g. 'C:\Documents\File.csv'). In Python, backslash is used to signify special characters, but when we use it in a path name we want to refer to actual backslashes, not to special characters.



To solve this issue, you need to add an <b>r</b> before the path name, so that Python can interpret backslashes as strings.



Example:



```python

df = pd.read_csv(r'C:\Documents\File.csv')

```
