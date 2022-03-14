---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [git]
date: '2020-05-19T23:44:39+02:00'
id: 002-remove-github-pages.md
image: assets/images/page.svg
keywords: git, github, github-pages
layout: post
meta-description: The missing step for unpublishing the Github pages site
tags: [git, github, github-pages]
template: post
title: How to unpublish GitHub pages site
title_new: remove-github-pages.md
---



# How to unpublish GitHub pages site



Sometimes, you don't want your Github Pages personal website to be available, or you are migrating to the new repository so you need to unpublish the site. The first thing that you would usually do is to:

1. Go to repository settings

2. Under GitHub Pages select the None(Disable GitHub Pages) option from the dropdown.



That is the correct way but, there is one additional step that you need to do, to successfully unpublish the site.



## Delete gh-pages branch



The gh-pages branch is the default publishing source branch for most of the GitHub Pages sites. Make sure that this branch is deleted from the repository:



```git

git push origin -d gh-pages

#git version older then 1.7

git push origin :gh-pages

```



If the response is `fatal: 'gh-pages' does not appear to be a git repository`, make sure that you have the branch locally before deleting it:



```git

git pull origin gh-pages

```

and then delete it. For additonal informations about `How to delete remote branch in Git` check [delete-remote-branch](https://github.com/oneminblogs/content/blob/unpublish-gh-pages/git/001-delete-remote-branch.md)



That's all. You have successfully unpublish the GitHub Pages site.

>Note: If you are using a custom domain for the GitHub Pages site, make sure to update your DNS settings.
