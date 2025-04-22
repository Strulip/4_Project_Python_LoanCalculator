# Python code to greet a friend in a unique way

# Function to create a greeting for a friend
def create_greeting(friend_name, favorite_drink):
    # Write your code here to format the string. 
    # Make sure to capitalize the first letter of both 'friend_name' and 'favorite_drink'.
    return (f'Hello {name_input.capitalize()}, I hope you are having a wonderful day! '
            f'Would you like a glass of {drink_input.capitalize()}?')

# Taking user's input
name_input = input()
drink_input = input()

# Call function and print the greeting
print(create_greeting(name_input, drink_input))