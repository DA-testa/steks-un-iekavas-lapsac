# python3
# Lauma Gailite 221RDB389 1. kurss 2. grupa. Uz Visual studio code kods strada, GitHub met erroru ~
# pielauju ka nesapass ar Workflow requirements (?), bet uzdevuma del neko nemainiju.
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            #pass
        elif next in ")]}":
            if not opening_brackets_stack:
                return i+1
        last = opening_brackets_stack.pop()
        if not are_matching(last.char, next):
            return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"
            # Process closing bracket, write your code here
            #pass

def main():
    choice = input("Choose files or input - F or I : ")
    
    if choice == "F":
        fails = input("Input / paste file path: ")
        with open(fails, "r") as file:
            text = file.read()
    elif choice == "I":
        text = input("Input brackets: ")
    else:
        print(" ")
        return
    
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)
        
if __name__ == "__main__":
    main()
