#!/usr/bin/env python
#  
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


for host in sensors:
runBash("rwfilter --start-date=%s --end-date=%s --protocol=1,6,17 --sensor= --type=all --pass=stdout | rwstats --count=10 --fields=sip,$")



