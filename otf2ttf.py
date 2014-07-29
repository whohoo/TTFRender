#!/usr/bin/python
#
# utility convert stix otf fonts to ttf
#
import ConfigParser
import fontforge
import json
import optparse
import os
import sys
import urllib
import urllib2

parser = optparse.OptionParser()
parser.add_option("--input", dest="input", help="directory with otf fonts", default=".")
parser.add_option("--output", dest="output", help="directory for ttf fonts", default=".")
parser.add_option("--quiet", action="store_false", dest="verbose", default=True)

(options, args) = parser.parse_args()

count = 0
fileList = os.listdir(options.input)
for fileName in fileList:
	
	if fileName[-4:] != ".otf":
		continue

	if options.verbose:
		sys.stdout.write("INFO: processing %s\n" % fileName)
	
	dest = os.path.join(options.output, fileName[:-4] + ".ttf")
	
	theFont = fontforge.open(fileName)
	
	theFont.generate(dest)
	
	if options.verbose:
		sys.stdout.write("INFO: saved as %s\n" % dest)

	count += 1
	
if options.verbose:
	sys.stdout.write("INFO: %d fonts converted\n" % count)




