"""
Setup
-----
The input data has been copied into a .txt file
Use code to manipulate this .txt into a list of (int) depth values.

Set new variables, each showing the number of depth values to include in calculation 
based on what version of the challenge is being solved:
  (int) : refined_focus = 1 used for challenge 1-1
  (int) : wide_focus = 3 used for challenge 1-2
"""

input_text = open('inputs/20211201_sonar_sweep_input.txt')
input_list = list(input_text)
input_list = [int(strint) for strint in input_list]

refined_focus = 1
wide_focus = 3

def how_many_increases(list_of_depths, focus):
  """Uses the data from the input file and the focus variable to calculate the number 
  of times the depth increases.
  
  Parameters
  ----------
  (list) : list_of_depths
    The list of depth measurements derived from the input .txt file
    
  (int) : focus
    How many depth measurements are being considered during each iteration
    
  Returns
  -------
  (int) : total increases
    The total number of times the depth increased
    
  Notes
  -----
  In the example of the wide focus, the 'middle' two values can be ignored and the 
  same solution can be obtained via a direct comparison between the 'first' and the 
  'last' value. eg:
  
  index:  depth:    window:
  0       199       A      
  1       200       A B
  2       208       A B
  3       210         B
  4       200
  
  Since elements [1] and [2] are included in both A & B, there is no need to include 
  these in the calculation. The result is the same as a direct comparison between 
  elements [0] and [3], so the calculation is done using this simplification.
  """
  total_increases = 0
  for i in range(1, len(list_of_depths)):
    if list_of_depths[i] > list_of_depths[i - focus]:
      total_increases += 1
      
  return total_increases

"""
Print statements to display solutions
-------------------------------------
"""
print("(1-1) The number of times the depth increases when looking with refined focus is:")
print(how_many_increases(input_list, refined_focus))
print("")
print("(1-2) The number of times the depth increases when looking with wide focus is:")
print(how_many_increases(input_list, wide_focus))
