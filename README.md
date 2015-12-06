# sillyPythonDuplicateFinder

Simple python script for finding duplicate files in directories.  About 10,000 duplicate finders exist, but I wanted one to do fuzzy matching on filenames according to the filenaming conventions I use.

###Usage

For each directory you're comparing, issue `ls -AlhF > directoryname.txt` to output the content list of the directory.  Add each of these txt files to the `input` folder.  Execute python script.
