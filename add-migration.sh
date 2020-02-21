#!/bin/bash

if test -z "$1"; then
  echo "Please provide a migrate name..."
  exit 2
fi

name=`echo $@ | sed 's/ /_/g'`

cmd="alembic revision --autogenerate -m $name"
echo $cmd
exec $cmd
