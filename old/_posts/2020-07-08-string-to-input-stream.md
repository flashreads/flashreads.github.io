---
author: Pavle Jonoski
author_email: pavle.jonoski@gmail.com
categories: [java]
date: '2020-07-08T15:22:45+02:00'
id: 003-string-to-input-stream.md
image: assets/images/java/input.svg
keywords: java, one-liner, string, input-stream
layout: post
meta-description: Easily convert String to InputStream in Java
tags: [java, one-liner, string, input-stream]
template: post
title: How to convert String to InputStream in Java
---



# Convert String to InputStream in Java



Very often, especially when writing tests, you need to pass an `InputStream ` and

you want to read the data from a `String`.



To convert to input stream, the easiest way is first to convert the string to 

array of bytes, then read from the bytes using `ByteArrayInputStream`.



Here is an one-liner on how to do that in Java:



```java



InputStream stream = new ByteArrayInputStream("my-data".getBytes(StandardCharsets.UTF_8));



```
