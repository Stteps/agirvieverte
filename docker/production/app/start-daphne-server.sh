#!/bin/sh
daphne config.asgi:application --bind 0.0.0.0 -p 8031 --access-log -