#!/usr/bin/env ruby
# This script matches uppercase letters

arg = ARGV[0] # gets first argument from terminal
regex = /[A-Z]/ # creates search pattern

matches = arg.scan(regex)
puts matches.join("")
