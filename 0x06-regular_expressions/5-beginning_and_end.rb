#!/usr/bin/env ruby
# This script matching a string that starts with h ends
# with n and can have any single character in between

arg = ARGV[0] # gets first argument from terminal
regex = /h.n/ # creates search pattern

matches = arg.scan(regex)
puts matches.join("")
