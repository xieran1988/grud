#!/bin/bash

ldd $1 | awk '{print $1}'

