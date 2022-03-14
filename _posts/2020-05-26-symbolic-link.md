---
author: subhgogoi
author_email: subhendu.gogoi@vantagecircle.com
categories: [linux]
date: '2020-05-26T21:27:27+02:00'
id: 007-symbolic-link.md
image: assets/images/link.svg
keywords: linux, symlinc
layout: post
meta-description: What is Symbolic Link?
tags: [linux, symlink, symbolic-links]
template: post
title: Symbolic link
title_new: symbolic-link.md
---



# Symbolic Link



## What is Symbolic Link?

A symlink or a Symbolic Link is simply enough a shortcut to another file. It is a file that points to another file.



## How to create a Symbolic Link?

Files is a symbolic link to /images/files/prod/files. When you access files or anything inside it, you'll really access the path under /images. Symbolic links are made and updated using the ln command. This link could have been made with:



```

ln -s /images/files/prod/files files

```

-s means to make a symbolic link. To update a link, either delete the link and create it as above, or use the -f option to ln as well. If you are linking to a folder, you should include the -n option:



```

ln -sfn /a/new/path files

```



This will replace the link with a new one pointing at /a/new/path.



The -n option is necessary when linking to a different target folder to avoid creating a sub-folder inside that symbolic link and instead replace the symbolic link completely.
