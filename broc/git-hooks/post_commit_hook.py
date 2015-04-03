#!/usr/bin/python

import subprocess

print "Latest commit was:", subprocess.check_output(['git','rev-parse','HEAD'])
