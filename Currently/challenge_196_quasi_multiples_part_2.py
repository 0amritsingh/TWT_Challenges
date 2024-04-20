# Challenge 196: Quasi-multiples, Part 2
# Difficulty: 3/10
# Labels: Divisors
# This is the second problem in our exploration of simple modular arithmetics.

# Call a positive integer N a quasi-multiple of positive integer m if the remainder when N is divided by m is either 1 or m-1. For example, 28 is a quasi-multiple of 9 and 23 is a quasi-multiple of 8, but 30 is not a quasi-multiple of 5. All integers are a quasi-multiple of 1.

# SnowballSH had a dream about quasi-multiples. In his dream, he saw two integers N and m. He knew that N is a quasi-multiple of m, but he forgot what m was. Help him find the number of distinct integers m that could have been the one in his dream.

# Task
# You are given a number T and T testcases follow, for each testcase,

# The only line contains a positive integer N.
# Output a single integer, the number of positive integers m such that N is a quasi-multiple of m. If there are infinitely many such m, output inf.

# Note that an O(N) algorithm may be too slow, depending on your implementation. This problem can be solved in O(sqrt(N)).

# Examples
# input
# 9
# 1
# 2
# 3
# 300
# 17
# 2024
# 1048577
# 1048576
# 1048575

# output
# inf
# 2
# 3
# 7
# 9
# 20
# 27
# 51
# 23

# For testcase 3, m could have been 1, 2, 4.
# For testcase 4, m could have been 1, 7, 13, 23, 43, 299, 301.

# Note
# 1 <= T
# 1 <= N <= 10^9


