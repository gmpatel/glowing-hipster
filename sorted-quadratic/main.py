def sorted_quadratic(values, a, b, c):
	if a == 0:
		return sorted_linear(values, b, c)
		
	def f(x):
		return a*x*x + b*x + c
		
	vertex_x = -b/(2*a)
	
	left_of_vertex = []
	right_of_vertex = []
	
	for x in values:
		if x < vertex_x:
			left_of_vertex.append(f(x))
		else:
			right_of_vertex.append(f(x))
			
	if a > 0:
		left_of_vertex.reverse()
	else:
		right_of_vertex.reverse()
		
	return merge(left_of_vertex, right_of_vertex)
	
def sorted_linear(values, b, c):
	output = [ b*x + c for x in values]
	
	if b < 0:
		output.reverse()
	
	return output
	
def merge(list_1, list_2):
	output = []
	i_1, i_2 = 0, 0
	
	while i_1 < len(list_1) and i_2 < len(list_2):
		if list_1[i_1] < list_2[i_2]:
			output.append(list_1[i_1])
			i_1 += 1
		else:
			output.append(list_2[i_2])
			i_2 += 1
			
	output += list_1[i_1:]
	output += list_2[i_2:]
	
	return output