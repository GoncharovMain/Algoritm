import sys
import math
from math import log2
from time import sleep
from math import exp
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def graphics():
	fig = plt.figure()
	ax = fig.gca()
	plt.scatter(4, 4)
	plt.scatter(3, 2)


	x = np.linspace(-7.5, 7.5, 40)
	y = 1 / (1 + pow(math.e, -x))
	plt.plot(x, y)

	plt.grid()
	plt.show()



def NumbersStyle(input):
	try:
		s = input
		assert 0 <= s <= 99999999
	except (ValueError, AssertionError):
		s = 1234567890
	p_num = {
	0: ' _ | ||_|',
	1: '     |  |',
	2: ' _  _||_ ',
	3: ' _  _| _|',
	4: '   |_|  |',
	5: ' _ |_  _|',
	6: ' _ |_ |_|',
	7: ' _   |  |',
	8: ' _ |_||_|',
	9: ' _ |_| _|',
	}
	for i in range(3):
		for n in str(s):
			print(p_num[int(n)][i*3:i*3+3], end = '')
		print()

def binary_search(list, item):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = int((low + high) / 2)
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] <= smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr): #number sorting
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in main_box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("key is founded")

def look_for_key_rec(box):
	for item in box:
		if is_a_box(item):
			look_for_key_rec(item)
		elif is_a_key(item):
			print("found the key")

def fact(f): #factorial
	if f == 1:
		return 1
	else:
		return fact(f - 1) * f

def PrimeNumber(a): #prime number from 0 to a
	p = True
	PrimeNumb = []
	for i in range(2, a):
		p = True
		for j in range(2, int(i / 2) + 1):
			if i % j == 0:
				p = False
				break
		if p:
			PrimeNumb.append(i)
	return PrimeNumb

def Rect(x, y): #the largest square for the rectangle №2 (no recursion)
	MassPrime = PrimeNumber(50)
	r = []
	t = 1
	x1 = x
	y1 = y
	for i in MassPrime:
		if x % i == 0 and y % i == 0:
			while x % i == 0:
				x = x / i
				y = y / i
				t = t * i
				r.append(i)
	print("Наибольший квадрат: " + str(t))
	NumbersStyle(t)
	print("Общие множители: " + str(r))
	print("Кол-во квадратов: " + str(int((x1 * y1) / (t * t))))
	return t


def LargSq(a, b): #the largest square for the rectangle
	if(a % b == 0):
		return b
	else:
		return LargSq(b, a - (b * int(a / b)))

def SumArr(mas): # sum of array numbers
	if(len(mas) > 0):
		return mas.pop() + int(SumArr(mas))
	return 0

MyList = [1, 50, 10, 68, 15, 6, 4, 2]
def LargNum(list):
	if list[0] < list[1]:
		list.pop(0)
	else:
		list.pop(1)
	if len(list) > 1:
		return LargNum(list)
	else:
		return list[0]

def LargeNumSort(list):
	return selectionSort(list)[len(list)]



def qsort(list): #Quick sort (my version)
	if len(list) < 2:
		return list
	else:
		center = int(len(list) / 2) ##
		t = list[int(len(list) / 2) - 1] ##
		print(str(len(list)) + " : " + str(center) + " : " + str(list) + " : " + str(t))
		left = [i for i in list[0:] if i < t] ##change 0 to 1
		right = [i for i in list[0:] if i > t]
		return qsort(left) + [t] + qsort(right)

		
def Qsort(L):
	if len(L) > 2: return Qsort([x for x in L if x < L[0]]) + [x for x in L if x == L[0]] + Qsort([x for x in L if x > L[0]])
	return []


MyArr = [50, 20, 14, 53, 24, 52, 77]
#print(Qsort(MyArr))

#print("Before " + str(MyArr))
#print("After " + str(qsort(MyArr)))
#**************************************************************

book = dict()
book["Hi"] = "Hello"	
#print(book["Hi"])

voted = {}
def check_voter(name):
	if voted.get(name):
		print("kick them out")
	else:
		voted[name] = True
		print("Let them vote!")

#*****************

def person_is_seller(name):
	return name[-1] == 'y'

def search_number(name):
	graph = {
	"you":["alice", "bob", "claire"],
	"bob":["anuj", "peggy"],
	"alice":["peggy"],
	"claire":["thom", "jonny"],
	"anuj":[],
	"peggy":[],
	"thom":[],
	"jonny":[]
	}
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue: 
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller!")
				return True
			else:
				print(person + " isn't mango seller!")
				search_queue += graph[person]
				searched.append(person)
	return False

def print_trajectory_graph(start, end, way):
	s = ""
	for w in way.keys():
		s += w + " -> "
	s += str(end) + " : " + str(len(way))
	print(s)

def print_min_way(start, end, way):
	s = ""
	min_index = 0
	min_len = len(way[min_index])
	for i in range(1, len(way)):
		l = len(way[i])
		if min_len > l:
			min_len = l
			min_index = i
	for k in way[min_index].keys():
		s += str(k) + " -> "
	s += str(end) + " : " + str(min_len)
	print("Кратчайший путь из " + str(start) + " в " + str(end) + ": " + s)

def find_nearest_path(start, end, graph):
	result = []
	i = 0
	CountWays = 1
	s = start
	result.append({})
	while i < CountWays:
		if len(result[i]) > 0: 
			k = list(result[i].keys())[-1]
			s = result[i][k]
		else:
			s = start
		while s != end:
			if len(graph[s]) > 1:
				for n in range(1, len(graph[s])):
					t = result[i].copy()
					result.append(t)
					result[-1][s] = graph[s][n]
					CountWays += 1
			result[i][s] = graph[s][0]
			s = graph[s][0]
		i += 1
	return result 

