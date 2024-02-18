#!/bin/sh

export FLASK_APP=./discogs_wantlist_watch/index.py

python3 -m flask --debug run -h 0.0.0.0

