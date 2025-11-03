"""

Given a string S containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

"""

str = input("Enter a string: ")

last = []

for i in str:

    if i == '(':
        last.append('(')

    elif i == '{':
        last.append('{')

    elif i == '[':
        last.append('[')


    elif i == ')':

        if last.pop() != '(':
            print("Invalid.")
            break

    elif i == '}':

        if last.pop() != '{':
            print("Invalid.")
            break

    elif i == ']':

        if last.pop() != '[':
            print("Invalid.")
            break
    
else:
    
    if len(last) == 0:
        print("Valid.")
    else:
        print("Invalid.")