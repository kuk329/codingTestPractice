from typing import List

total_nodes = 0

# prints subset found
def print_subset(A:List[int], size:int)->None:
	for i in range(size):
		print(A[i], end=' ')
	print()

# inputs
# s		 - set vector
# t		 - tuplet vector
# s_size	 - set size
# t_size	 - tuplet size so far
# sum		 - sum so far
# ite		 - nodes count
# target_sum - sum to be found
def subset_sum(s:List[int], t:List[int], s_size:int, t_size:int, sum_so_far:int, ite:int, target_sum:int)->None:
	global total_nodes
	total_nodes += 1
	if target_sum == sum_so_far:
	
	# We found sum
		print_subset(t,t_size)
		
		# constraint check
		if ite + 1 < s_size and sum_so_far - s[ite] + s[ite + 1] <= target_sum:
		
		# Exclude previous added item and consider next candidate
			subset_sum(s, t, s_size, t_size - 1, sum_so_far - s[ite], ite + 1, target_sum)
		return
	elif ite < s_size and sum_so_far + s[ite] <= target_sum:
		for i in range(ite, s_size):
			t[t_size] = s[i]
			if sum_so_far + s[i] <= target_sum:
				subset_sum(s, t, s_size, t_size + 1, sum_so_far + s[i], i + 1, target_sum)

# Wrapper that prints subsets that sum to target_sum
def generateSubsets(s:List[int], size:int, target_sum:int)->None:
	t = [0]*size
	total = 0
	
	# sort the set
	s = sorted(s)
	for i in range(size):
		total += s[i]
	if s[0] <= target_sum and total >= target_sum:
		subset_sum(s, t, size, 0, 0, 0, target_sum)

# Driver code
weights = [15, 22, 14, 26, 32, 9, 16, 8]
target = 53
size = len(weights)
generateSubsets(weights, size, target)
print("Nodes generated ",total_nodes)

# This code is contributed by hardikkhushwaha
