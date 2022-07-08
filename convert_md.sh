#!/bin/bash

HTML_EXTRACT=scrap/$(basename $(dirname $1)).html
OUT=src/$(basename $(dirname $1)).md

echo $1 ">>>" $OUT

python scripts/extract_main.py $1 $HTML_EXTRACT
pandoc --from html --to markdown -o $OUT $HTML_EXTRACT
cp -f $OUT scrap/backup.md

scripts/cleanup.sh $OUT

