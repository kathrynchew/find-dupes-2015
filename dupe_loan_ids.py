import sys

data = sys.argv[1]
dupes_count = {}
dupes_contents = {}
dupes = {}

def find_dupes():
	"""Reads through file; for any profiles originated in 2015, counts how many 
	times a given user identifier (ssn_id) appears, logs count in dict 
	dupes_count, also saves remaining contents (loan_id) of line in dict
	dupes_contents for later."""

	for line in open(data):
		line = line.rstrip().split(",")
		if line[0] == '2015':
			if line[1] in dupes_count:
				dupes_count[line[1]] += 1
				dupes_all_else[line[1]].append(line[2])
			else: 
				dupes_count[line[1]] = 1
				dupes_all_else[line[1]] = [line[2]]

def surface_dupes():
	"""Surfaces info for accounts with multiple loans by checking frequency count
	of a given user identifier (ssn_id). Any user identifier that occurs more than
	once has all associated loan_id items put into dict dupes and prints to console
	or file, as specified by user."""

	for key, value in dupes_count.items():
		if value > 1:
			dupes[key] = dupes_all_else[key]

find_dupes()
surface_dupes()
print dupes