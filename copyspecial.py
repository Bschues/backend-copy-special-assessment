#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# _author_ = Bschue

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""


def get_abs(dir):
    special = []
    count = 0
    # List all the files in the given directory and loop over them
    for file in os.listdir(dir):
        # Search the file name for a string of characters
        match = re.search(r'__\w+__', file)
        # If found, append the filename to the special list
        if match:
            count += 1
            special.append(os.path.abspath(file))
    # Return the special list
    print('Found {} special files:'.format(count))
    print('\n'.join(special))
    return special


def copy_files(s_paths, path):
    # If the directory provided doesn't exist, make a new one,
    #   then copy every filename in the provided list of paths
    #   to the new directory path
    count = 0
    if not os.path.exists(path):
        os.makedirs(path)
    for file in s_paths:
        count += 1
        shutil.copy(file, path)

    print('Copied {} files to {}'.format(count, path))
    return


def zip_files(s_paths, path):
    print("Command I'm going to run:")
    # Create the front of the cmd that you're going to run
    cmd = 'zip -j ' + path
    # Loop over the special paths and add them to the command
    for s_path in s_paths:
        cmd += ' ' + s_path
    # Print the command being run
    print(cmd)
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print(output)
        sys.exit(status)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='directory holding the special files')
    args = parser.parse_args()

    # Checks if arguments were provided, if not
    # prints how to use the program
    if not args:
        parser.print_usage()
        sys.exit(1)

    special_files = (get_abs(args.fromdir))
    if args.todir:
        copy_files(special_files, args.todir)
    if args.tozip:
        zip_files(special_files, args.tozip)


if __name__ == "__main__":
    main()
