#!/bin/bash

OUT=$1

sed -i -e '/:::/d' $OUT
sed -i -e 's/\\\^/\^/g' $OUT
sed -i -e 's/\\_/_/g' $OUT
sed -i -e 's/\\\\/\\/g' $OUT
sed -i -e 's/\\~/~/g' $OUT
sed -i -e 's/\\\$\\\$/\$\$/g' $OUT
sed -i -e 's/\\\$/\$/g' $OUT
# sed -i -e 's/\\\[/\\lbrack\{\}/g' $OUT
# sed -i -e 's/\\\]\s*/\\rbrack\{\}/g' $OUT
sed -i -e 's/\\>/>/g' $OUT
sed -i -e 's/\\</</g' $OUT
python scripts/cleanup.py $OUT  # Remove NEXT SECTION
