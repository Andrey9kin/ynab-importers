#!/usr/bin/env bash

set -ex

source env/bin/activate

FILES=$(find ~/Downloads/ -name "Movimi*.xls" -print)

for FILE in ${FILES}
do
  python3 bankinter.py "${FILE}"
  rm -rf "${FILE}"
done 