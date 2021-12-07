from collections import Counter
from datetime import datetime


input_text = open('inputs/20211207_the_treachery_of_whales_input.txt', 'r')
input_string = input_text.read()
input_list = [int(i) for i in input_string.split(',')]
input_counter = Counter(input_list)


def get_range_of_crab_distribution(list_of_crabs):
  low_end = min(list_of_crabs)
  high_end = max(list_of_crabs)
  return range(low_end, high_end + 1, 1)


def get_fuel_consumption_for_single_position_in_range(position, counter_of_crabs):
  fuel_used = 0
  for key, value in counter_of_crabs.items():
    fuel_used += abs(position - key) * value
  return fuel_used


def get_fuel_consumption_for_all_positions_in_range(list_of_crabs, counter_of_crabs):
  fuel_used_list = []
  list_of_possible_crab_positions = list(get_range_of_crab_distribution(list_of_crabs))
  for crab in list_of_possible_crab_positions:
    fuel_used_list.append(get_fuel_consumption_for_single_position_in_range(
      crab, counter_of_crabs
    ))
  return min(fuel_used_list)
  

def get_n_th_triangular_number(n):
  triangular_number = 0
  for i in range(1, n+1):
    triangular_number += i
  return triangular_number


def get_increased_fuel_consumption_for_single_position_in_range(position, counter_of_crabs):
  fuel_used = 0
  for key, value in counter_of_crabs.items():
    absolute_value_of_positional_difference = abs(position - key)
    fuel_used += get_n_th_triangular_number(absolute_value_of_positional_difference) * value
  return fuel_used


def get_increased_fuel_consumption_for_all_positions_in_range(list_of_crabs, counter_of_crabs):
  fuel_used_list = []
  list_of_possible_crab_positions = list(get_range_of_crab_distribution(list_of_crabs))
  for crab in list_of_possible_crab_positions:
    fuel_used_list.append(get_increased_fuel_consumption_for_single_position_in_range(
      crab, counter_of_crabs
    ))
  return min(fuel_used_list)


solution_7_1 = get_increased_fuel_consumption_for_all_positions_in_range(input_list, input_counter)
solution_7_2 = get_fuel_consumption_for_all_positions_in_range(input_list, input_counter)


"""
Print statements to display solutions
-------------------------------------
"""
print("(7-1) The assumed fuel consumption for all crabs to get into position is:")
print(solution_2_1)
print("")
print("(7-2) The actual (after recalculation) fuel consumption is:")
print(solution_2_2)
