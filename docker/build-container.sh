#!/bin/bash                                                                                                                                              

#                                                                                                                                                        
# Build a new .../deepspeech_torch image                                                                                                                 
#                                                                                                                                                        

WHOAMI=$(whoami)
CONTAINERNAME=danspeech-cuda10.1
TAGNAME="$WHOAMI/$CONTAINERNAME"


docker build --file="Dockerfile" --tag "$TAGNAME" .
