---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [git]
date: '2020-05-20T23:53:42+02:00'
id: 004-checkout-remote-branch
image: assets/images/remote.svg
keywords: git, git-remote, git-checkout, git-branches
layout: post
meta-description: Checkout remote Git branch with one command
tags: [git, git-remote, git-checkout, git-branches]
template: post
title: How to check out a remote Git branch
---



## How to check out a remote Git branch



You need to work on a git branch that you don't have locally, but you are not sure how to pull and switch to that branch.

Let's first list the remote branches so we are sure the branch exists. To list all of the remote branches run:



```bash

git branch -a

```



This will list all of the local and remote branches. 



```

local_branch1

local_branch2

remotes/new_branch

```



The first displayed are all local branches, and the branches that contain `remote/` are the remote branches.

Copy the name of the remote branch you want to work on and execute:



```bash

git checkout new_branch

```



You should see the `Branch 'new_branch' set up to track remote branch 'new_branch' from 'origin'.` message. This means you have successfully checkout to the  `new_branch`. 



## Multiple remotes



There are cases where the repository will contain more than one remote. In that case run:



```bash

git checkout -t <name of remote>/new_branch

```








