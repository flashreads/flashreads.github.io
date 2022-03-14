---
author: Melissa Gonzalez
author_email: gonzalm7@wwu.edu
categories: [javascript]
date: '2021-10-16T00:00:00'
id: 014-javascript-arrow-functions
image: assets/images/javascript/arrow.svg
keywords: javascript, functions
layout: post
meta-description: Beginner intro to JavaScript Arrow Functions
tags: [development - javascript]
title: JavaScript Arrow Functions
title_new: javascript-arrow-functions.md
---



# Arrow Functions



An arrow function expression has a shorter syntax compared to regular functions expressions. There are two key differences: arrow functions are always anonymous and are non-binding of ‘this’.



Before:



```javascript

hello = function() {

  return "Hello World!";

};

```



After:



```javascript

hello = () => {

  return "Hello World!";

};

```



It can be even shorter if the function has only ONE statement that returns a value.



Example:



```javascript

hello = () => "Hello World!";

```



## How to Use Parameters



```javascript

hello = (param) => "Hello " + param;

```



OR without parenthesis



```javascript

hello = (param) => "Hello " + param;

```



## How to Handle 'this'



Regular functions always define its ‘this’ value but arrow functions treat ‘this’ keyword differently. They do not define their own context since it doesn’t have its own ‘this’ context. It is inherited from the parent scope whenever you call ‘this’.



Example:



Regular Function:



```javascript

var obj = {

  count: 10,

  doSomethingLater: function() {

    setTimeout(function() {

      // the function executes on the window scope

      this.count++;

      console.log(this.count);

    }, 300);

  },

};



obj.doSomethingLater(); // result is "NaN", because the property "count" is not in the window scope.

```



Arrow Function:



```javascript

var obj = {

  count: 10,

  doSomethingLater: function() {

    // The traditional function binds "this" to the "obj" context.

    setTimeout(() => {

      // Since the arrow function doesn't have its own binding and

      // setTimeout (as a function call) doesn't create a binding

      // itself, the "obj" context of the traditional function will

      // be used within.

      this.count++;

      console.log(this.count);

    }, 300);

  },

};



obj.doSomethingLater();

```
