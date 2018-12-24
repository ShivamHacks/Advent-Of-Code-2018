"""

### PART 1

Want to parse a log file of guard sleep times
and find the guard that sleeps the most and the
minute they are most likely to be asleep based
on history.

Method:

Go through log file line by line:
1. Keep track of total minutes slept for every guard
2. Keep a tally of how many times they have fallen
asleep on specific minutes of the 60 possible minutes

Once processing complete, go through all guards and
find the guard that has the most minutes slept. For that
guard, find the minute that has the most tallies - that
is the minute the guard slept the most so is most likely
to fall asleep on.

Return guardID * minuteMostSleptOn

### PART 2

Want to get the guard that is most frequently asleep
on the same minute.

Method:

Go through tally of number of times guards fell asleep
on a specific minute and the find the largest tally and
return the guard that corresponds to that tally.

"""

import re
import numpy as np

lines = [line.rstrip('\n') for line in open('input4.txt')]

# Test input
"""
lines = [
	'[1518-11-01 00:00] Guard #10 begins shift',
	'[1518-11-01 00:05] falls asleep',
	'[1518-11-01 00:25] wakes up',
	'[1518-11-01 00:30] falls asleep',
	'[1518-11-01 00:55] wakes up',
	'[1518-11-01 23:58] Guard #99 begins shift',
	'[1518-11-02 00:40] falls asleep',
	'[1518-11-02 00:50] wakes up',
	'[1518-11-03 00:05] Guard #10 begins shift',
	'[1518-11-03 00:24] falls asleep',
	'[1518-11-03 00:29] wakes up',
	'[1518-11-04 00:02] Guard #99 begins shift',
	'[1518-11-04 00:36] falls asleep',
	'[1518-11-04 00:46] wakes up',
	'[1518-11-05 00:03] Guard #99 begins shift',
	'[1518-11-05 00:45] falls asleep',
	'[1518-11-05 00:55] wakes up'
]
"""
"""
Note: there is a single guard on duty at one time
In real input, log file may not be sorted by date
so need to do that first.
Note: the lines may have a variety of text, but because
the first part of the string is the date in the same format:
[date] ... then sorting the array of lines using the string's
lexical order will be enough because 1) there are not duplicate dates
2) so only the date will ever be used to sort
"""

lines = sorted(lines)

guard_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] Guard #(\d+) begins shift'
asleep_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] falls asleep'
awake_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] wakes up'

current_guard = None
asleep_time = None

# map to store total time sleeping for each guard
sleep_times = {}
# table of which minutes guards sleep
minutes_asleep = {}

for line in lines:
	
	if re.match(guard_pattern, line):
		# new guard
		matches = re.match(guard_pattern, line)
		current_guard = matches.group(2)
		if current_guard not in sleep_times:
			sleep_times[current_guard] = 0
			minutes_asleep[current_guard] = np.zeros(60)

	elif re.match(asleep_pattern, line):
		# current guard falls asleep
		matches = re.match(asleep_pattern, line)
		asleep_time = int(matches.group(1))

	elif re.match(awake_pattern, line):
		# current guard wakes up
		matches = re.match(awake_pattern, line)
		wake_time = int(matches.group(1))
		time_awake = wake_time - asleep_time
		sleep_times[current_guard] = sleep_times[current_guard] + time_awake
		minutes_asleep[current_guard][asleep_time : wake_time] = (
			minutes_asleep[current_guard][asleep_time : wake_time] + 1
		)

### PART 1

# find guard that slept the most
slept_most = max(sleep_times, key = lambda k: sleep_times[k])
# find minute slept most
minute_slept_most = max(
	range(60),
	key = lambda k: minutes_asleep[slept_most][k]
)

print("PART 1: ", int(slept_most) * minute_slept_most)

### PART 2
most_freq_asleep_guard = max(
	minutes_asleep,
	# get most frequently slept minute for guard k
	key = lambda k: np.amax(minutes_asleep[k])
)
most_freq_asleep_min = max(
	range(60),
	key = lambda k: minutes_asleep[most_freq_asleep_guard][k]
)

print("PART 2: ", int(most_freq_asleep_guard) * most_freq_asleep_min)