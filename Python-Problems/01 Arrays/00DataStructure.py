"""
Array starts from index 0
append(value) -> Adds a new value to the existing array
clear() -> Removes all elements from the list
copy() -> Returns a copy of the list
count() -> Returns the number of elements with the specified value
extend() -> Add the elements of a list (or any iterable), to the end of the current list
index() -> Returns the index of the first element with the specified value
insert() -> Adds an element at the specified position
pop() -> Removes the element at the specified position
remove() -> Removes the first item with the specified value
reverse() -> Reverses the order of the list
sort() -> Sorts the list
Subset/Slicing -> array[start:end] Always first index is included and last is excluded
"""

print("Arrays are used to store multiple values in one single variable")
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print("=========================================================================")

print("Access the Elements of an Array")
print(f"Get the value of the first array item -> cars[0]: {cars[0]}")
cars[0] = "Toyota"
print(f"Modify the value of the first array item -> cars[0] = 'Toyota': {cars[0]}")
cars.insert(3, "Audi")
print(f"Add a value to a specific index -> cars.insert(3, 'Audi'): {cars[3]}")
print("=========================================================================")

print("The Length of an Array")
print(f"length of car's array -> len(cars): {len(cars)}")
print("=========================================================================")

print("Looping Array Elements -> for x in cars: print(x) ")
for x in cars: print(x)
print("=========================================================================")

print("Adding Array Elements")
cars.append('Honda')
print(f"Add one more element to the cars array-> cars.append('Honda'): {cars}")
cars.insert(3, 'Mercedes')
print(f"Add one more element to the cars array-> cars.insert(3, 'Mercedes'): {cars}")
print("=========================================================================")

print("Removing Array Elements")
cars.pop(0)
print(f"Delete the second element of the cars array-> cars.pop(0): {cars}")
cars.remove('Volvo')
print(f"Delete the element that has the value 'Volvo'-> cars.remove('Volvo'): {cars}")
print("=========================================================================")

print("Copy Array")
car_copy = cars.copy()
print(f"Copy array into another variable-> car_copy = cars.copy(): {car_copy}")
print("=========================================================================")

print("Count the number of elements with the specified value")
print(f"Count a value in an array-> cars.count('Ford'): {cars.count('Ford')}")
print("=========================================================================")

print("Add the elements of a list (or any iterable), to the end of the current list")
electric_cars = ["Tesla", "Rivian", "Lucid"]
cars.extend(electric_cars)
print(f"Add elements AT THE END of the list using anothr list-> cars.extend(electric_cars): {cars}")
print("=========================================================================")

print("Returns the index of the first element with the specified value")
print(f"Returns the index of the FIRST ELEMENT with the specified value-> cars.index('Tesla'): {cars.index('Tesla')}")
print("=========================================================================")

print("Sort an array")
cars.sort()
print(f"Sort array in ASCENDING order -> cars.sort(): {cars}")
cars.sort(reverse=True)
print(f"Sort array in DESCENDING order -> cars.sort(reverse=True): {cars}")
cars.reverse()
print(f"Sort array in DESCENDING order -> cars.reverse(): {cars}")
print("=========================================================================")

print("Subset/Slicing -> array[start:end]")
print(f"Array before subset -> {cars}")
print(f"In Slicing - Always FIRST INDEX is INCLUSIVE and LAST IS EXCLUDED(INDEX 5 is EXCLUDED) -> cars[1:5]: {cars[1:5]}")
print(f"In Slicing - From SELECTED INDEX(INCLUSIVE) to END -> cars[1:]: {cars[1:]}")
print(f"In Slicing - From START to SELECTED INDEX(EXCLUDED) index 4 is EXCLUDED -> cars[:4]: {cars[:4]}")
print(f"In Slicing - From length of cars to end -> len(cars):: {len(cars):}")
print("=========================================================================")

print("Navigate last element in single set array")
print(f"Array -> {cars}")
print(f"Last element in single set array-> cars.clear(): {cars[-1]}")
print("=========================================================================")

print("Clear an array")
cars.clear()
print(f"Clear an array-> cars.clear(): {cars}")
print("=========================================================================")

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Row 0: [1, 2, 3] -> index 0
Row 1: [4, 5, 6] -> index 1
Row 2: [7, 8, 9] <- index 2, also index -1

Access Pattern	Meaning	                Value
matrix[0][0]	First row, first col	1
matrix[1][2]	Second row, third col	6
matrix[2][1]	Third row, second col	8
matrix[-1][-1]	Last row, last col 🏁	9
matrix[-1][0]	Last row, first col	    7
matrix[0][-1]	First row, last col	    3
"""
print("2D Array")
matrix = [[5, 2], [1, 9], [3, 4]]
print(f"2D Array: {matrix}")
matrix.sort(key=lambda x: x[0])
print(f"2D Array sorted by first element in each row matrix.sort(key=lambda x: x[0]): {matrix}")
matrix.sort(key=lambda x: x[1])
print(f"2D Array sorted by second element in each row matrix.sort(key=lambda x: x[1]): {matrix}")
print(f"2D Array: {matrix}")
print(f"2D Array sorted access element matrix[-1]: {matrix[-1]}")
print(f"2D Array sorted access element matrix[-1][0]: {matrix[-1][0]}")
print(f"2D Array sorted access element matrix[-1][1]: {matrix[-1][1]}")
print(f"2D Array sorted access element matrix[1][-1]: {matrix[1][-1]}")
print(f"2D Array sorted access element matrix[1][-1]: {matrix[0][-1]}")
print(f"2D Array sorted access element matrix[-1][-1]: {matrix[-1][-1]}")
print("=========================================================================")

