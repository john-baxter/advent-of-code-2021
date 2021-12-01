input_text = open('20211201_1_sonar_sweep_input.txt')
input_list = list(input_text)
input_list = [int(strint) for strint in input_list]

def how_many_increases(list_of_depths):
  total_increases = 0
  for i in range(1, len(list_of_depths)):
    if list_of_depths[i] > list_of_depths[i-1]:
      total_increases += 1
      
  return total_increases

print(how_many_increases(input_list))
