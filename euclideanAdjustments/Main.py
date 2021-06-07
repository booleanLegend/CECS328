# Matthew Zaldana (SID: 027008928)

import itertools


# storing method saves all values in dictionary and calculates euclid values
def storing():
    target = 0
    # create empty dict
    fixed_values = {}

    #open file
    with open("input.txt") as file:
        # save target which is the first line
        target = int(file.readline())
        # get remaining values and convert all numbers to ints
        content = file.readlines()
        content = [int(i) for i in content]
        # add each value to fixed_values
        for x_value in range(len(content)):
			# call euclid function on values and save result to key in dictionary
            fixed_values[content[x_value]] = euclid(target, content[x_value])
	# call sum_of_values funtion which will calculate sum of euclidean values
    sum_of_values(target, fixed_values)


# euclid function calculates GCD between target and individual test value
def euclid(target, test):
    if test == 0:
        return target
    else:
        return euclid(test, target % test)


# sum_of_value function calculates current sum of values and creates a new adj target to sum to 
def sum_of_values(target, values):
	adj = 0
	# new adj target to get to
	for key, value in values.items():
		adj += key * value
	if target == adj:
		return
	if len(values) == 0:
		return
	else:
		# calls adjustments function to get combos, saves them, removes repeated values and adds each repeated one to key's value
		combos = []
		adjustments(0, values, len(values) - 1, target, combos)
		for key, value in values.items():
			value += combos.count(key)
		# calls output_adjustments to write answers
		output_adjustments(values)


# adjustments function recursively calls until combos add up to target, then returns the combos
def adjustments(total, values, ele_count, target, l):
	if target == total:
		return l
	if ele_count < 0:
		return
	# going to next element
	adjustments(total, values, ele_count - 1, target, l)
	# on last element, try subtraction to the target
	for current_value, next_value in values.items():
		l.append(current_value)
	adjustments(total + values.__iter__().__next__(), values, ele_count - 1,  target, l)
	l.pop()
	# on the last element, try addition to the target
	for current_value, next_value in values.items():
		l.append(current_value * -1)
	adjustments(total - values.__iter__().__next__(), values, ele_count - 1, target, l)
	l.pop()
	# slices dictionary to next key and recursively calls adjustments function and adding next value
    # for current_value, next_value in values.items():
      #  left = dict(itertools.islice(values.items(), 2, -1))
       # yield from adjustments(target, left, l + [current_value])


# writes adjustments to file
def output_adjustments(adjustments):
	output_file = open('output.txt', 'w')
	for key, value in adjustments.items():
		output_file.write(str(key) + " " + str(value) + "\n")
	output_file.close()


# driver method
if __name__ == "__main__":
    storing()


# 1122 1
# 1156 1
# 84 1
# 1430 1
# 550 1
# 4394 1
# 2618 1
# 10285 1
# 4862 1
