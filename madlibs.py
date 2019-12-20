print("Mad Libs where libs get mad.\n")
print("Start below:\n\n")

time = input("Eter a number from 1 to 12: ")
items = input("Enter a noun (plural): ")
name =  input("Enter a name: ")
scream = input("Enter any sentence: ")
action = input("Enter a verb: ")

print(""" 
The story goes...

It was {} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {} with a note saying "From Mr. {}."
Just as I closed the door I heard a scream "{}"
I froze in place and all I could do was {}. 
""".format (time, items, name.title(), scream.upper(), action))
