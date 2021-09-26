# Organizing a List

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort this list in reverse alphabetically order by passing the argument reverse=True to the sort() method. 
# Again, the order of the list is permanently changed.
cars =['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printinga List in Reverse Order
# The reverse() doesn't sort backward alphabetically; it simply reverse the order of the list;
# The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
cars =['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the Length of a List
cars =['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))