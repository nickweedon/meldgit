#!/bin/python

import argparse
import os

from subprocess import Popen, PIPE

def cyg2win(cygwinPath):
    # Make sure tha path is absolute
    cygwinPath = os.path.realpath(cygwinPath)
    p = Popen(['cygpath', '-w', cygwinPath], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    if p.returncode != 0:
        raise Exception("Could not convert cygiwn path: '", cygwinPath, "' to a valid windows path.")
    return output.strip()

def executeMeldDiff(meldArgs):
    baseArgs = ["meld"]
    baseArgs.extend(meldArgs)
    p = Popen(baseArgs)
    p.communicate()
    if p.returncode != 0:
        raise Exception("Meld returned a non-zero exit code")

parser = argparse.ArgumentParser(description="Wrapper script for Meld for use with Git")
parser.add_argument('-l', '--local')
parser.add_argument('-r', '--remote')
args = parser.parse_args()

print "Local", cyg2win(args.local)
print "Remote", cyg2win(args.remote)

executeMeldDiff([cyg2win(args.local), cyg2win(args.remote)])
