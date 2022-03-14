---
author: Rabson J Phiri
author_email: phirirabsonj@gmail.com
categories: [javascript]
date: '2020-10-26T13:59:31+01:00'
id: 006-sort-trick.md
image: assets/images/javascript/sort.svg
keywords: JavaScript, sort, localeCompare
layout: post
meta-description: How to sort strings and avoid unexpected outcomes
tags: [JavaScript, sort, localeCompare]
template: post
title: JavaScript sort trick
title_new: sort-trick.md
---



# Sorting strings in JavaScript



The JavaScript **sort** method is very useful when we want to sort numbers, or even strings. But when sorting strings, we ought to be careful because the strings might be in different languages. Luckily, there's a fix for that. It's called **localeCompare**:



`referenceString.localeCompare(compareString)`



The `referenceString` is the string we want to compare, and the `compareString` is the string against which we're compareing. The `localeCompare` method returns a Number, which may be:



> - -1 if the `referenceString` is sorted before the `compareString`

> - 0 if the two strings are equal

> - 1 if the `referenceString` is sorted after the `compareString`



Here's an example:



```javascript



const words = ['hello', 'répondre', 'sort', 'déclaré'];



words.sort((a, b) => a.localeCompare(b)); 



```



As we can see, some words have certain punctuations. Using `localeCompre` with **sort** helps us sort the English and French words in our array successfully. More documentaion can be found [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)