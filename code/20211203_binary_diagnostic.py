"""
Setup
-----
The input data has been copied into a .txt file
Use code to convert this .txt into a list of (string) binary numbers, removing 
the trailing newline from each.
"""
input_text = open('inputs/20211203_binary_diagnostic.txt')
input_list = list(input_text)
input_list = [binary_number.rstrip("\n") for binary_number in input_list]
# input_list = [
#   "00100",
#   "11110",
#   "10110",
#   "10111",
#   "10101",
#   "01111",
#   "00111",
#   "11100",
#   "10000",
#   "11001",
#   "00010",
#   "01010",
# ]


def total_each_column(list_of_string_numbers):
  """Converts a list of numbers (as strings) and converts it into a new list containing 
  the total of each 'column' of numbers.
  
  Will be used to calculate how many '1's are in each corresponding position in the 
  diagnostic report.
  
  Assumption
  ----------
  Every number in the list has the same amount of digits.
  
  Parameters
  ----------
  (list) : list_of_string_numbers
    A list of arbitrary length contining numbers as strings
    
  Returns
  -------
  (list) : list_of_column_totals
    A list with length equivalent to the number of digits in each number. Contains the 
    total values of the sum of all digits in each corresponding position.
    Elements are integers.
  """
  # assumes all elements in list_of_string_numbers have same len(element)
  list_of_column_totals = []
  for i in range(len(list_of_string_numbers[0])):
    column_total = 0
    for string_number in list_of_string_numbers:
      column_total += int(string_number[i])
    list_of_column_totals.append(column_total)
  return list_of_column_totals


def interrogate_column_totals_gamma(list_of_ints):
  """Converts each column total to either 1 or 0 as appropriate for the 'gamma rate'
  
  References len(input_list) (from above) and if the column total is more than half, 
  that corresponding position is populated by (int) 1; if less than half, populated 
  by (int) 0
  
  Parameters
  ----------
  (list) : list_of_ints
    A list of integers, values are arbitrary.
    
  Returns
  -------
  (list) : list_of_bits
    A list of integers, values are either 0 or 1
  """
  list_of_bits = []
  for i in list_of_ints:
    if i > len(input_list) // 2:
      list_of_bits.append(1)
    if i < len(input_list) // 2:
      list_of_bits.append(0)
  return list_of_bits


def convert_list_of_bits_to_decimal_integer(list_of_bits):
  """Converts a list of bits into the corresponding decimal value
  
  Parameters
  ----------
  (list) : list_of_bits
    A list of integers, the values are 0 or 1
    
  Returns
  -------
  (int) : The integer value corresponding to the result of joining the given bits into 
  a binary integer and converting that to decimal.
  """
  return int("".join(str(bit) for bit in list_of_bits), 2)


def derive_epsilon_from_gamma(list_of_bits):
  """Converts 0 to 1, and 1 to 0 for a given list of bits
  
  Parameters
  ----------
  (list) : list_of_bits
    A list of integers, the values are 0 or 1
    
  Returns
  -------
  (list)
    A list of bits of same length as given list_of_bits, each bit has been converted 
    to its 'opposite' value
  
  """
  return [int(not bit) for bit in list_of_bits]


def get_gamma_rate(input_list):
  """Calls all relevant functions to derive the 'gamma rate' from the input list
  
  Parameters
  ----------
  (list) : input_list
    As above, the input text given by the challenge converted to binary numbers as strings
    
  Returns
  -------
  (int)
    The 'gamma rate' following the logic as per the challenge information
  """
  return convert_list_of_bits_to_decimal_integer(
    interrogate_column_totals_gamma(
      total_each_column(input_list)
    )
  )


def get_epsilon_rate(input_list):
  """Calls all relevant functions to derive the 'epsilon rate' from the input list
  
  Parameters
  ----------
  (list) : input_list
    As above, the input text given by the challenge converted to binary numbers as strings
    
  Returns
  -------
  (int)
    The 'epsilon rate' following the logic as per the challenge information
  """
  return convert_list_of_bits_to_decimal_integer(
    derive_epsilon_from_gamma(
      interrogate_column_totals_gamma(
        total_each_column(input_list)
      )
    )
  )


def calculate_power_consumption(input_list):
  """Calculates the power consumption following the logic as per the challenge 
  information by calling relevant functions, then multiplying the gamma 
  and epsilon rates
  
  Parameters
  ----------
  (list) : input_list
    As above, the input text given by the challenge converted to binary numbers as strings
    
  Returns
  -------
  (int)
  The 'power consumption' following the logic as per the challenge information
  """
  return get_gamma_rate(input_list) * get_epsilon_rate(input_list)


def calculate_oxygen_rating(given_list):
  for i in range(len(given_list[0])):
    dominant_digit_for_column_i = int((sum([int(element[i]) for element in given_list]) >= len(given_list) / 2))
    given_list = [element for element in given_list if int(element[i]) == dominant_digit_for_column_i]
    if len(given_list) == 1:
      return given_list[0]
    
  
def calculate_carbon_dioxide_rating(given_list):  
  for i in range(len(given_list[0])):
    non_dominant_digit_for_column_i = int((sum([int(element[i]) for element in given_list]) < len(given_list) / 2))
    given_list = [element for element in given_list if int(element[i]) == non_dominant_digit_for_column_i]
    if len(given_list) == 1:
      return given_list[0]
    
    
def calculate_life_support_rating(given_list):
  return int(calculate_oxygen_rating(given_list), 2) * int(calculate_carbon_dioxide_rating(given_list), 2)

  
"""
Print statements to display solutions
-------------------------------------
"""
print("(3-1) The power consumption is:")
print(calculate_power_consumption(input_list))
print()
print("(3-2) The life support rating is:")
print(calculate_life_support_rating(input_list))
