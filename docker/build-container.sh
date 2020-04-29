#!/bin/bash

#
# Build a new .../deepspeech_torch image
#

WHOAMI=$(whoami)
CONTAINERNAME=pytorch_cuda101:dsfromdockerf
TAGNAME="$WHOAMI/$CONTAINERNAME"
#CONTAINER_BASE_NAME=danspeech-p-cuda10.1
#TAGNAME="$WHOAMI/$CONTAINER_BASE_NAME"

docker build --file="Dockerfile-from-bash-history" --tag "$TAGNAME" .
