#!/bin/bash

fping `cat *ovpn | grep remote | grep .com | cut -d" " -f2`