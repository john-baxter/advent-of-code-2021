input_text = open('inputs/20211203_binary_diagnostic_test.txt')
# input_text = open('inputs/20211203_binary_diagnostic.txt')
input_list = list(input_text)
input_list = [binary_number.rstrip("\n") for binary_number in input_list]

# print(input_list)

def total_each_column(list_of_string_numbers):
  # assumes all elements in list_of_string_numbers have same len(element)
  list_of_column_totals = []
  for i in range(len(list_of_string_numbers[0])):
    column_total = 0
    for string_number in list_of_string_numbers:
      column_total += int(string_number[i])
    list_of_column_totals.append(column_total)
  return list_of_column_totals


def interrogate_column_totals_gamma(list_of_ints):
  list_of_bits = []
  for i in list_of_ints:
    if i > len(input_list) // 2:
      list_of_bits.append(1)
    if i < len(input_list) // 2:
      list_of_bits.append(0)
  return list_of_bits
        

print(interrogate_column_totals_gamma(
  total_each_column(input_list)))    
# print(total_each_column(input_list))