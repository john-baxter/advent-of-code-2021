from collections import Counter
"""
Solution to part one
--------------------
The input data has been copied into a .txt file
Use code to manipulate this .txt into a list of 'instructions'.
  Each instruction is a 2-element list
    element[0] is the direction as a string
    element[1] is the distance moved in that direction as an integer
Then iterate through this list and collect the data in a Counter, which will contain 
the total distances for each instruction.
Then use these values to perform the final calculation asked for in the challenge
"""

input_text = open('20211202_dive_input.txt')
input_list = list(input_text)
instruction_list = [instruction.split(" ") for instruction in input_list]

for instruction in instruction_list:
  instruction[1] = int(instruction[1])

instruction_count = Counter()
for instruction in instruction_list:
  instruction_count[instruction[0]] += instruction[1]
  
depth = instruction_count['down'] - instruction_count['up']

print("(2-1) The depth multiplied by the forward distance is:")
print(instruction_count['forward'] * depth)

"""
Solution to part two
--------------------
Set new variables, each equal to 0:
  (int) : aim 
  (int) : depth
  (int) : horizontal

Iterate through (list) instruction_list (as above) and change the relevant variables as described in the instructions.

Use the final values of horizontal and depth to perform the required calculation.
"""

aim = 0
depth = 0
horizontal = 0
for instruction in instruction_list:
  if instruction[0] == 'down':
    aim += instruction[1]
  if instruction[0] == 'up':
    aim -= instruction[1]
  if instruction[0] == 'forward':
    horizontal += instruction[1]
    depth += (aim * instruction[1])

print("")
print("(2-2) The final horizontal position multiplied by the final depth is:")
print(horizontal * depth)
