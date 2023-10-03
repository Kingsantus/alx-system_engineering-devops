#!/usr/bin/env ruby
# This script matches characters

arg = ARGV[0] # gets first argument from terminal
regex = /hbt+n/ # creates search pattern

matches = arg.scan(regex)
puts matches.join("")
