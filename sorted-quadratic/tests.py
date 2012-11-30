from random import randint
from main import sorted_quadratic

num_tests = 100

def run_random_test():
	a = randint(-100, 100)
	b = randint(-100, 100)
	c = randint(-100, 100)
	
	test_data = []
	for _ in range(randint(0, 16)):
		test_data.append(randint(-100, 100))
		
	test_data.sort()
	
	result = sorted_quadratic(test_data, a, b, c)
		
	print '=================================================================='
	print 'input: ', test_data, a, b, c 
	print 'output: ', result
	
	return sorted(result) == result
	

def run_tests():
	num_passed, num_failed = 0, 0

	for _ in range(num_tests):
		if run_random_test():
			num_passed += 1
		else:
			num_failed += 1
		
	print 'Passed %s tests, failed %s' % (num_passed, num_failed)
		
run_tests()