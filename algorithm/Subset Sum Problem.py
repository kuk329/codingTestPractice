# def subset_sum(numbers, target):
#     # 부분 집합의 합이 목표 값과 일치하는지 확인하는 도우미 함수
#     def backtrack(curr_sum, curr_index):
#         # 기저 조건: 부분 집합의 합이 목표 값과 일치하는 경우
#         if curr_sum == target:
#             return True
        
#         # 기저 조건: 현재 인덱스가 배열의 끝에 도달한 경우
#         if curr_index == len(numbers):
#             return False
        
#         # 현재 인덱스의 숫자를 선택하는 경우
#         if backtrack(curr_sum + numbers[curr_index], curr_index + 1):
#             return True
        
#         # 현재 인덱스의 숫자를 선택하지 않는 경우
#         if backtrack(curr_sum, curr_index + 1):
#             return True
        
#         return False

#     # 백트래킹 알고리즘 호출
#     return backtrack(0, 0)

# # 예시 실행
# numbers = [1, 3, 5, 7, 9]
# target = 12
# print(subset_sum(numbers, target))


# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum


# Returns true if there is a subset of set[]
# with sum equal to given sum
def isSubsetSum(set, n, sum):

	# The value of subset[i][j] will be
	# true if there is a
	# subset of set[0..j-1] with sum equal to i
	subset = ([[False for i in range(sum + 1)]
			for i in range(n + 1)])

	# If sum is 0, then answer is true
	for i in range(n + 1):
		subset[i][0] = True

	# If sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum + 1):
		subset[0][i] = False

	# Fill the subset table in bottom up manner
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j < set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j >= set[i-1]:
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]])

	return subset[n][sum]


# Driver code
if __name__ == '__main__':
	set = [3,4,5,2]
	sum = 6
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")

# This code is contributed by
# sahil shelangia.
