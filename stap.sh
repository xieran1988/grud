#!/bin/bash

sudo stap all.stp | ./nc.pl 127.0.0.1 1900
