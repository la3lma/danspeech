#!/bin/bash                                                                                                                                              

#                                                                                                                                                        
# Build a new .../deepspeech_torch image                                                                                                                 
#                                                                                                                                                        

WHOAMI=$(whoami)
CONTAINERNAME=danspeech10.2
TAGNAME="$WHOAMI/$CONTAINERNAME"


docker build --file="Dockerfile" --tag "$TAGNAME" .
