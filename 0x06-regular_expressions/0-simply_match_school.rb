#!/usr/bin/env ruby
# This script matches the word "School" passed as argument

arg = ARGV[0] # gets first argument from terminal
regex = /[S]chool/ # creates search pattern

matches = arg.scan(regex)
puts matches.join("")
