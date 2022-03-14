---
author: Zoran Pandovski
author_email: zoran.pandovski@keitaro.com
categories: [ci]
date: '2020-06-21T20:28:46+02:00'
description: Increase Travis timeouts with one prefix
id: 001-travis-timeouts-wait.md
image: assets/images/time.svg
keywords: ci, travis-ci, travis
layout: post
tags: [ci, travis-ci, travis]
template: post
title: How to increase Travis CI timeout?
title_new: travis-timeouts-wait.md
---



There are different use cases where Travis jobs could raise the timeout error. Maybe you are trying to install a Python module that takes some time before installing the dependencies e.g:



```yml

install:

    pip install torch

```

or you are running the Java project tests e.g



```yml

script:

    mvn package -Dtestng=test.xml

```

or pushing a new image to the Docker registry e.g



```yml

script:

    docker push $APPLICATION:$IMAGE_VERSION;

```



The default Travis job timeout is set to 10 min, so in some scenarios the above commands will fail with:



```

Timeout (20 minutes) reached. Terminating "..."

```



To increase the `timeouts` travis ci offers a [function](https://docs.travis-ci.com/user/common-build-problems/#build-times-out-because-no-output-was-received) that will increase the build timeouts:



```yml

install: travis_wait N mvn install

```



The `travis_wait n`  where the `n` is the minutes by which the waiting time is increased.



>Note: You must carefully use `travis_wait` since it can extend the build time when there could happen another issue.