graph_1 = {
'A':['B', 'D', 'E'],
'B':['C', 'D'],
'C':['D', 'L'],
'D':['L', 'K'],
'E':['F', 'O'],
'F':['D', 'K', 'M'],
'L':['K'],
'O':['P','R'],
'P':['R', 'S'],
'S':['T', 'W'],
'R':['M', 'W'],
'W':['T'],
'T':['M'],
'M':['K', 'X'],
'K':['X']
}

#way_1 = find_nearest_path('A', 'X', graph_1)
#for i in range(len(way_1)):
#	print_trajectory_graph('A', 'X', way_1[i])
#print("Количество путей: " + str(len(way_1)))
#print_min_way('A', 'X', way_1)

#graphics()

Z = [1, 0, 0, 0, 0]
X1 = [-6, 5, 2, -1, 2]
X2 = [-4, 2, 4, 2, 0]
S1 = [0, 1, 0, 0, 0]
S2 = [0, 0, 1, 0, 0]
S3 = [0, 0, 0, 1, 0]
S4 = [0, 0, 0, 0, 1]
solution = [0, 20, 16, 2, 7]

def print_table(z, x1, x2, s1, s2, s3, s4, sol):
	print("z\t\t\tx1\tx2\ts1\ts2\ts3\ts4\tsol")
	for i in range(len(Z)):
		print(
			str(round(z[i], 3)) + "\t\t" + 
			str(round(x1[i], 3)) + "\t\t" + 
			str(round(x2[i], 3)) + "\t\t" + 
			str(round(s1[i], 3)) + "\t\t" + 
			str(round(s2[i], 3)) + "\t\t" + 
			str(round(s3[i], 3)) + "\t\t" + 
			str(round(s4[i], 3)) + "\t\t" + 
			str(round(sol[i], 3))
			)

def MinValIndex(x_n, sol):
	for i in range(1, len(sol)):
		if sol[i] / x_n[i] > 0:
			min_value_index = i #2
			min_value = x_n[i] 	#x_n[2] = 4
			break

	for i in range(min_value_index + 1, len(sol)):
		if x_n[i] == 0:
			continue
		if sol[i]/x_n[i] > 0 and min_value > sol[i]/x_n[i] and sol[i]/x_n[i] != sol[min_value_index] / x_n[min_value_index]:
			min_value_index = i
			min_value = x_n[i]

	return min_value_index


def iter_basis_sol(MaxX, z, x1, x2, s1, s2, s3, s4, sol):
	min_lead_index = MinValIndex(MaxX, sol)
	print("leading line: x_n[" + str(min_lead_index) + "] = " + str(round(MaxX[min_lead_index], 3)) + " -> (" + 
		str(round(sol[min_lead_index], 2)) + " / " + str(round(MaxX[min_lead_index], 2)) + ")")
	x = MaxX[min_lead_index] # 3
	z[min_lead_index] /= x
	x1[min_lead_index] /= x
	x2[min_lead_index] /= x
	s1[min_lead_index] /= x
	s2[min_lead_index] /= x
	s3[min_lead_index] /= x
	s4[min_lead_index] /= x
	solution[min_lead_index] /= x
	#print_table(z, x1, x2, s1, s2, s3, s4, sol)
	print("************************************")
	for i in range(len(z)):
		if(i == min_lead_index):
			continue
		x = MaxX[i]
		z[i] = z[i] - x * z[min_lead_index]
		x1[i] = x1[i] - x * x1[min_lead_index]
		x2[i] = x2[i] - x * x2[min_lead_index]
		s1[i] = s1[i] - x * s1[min_lead_index]
		s2[i] = s2[i] - x * s2[min_lead_index]
		s3[i] = s3[i] - x * s3[min_lead_index]
		s4[i] = s4[i] - x * s4[min_lead_index]
		sol[i] = sol[i] - x * sol[min_lead_index]
	print_table(z, x1, x2, s1, s2, s3, s4, sol)





#************************************
print("************************************")

print("step 1")
iter_basis_sol(X1, Z, X1, X2, S1, S2, S3, S4, solution)
print("step 2")
iter_basis_sol(X2, Z, X1, X2, S1, S2, S3, S4, solution)
print("step 3")
iter_basis_sol(S4, Z, X1, X2, S1, S2, S3, S4, solution)
#iter_basis_sol(S4, Z, S1, S2, X1, X2, S3, S4, solution)
print("************************************")
#************************************


#Z = 	[1, 0, 0, 0, 0]
#X1 = 	[-5,3, 2, 1, 4]
#X2 = 	[3,-2, 3,-1, 7]
#S1 = 	[0,-1, 0, 0, 0]
#S2 = 	[0, 0,-1, 0, 0]
#S3 = 	[0, 0, 0, 1, 0]
#S4 = 	[0, 0, 0, 0, 1]
#solution = [0, 6, -6, 4, 28]

Z = 	[-1, 0, 0, 0, 0]
X1 = 	[5, -3 , -2, -1, -4]
X2 = 	[-3, 2, -3, 1, -7]
S1 = 	[0, 1, 0, 0, 0]
S2 = 	[0, 0, 1, 0, 0]
S3 = 	[0, 0, 0,-1, 0]
S4 = 	[0, 0, 0, 0,-1]
solution = [0, -6, 6, -4, -28]




print("*****************My project*******************")
print_table(Z, X1, X2, S1, S2, S3, S4, solution)
print("*******step 1*******")
iter_basis_sol(X1, Z, X1, X2, S1, S2, S3, S4, solution)
print("*******step 2*******")
iter_basis_sol(X2, Z, X1, X2, S1, S2, S3, S4, solution)
print("*******step 3*******")
iter_basis_sol(S4, Z, X1, X2, S1, S2, S3, S4, solution)
print("************************************")