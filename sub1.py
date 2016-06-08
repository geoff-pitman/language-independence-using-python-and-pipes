#sub1.py
import sys

while True:
	input = str(sys.stdin.readline()) + ' something else\n'
	sys.stdout.write(input)
	sys.stdout.flush()