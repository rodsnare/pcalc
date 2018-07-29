
while True:
	user_input = input("Enter a command: ")

	if user_input == "quit":
		break
	elif user_input == "add":
		print("add")
	elif user_input == "subtract":
		print("subtract")
	elif user_input == "multiply":
		print("multiply")
	elif user_input == "divide":
		print("divide")
	elif user_input == "help":
		print("\nEnter 'add' to add two numbers")
		print("Enter 'subtract to subtract two numbers")
		print("Enter 'multiply to multiply two numbers")
		print("Enter 'divide to divide two numbers")
		print("Enter 'quit' to end the program\n")
	else:
		print("Unknown Input: Enter 'help' for help")		
