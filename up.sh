#!/bin/bash

mkdir -p data
mkdir -p data/roach1
mkdir -p data/roach2
mkdir -p data/roach3

ROACH_TEST_PATH=$(pwd)/code ROACH_DATA_ROOT=$(pwd)/data docker-compose up