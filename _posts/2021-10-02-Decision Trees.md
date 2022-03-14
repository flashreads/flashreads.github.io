---
author: Ankur
author_email: sin2ank84@gmail.com
categories: [python]
date: '2021-10-02T15:41:42-07:00'
id: 028-Decision Tree.md
image: assets/images/python/tree.svg
keywords: python, Decision Tree
layout: post
meta-description: What makes decision trees popular
tags: [python, random, machine learning]
template: post
title: Why Decision trees are so popular in Machine Learning algorithms
title_new: Decision Trees.md
---



## What is Decision Trees?



Decision trees-like model more specifically it is probablity tree that enables the user to made decision on the basis on conditions.This condition can be understand as if-then statements so there's if condition then it will choose some vertex else other.The solution choosen after particular condition is called decision. This algorithm can be used for both regression and classification.



In this trees internal nodes represents conditions and the leaf node depicts decision.



## But why they are so popular?



First off, Lets look which module allow you to make decision tree:



```python

From sklearn.tree import DecisionTreeClassifier  

classifier= DecisionTreeClassifier(criterion='entropy', random_state=0) #for classification

classifier= DecisionTreeRegressor(criterion='entropy', random_state=0)  #for regression

```



1.This tree based algorithm can visualized and inclusing its conditions.

https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html

https://scikit-learn.org/stable/_images/iris.sv



you can see how the decision tree made is plotted.



2.Less preprocessing is required when compared to other algorithms.Less effort in preprocessing makes it much handy.



3.This algorithm can handle missing values and it works healthy while working with outliers.



4.The usage is simple hence its very understandable.It looks like if-else statements



5.They can be stacked with other algorithms and can reach excellent results



6.They dont require setting of lots of parameters and can easily handle multidimensional data.



Thats it! Now you know what makes decision trees so popular! But this doesn't mean they can perform outstanding always.