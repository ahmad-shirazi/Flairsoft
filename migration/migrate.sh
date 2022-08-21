#!/usr/bin/env bash
set -e

echo "current env is dev"
cd src
ls
echo "Running migrations ..."
alembic upgrade head
