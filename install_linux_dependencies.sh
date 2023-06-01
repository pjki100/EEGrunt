#!/bin/sh
#
# Install Linux Dependencies
# ==========================
# This little script will automatically install all the packages needed to run
# EEGrunt on (ubuntu) Linux, if you're lucky.


sudo apt-get install  python2-dev build-essential libatlas-base-dev gfortran libpng-dev libfreetype6-dev pkg-config

sudo pip install -r requirements.txt
