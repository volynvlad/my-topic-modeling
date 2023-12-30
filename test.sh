#!/bin/sh

docker build -t  my-topic-modeling-test -f Dockerfile-test . &&
docker run --rm -t my-topic-modeling-test pytest
