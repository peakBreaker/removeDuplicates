# Remove Duplicates

This repository contains scripts for removing duplicates in a folder and recursive folders.  It works by comparing the MD5 hashes of the files and removing files with duplicate hashes.

Originally created by @dpt for python 2.  I did a quick translation to python 3 and added some docstrings.

## Getting started

### Prereq
- Python 3

### Instructions
1. Clone this repository
2. Run the removeDups.py file with python 3 (tested and working with python 3.7)
3. Remember to add a path as a commandline argument. Eg. python3 removeDups.py ../folder/