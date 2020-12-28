import StackImplementation

plates = StackImplementation.Stack()
print(f"is_empty should return True.\nResult:{plates.is_empty()}")
#Adding items 
plates.push(5)
plates.push(4)
plates.push(3)

print("")
print("We have added some plates to our stack")
print("")

print(f"size should return 3. \nResult:{plates.size()}")
print(f"is_empty should return False.\nResult:{plates.is_empty()}")
print(f"peek should return 3.\nResult:{plates.peek()}")

print("")
print("Next we're going to remove and add some stuff to the stack")
print("")

plates.pop()
plates.pop()
plates.push(2)
plates.push(1)
plates.pop()
plates.push(0)

print(f"size should return 3. \nResult:{plates.size()}")
print(f"is_empty should return False.\nResult:{plates.is_empty()}")
print(f"peek should return 0.\nResult:{plates.peek()}")

print("")
print("Next we'll clear the list")
print("")

plates.pop()
plates.pop()
plates.pop()

print(f"size should return Stack Empty.\nResult:{plates.size()}")
print(f"is_empty should return True.\nResult:{plates.is_empty()}")