#!/bin/bash

git remote add upstream "https://${geo_token}@github.com/redjumper/geo2addresslist"

#git checkout -b master
git add -A
git commit -m 'Update'
git push -u upstream HEAD:master 