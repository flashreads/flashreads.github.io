---
author: Alex Kimeu
author_email: zoran.pandovski@gmail.com
categories: [javascript]
date: '2020-10-31T17:50:04+01:00'
id: 009-array-sort-method
image: assets/images/javascript/sort1.svg
keywords: javascript, es6, beginner, codenewbie
layout: post
meta-description: Learn JavaScript array.sort() method
tags: [javascript, es6, beginner, codenewbie]
template: post
title: JavaScript Array.sort() Method
title_new: array-sort-method.md
---



## JavaScript Array sort() method.



<img src="https://media-exp1.licdn.com/dms/image/C4D22AQHO5yOEY-_nUw/feedshare-shrink_800-alternative/0?e=1605744000&v=beta&t=5gF_H5Bk1GimAMRvDKBFAGQ8eoKGaQNaTHZxLWKsfFA">



This method sorts the elements of an array in ascending order by default. It converts the elements from the array to strings then compares their sequences of utf-16 code values.

For an array of strings, this works perfectly fine. However, to sort an array of numbers, this method will not work as expected because it converts the elements to strings first.



To achieve what you expect, you can provide a compare function as a callback to the sort method. There are 3 possible outcomes in the callback function: **_1. < 0 : a comes first_** **_2. 0 : no change_** **_3. > 0 : b comes first_**

If you want to sort in descending order, you can return b - a in the callback function.
