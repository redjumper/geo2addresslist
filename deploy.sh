#!/bin/bash

git remote add upstream "https://${geo_token}@github.com/redjumper/geo2addresslist"

python geo2addresslist.py
rm GeoLite2-ASN-Blocks-IPv4.csv
#git checkout -b master
git add -A
git commit -m 'Update'
git push -u upstream HEAD:master 
