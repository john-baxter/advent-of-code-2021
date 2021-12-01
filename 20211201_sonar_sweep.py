input_text = open('20211201_sonar_sweep_input.txt')
input_list = list(input_text)
input_list = [int(strint) for strint in input_list]

refined_focus = 1
wide_focus = 3

def how_many_increases(list_of_depths, focus):
  total_increases = 0
  for i in range(1, len(list_of_depths)):
    if list_of_depths[i] > list_of_depths[i - focus]:
      total_increases += 1
      
  return total_increases

print("(1-1) The number of times the depth increases when looking with refined focus is:")
print(how_many_increases(input_list, refined_focus))
print("")
print("(1-2) The number of times the depth increases when looking with wide focus is:")
print(how_many_increases(input_list, wide_focus))
