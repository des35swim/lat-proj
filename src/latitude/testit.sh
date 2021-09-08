#!/bin/bash

current_dir=`dirname $0`
cd ${current_dir}/exercise/maxprofit
python -m unittest discover
