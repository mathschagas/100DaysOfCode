import art
# Clearing the console in python has different methods for different Operating Systems.
# In Windows: For clearing the console in the windows operating system, we can use the system() function from the os module with the 'cls' parameter.
import os
def clear():
    os.system('cls')

print(art.logo)
print("Welcome to the secret auction program.")
secret_auction = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    secret_auction[name] = bid
    if (input("Are there any other bidders? Type 'yes' or 'no'. ") != "yes"):
        should_continue = False
    clear()

highest_bid = 0
highest_bid_person = ""
for person in secret_auction:
    if int(secret_auction[person]) > highest_bid:
        highest_bid = int(secret_auction[person])
        highest_bid_person = person

print(f"The winner is {highest_bid_person} with a bid of ${highest_bid}")