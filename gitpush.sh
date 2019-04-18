#!/bin/#!/bin/sh

git config --global user.name "insideman02468"
git config --global user.email "insideman02468@gmail.com"
git remote add origin https://github.com/insideman02468/TestHeroku.git
git status
git checkout book2
git add --all
git commit -m "Finish Django nyumon(５)"
git push origin book2
