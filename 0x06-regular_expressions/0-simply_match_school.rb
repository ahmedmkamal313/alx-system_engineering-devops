#!/usr/bin/env ruby
# script that accepts one argument and pass it to a regular expression matching method

input = ARGV[0]
match = /School/.match(input)
puts match
