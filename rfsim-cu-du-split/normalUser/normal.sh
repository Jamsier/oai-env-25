#!/bin/bash

( sleep 300 && kill $$ ) &
python3 test.py