---
author: Rabson J Phiri
author_email: phirirabsonj@gmail.com
categories: [other]
date: '2020-10-26T17:27:18+01:00'
id: 003-css-image-display-fix.md
image: assets/images/img.svg
keywords: CSS, Images, Image Display
layout: post
meta-description: How to get rid of the small space under your images
tags: [CSS, Images, Image Display]
template: post
title: FIx for properly displaying images
title_new: css-image-display-fix.md
---



# CSS Image DIsplay Fix



You might or might not have noticed this, but when you inspect images on a webpage using your Dev Tools, there's a small line underneath them, unless this was "fixed" by the developer.



This is not really a bug. It happens because images are inline elements, and once you look at the image below, you'll begin getting the sense.



<div align="center">

  <img src="images/baseline.jpg">

</div>



The green line is the **baseline**, an invisble line on which elements "sit". As you can see, some characters in the word `paragraph` go beyond this line, creating the red line you're seeing. And since images are inline elements, they "sit" on the baseline relative to elements before or after them, leaving a whitespace between their base and the space created by characters going beyond the baseline.



To avoid this, just give the images a `display: 'block';`



```html

img {

   display: block;

}

```



There, done! Now all images on your page won't have that annoying whitespace as they will fill it up.