#!/bin/bash

#
# Build a new .../deepspeech_torch image
#

WHOAMI=$(whoami)
CONTAINERNAME=danspeech_demoserver
TAGNAME="$WHOAMI/$CONTAINERNAME"


docker build --file="Dockerfile-demo-server" --tag "$TAGNAME" .
