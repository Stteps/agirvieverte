#!/bin/sh
cp -rfu /cache/node_modules/. /frontend/node_modules/
exec "$@"