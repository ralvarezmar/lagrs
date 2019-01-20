#!/bin/bash
docker run --rm -it -h rmarbind01 --name rmarbind01 -v $HOME:/home/$USER rmartin/bind
