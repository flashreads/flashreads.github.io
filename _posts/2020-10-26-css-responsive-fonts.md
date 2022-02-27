---
author: Rabson J Phiri
author_email: phirirabsonj@gmail.com
categories: [other]
date: '2020-10-26T13:59:31+01:00'
id: 002-css-responsive-fonts.md
image: assets/images/css1.svg
keywords: CSS, Responsive Fonts, CSS Fonts
layout: post
meta-description: How to make your fonts responsive using fluid units
tags: [CSS, Responsive Fonts, CSS Fonts]
template: post
title: CSS Responsive Fonts
---



# CSS Responsive Fonts



Making sure your fonts adapt to different screen layouts is very important. To help us with this, we often use **rem** units, which are fluid. **REM** stands for *root em*. **1rem** = the root font size, i.e. the default font size of the browser, or the one the user sets. On most browsers, the default font size is **16px**, so **1rem** would equal **16px**.



You can manually set the root font size like this:



```css

html {

   font-size: 10px; /* You can put your desired default font size */

}

```



Therefore, **rem** all font sizes will refer to the 10px. So 



```css

p {

   font-size: 1rem; /* 1rem = 1 x 10px = 10px*/

}



h1 {

   font-size: 2rem; /* 2rem = 2 x 10px = 20px */

}

```



Doing this makes the fonts respond to whatever font size is the default or is set by the use. It is much better the using non-fluid units like PXs. You can read more about CSS units on the [Mozilla Documentaion Page](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)