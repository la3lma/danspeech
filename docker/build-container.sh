#!/bin/bash                                                                                                                                              

#                                                                                                                                                        
# Build a new .../deepspeech_torch image                                                                                                                 
#                                                                                                                                                        

WHOAMI=$(whoami)
CONTAINERNAME=pytorch_cuda101:dsfromdockerf
TAGNAME="$WHOAMI/$CONTAINERNAME"


docker build --file="Dockerfile-from-bash-history" --tag "$TAGNAME" .
