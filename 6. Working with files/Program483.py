"""

Write a Python program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail messages. 
The program looks for 'From' lines and takes the second
word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times 
hey appear in the file. 
After the dictionary is produced, the program reads
through the dictionary to identify the sender with the maximum count 
(the most prolific sender).

"""

file = open('6. Working with files/data/mbox-short.txt', 'r')

sender_count = {}

lines = file.readlines()

for line in lines:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1:
            email = words[1]
            sender_count[email] = sender_count.get(email, 0) + 1

file.close()

print(sender_count)

# Find sender with maximum count
max_count = 0
max_sender = None

for sender, count in sender_count.items():
    if count > max_count:
        max_count = count
        max_sender = sender


print("\n\n")
print(f"{max_sender} {max_count}")
