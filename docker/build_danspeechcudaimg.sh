#!/bin/bash

WHOAMI=$(whoami)
CONTAINERNAME=pytorch:danspeech
TAGNAME="$WHOAMI/$CONTAINERNAME"

docker build --file="df_danspeechcudafrompytorch" --tag "$TAGNAME" .
