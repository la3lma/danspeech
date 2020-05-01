#!/bin/bash

python3 danspeechdemo/manage.py runserver 0.0.0.0:8000 & 
sleep 5
curl --connect-timeout 600 http://0.0.0.0:8000/
exit 0
