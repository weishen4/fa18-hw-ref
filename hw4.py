"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!
import collections
"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):
    if (s == ''):
        return None
    counter = collections.Counter(s)
    return max(counter, key = lambda cha: counter[cha])


"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
	Argument:
		"qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
	Return:
		"qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
	Argument:
		"aardvarks are cool!"
	Return:
		None
"""
def alphabet_finder(s):
    result = set()
    for index, cha in enumerate(s):
        if (cha.isalpha()):
            result.add(cha.lower())
            if (len(result) == 26):
                return s[:index + 1]
    return None



"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
	Argument:
		[1, 2, 3, 1, 4, 5, 6]
	Return:
		[1, 6]
"""
def longest_unique_subarray(arr):
    #L is a changing temp that stores unrepetitive subarray
    L = []
    #key is length, value is start_index for every unique subarray
    result = dict()
    for i in range(len(arr)):
        if arr[i] in L:
            #store the unique array L, and its end index is at i - 1
            result[len(L)] = i - len(L)
            #update L
            L = L[L.index(arr[i]) + 1:]
        L.append(arr[i])
    #update the last one, its end index should be the last index of arr
    result[len(L)] = len(arr) - len(L)
    longest_len = max(result)
    return [result[longest_len], longest_len]

"""
string_my_one_true_love

A former(?) CA for this course really like strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
	Argument:
		"abcbabcdcdda"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
	Return:
		True

Example 2:
	Argument:
		"aaabbbcccddde"
		There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
	Return:
		True

Example 3:
	Argument:
		"aaabbbcccdddeeffgg"
		This string is similar to the other ones, except with 2 e's, f's and g's at the end.
		To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
		one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
	Return:
		False
"""

def string_my_one_true_love(s):
    if (len(s) == 0):
        return False
    counter = collections.Counter(s)
    L = list(set(counter.values()))
    #there's only one left
    if (len(L) == 1):
        return True
    #if there's two left, try to remove 1
    if (len(L) == 2 & abs(L[0] - L[1]) == 1 or L[0] == 1 or L[1] == 1):
        return True
    return False



"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
	Argument:
		[[1920, 80], [1940, 22], [1961, 10]]
	Return:
		1961
"""
def alive_people(data):
	#todo check invalid condition
    d = dict()
    for ele in data:
        startYear, time = ele
        for year in range(startYear, startYear + time + 1):
            if year in d:
                d[year] += 1
            else:
                d[year] = 1
    return max(d, key = lambda year: d[year])

"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
	Arguments:
		[-1, 0, 1, 2, -1, -4], 0
	Return:
		[
			[-1, 0, 1],
			[-1, -1, 2]
		]
"""
def three_sum(arr, t):
    result = []
    arr.sort()
    for i in range(len(arr)):
        start, end = i + 1, len(arr) - 1
        while ( i < start < end):
            triplet_sum = arr[i] + arr[start] + arr[end]
            if (triplet_sum == t):
                if [arr[i], arr[start], arr[end]] not in result:
                    result.append([arr[i], arr[start], arr[end]])
                #update result manually
                start += 1
                end -= 1
            if (triplet_sum < t):
                start += 1
            elif (triplet_sum > t):
                end -= 1
    return result


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
	Argument:
		8
		The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
	Return:
		2468 // 1234 (i.e., 2)
Example 2:
	Argument:
		15
	Return:
		4294967296 ** (1 / 16) (i.e., 4)
"""
def isHappyNum(n: int) -> bool:
    result = {n}
    temp = n
    while True:
        nextVal = sum((int(i)**2 for i in str(temp)))
        temp = nextVal
        if nextVal in result:
            #goes into a cycle from here
            if nextVal == 1:
                return True
            return False
        result.add(nextVal)

def happy_numbers(n: int) -> int:
    if (n < 1):
        return 0
    count = 0
    for i in range(1, n + 1):
        if (isHappyNum(i)):
            count += 1
    return count

"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
	Argument:
		[0, 1, 2, 3, 4, 5]
		Clearly, the first element by itself forms a subarray with sum == 0.
	Return:
		[0, 1]

Example 2:
	Argument:
		[10, 20, -20, 3, 21, 2, -6]
		In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
	Return:
		[1, 2]
"""
def zero_sum_subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i: j + 1]) == 0:
                return [i, j - i + 1]
    return None


