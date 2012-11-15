#!/usr/bin/env python
# this doesn't do anything yet. it was just a starting point
import sys, os, subprocess, smtplib, time

def runBash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    out = p.stdout.read().strip()
    return out


sensors = ["CHECORE1"]
startdate = runBash("date -d '-12 hour'+%Y/%m/%d:%H")
enddate = runBash("date +%Y/%m/%d:%H")

open('autosilk.data','w')
open('autosilk.data','a').write("Top TalkersReport for Last 12 Hours.\n\n")

