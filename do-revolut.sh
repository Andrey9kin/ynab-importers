#!/usr/bin/env bash

set -ex

source env/bin/activate

FILES=$(find ~/Downloads/ -name "account-statement*.csv" -print)

for FILE in ${FILES}
do
  python3 revolut.py "${FILE}"
  rm -rf "${FILE}"
done