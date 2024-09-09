#ex1

pizzaSlices: int = int(input("Please enter number of the pizza slices:\n"));

print(f"For {pizzaSlices} pizza slices, each friend get {pizzaSlices//4} and {pizzaSlices%4} slices left")

#ex2

friends: int = int(input("Please enter number of the danny's friends:\n"));

pizzaSlices: int = int(input("Please enter number of the pizza slices:\n"));

print(f"For {pizzaSlices} pizza slices, each friend get {pizzaSlices//friends} and {pizzaSlices%friends} slices left")