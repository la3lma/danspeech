#!/bin/bash
# Build a new .../deepspeech_torch image
#

WHOAMI=$(whoami)
CONTAINERNAME=danspeech-pytorch-pytorch
TAGNAME="$WHOAMI/$CONTAINERNAME"

#  
docker build --file="Dockerfile-from-bash-history-for-pytorch-pytorch" --tag "$TAGNAME" .
