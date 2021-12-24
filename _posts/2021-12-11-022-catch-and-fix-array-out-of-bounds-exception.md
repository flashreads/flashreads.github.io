---
author: Kosta Lazarevski
author_email: 44593214+KostaLaz@users.noreply.github.com
categories: [java, exception]
date: '2021-12-11T18:30:31.727884'
id: 022-catch-and-fix-array-index-out-of-bounds-exception-in-java.md
image: assets/images/fix.svg
keywords: exception, arrayoutofboundsexception, javaruntimeexception
layout: post
meta-description: Learn how to catch and fix ArrayIndexOutOfBoundsException in Java
tags: [arrayoutofboundsexception, exception, runtimeexception, java exception]
template: post
title: Catch and fix ArrayIndexOutOfBoundsException in Java
---



## What is a ArrayIndexOutOfBoundsException?



`java.lang.ArrayIndexOutOfBoundsException` is a runtime exception in Java. occurs while processing an array and asking for a position that does not exist within the size of the array.



Since the `ArrayIndexOutOfBoundsException` is a runtime exception, it doesn't need to be caught and handled explicitly in application code.



## Example of a ArrayIndexOutOfBoundsException



In this example we are trying to access an element at index 5 of the animals array, which has only 2 elements. In this case java.lang.ArrayIndexOutOfBoundsException will be thrown.



```java

public class ArrayIndexOutOfBoundsExample {

  public void processArray() {

    List animals = new ArrayList<>();

    names.add("cat");

    names.add("dog");



    return animals.get(5);

  }

}

```



## How to Avoid getting ArrayIndexOutOfBoundsException



The `ArrayIndexOutOfBoundsException` can be avoided using checks and preventive techniques like the following:



1. Always remember that the array is a zero-based index, the first element is at the 0th index and the last element is at length - 1 index.

2. Pay special attention to the start and end conditions of the loop.
