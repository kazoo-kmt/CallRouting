import csv
import time
from collections import defaultdict

def time_function(func):

	def inner(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		dt = round(end_time - start_time, 6)
		print('Call to function {} -> took {}s'.format(func, dt))
		return result

	return inner

@time_function
def create_map(filenames):
	callmap = {}

	for filename in filenames:
		with open('{}.csv'.format(filename), 'r') as numfile:
			reader = csv.reader(numfile, delimiter=',')
			for row in reader:
				number = row[0][1:]
				cost = float(row[1])
				if number in callmap:
					current_cost = callmap[number]
					callmap[number] = min(current_cost, cost)
				else:
					callmap[number] = cost

	return callmap

@time_function
def find_best_number(callmap, number):
	for i in range(len(number)):
		num = number[:len(number) - i]
		if num in callmap:
			return callmap[num]
	return None

if __name__ == '__main__':
	callmap = create_map(['route-costs'])

	with open('phone-numbers-10k.txt') as fp:
		start_time = time.time()
		while True:
			line = fp.readline()
			if line == '':
				print(round(time.time() - start_time, 6))
				break
			else:
				find_best_number(callmap, line[1:])
