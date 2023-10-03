#!/usr/bin/env ruby
# This script matches characters in a log file
# Output format: [SENDER],[RECEIVER],[FLAGS]

arg = ARGV[0] # gets first argument from terminal
regex = /(?<=(?:from:|to:|flags:))([a-zA-Z\-:+0-9]+)/ # creates search pattern

matches = arg.scan(regex)
puts matches.join(",")
