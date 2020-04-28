#!/bin/bash                                                                                                                                              

#                                                                                                                                                        
# Build a new .../deepspeech_torch image                                                                                                                 
#                                                                                                                                                        

WHOAMI=$(whoami)
CONTAINERNAME=danspeech-p-cuda10.1
TAGNAME="$WHOAMI/$CONTAINERNAME"


docker build --file="Dockerfile-from-bash-history" --tag "$TAGNAME" .
