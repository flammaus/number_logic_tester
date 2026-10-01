#Converts numbers to binary/hex, then builds truth tables for logic gates
#***CDA 3103C Test Project***



#***NUMBER CONVERTER***

#Numbers im testing converter on, change to test different ones
numbers_to_convert = [13, 42, 255, 8]

print("***NUMBER CONVERTER***")
for num in numbers_to_convert:
    #Format() is converting, 'b' = binary, 'x' = hex
    binary_version = format(num, 'b')
    hex_version = format(num, 'x')
    print(f"{num} -> binary: {binary_version}, hex: {hex_version}")

print()

#***LOGIC GATES***
#A gate just takes 1s and 0s (on/off) and spits out a 1 or 0 based on a rule
#Going through every possible combo of two inputs below (0+0, 0+1, 1+0, 1+1) to see the full truth table

print("***LOGIC GATE TRUTH TABLES***")

print("\nAND gate (output is 1 only if both inputs are 1):")
for a in [0, 1]:
    for b in [0, 1]:
        #Python has "and"/"or" built in
        if a and b:
            result = 1
        else:
            result = 0
        print(f"  {a} AND {b} = {result}")

print("\nOR gate (output is 1 if either input is 1):")
for a in [0, 1]:
    for b in [0, 1]:
        if a or b:
            result = 1
        else:
            result = 0
        print(f"  {a} OR {b} = {result}")

#XOR = "two inputs are different", so != (not equal) is the same
print("\nXOR gate (output is 1 only if the inputs are different from each other):")
for a in [0, 1]:
    for b in [0, 1]:
        if a != b:
            result = 1
        else:
            result = 0
        print(f"  {a} XOR {b} = {result}")

print("\nNOT gate (only takes one input, just flips it):")
for a in [0, 1]:
    if a == 0:
        result = 1
    else:
        result = 0
    print(f"  NOT {a} = {result}")
