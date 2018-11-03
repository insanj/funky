#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import urllib2

param = sys.argv[-1]
baseurl = "https://funky.host/"
funkyurl = baseurl + param
response = urllib2.urlopen(funkyurl)
print response.read()
