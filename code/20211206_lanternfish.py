input_text = open('inputs/20211206_lanternfish_input.txt', 'r')
input_string = input_text.read()
input_list = [int(i) for i in input_string.split(',')]


new_parent_status = 6
baby_lanternfish_status = 8
days_to_simulate = 80


def propagate_lanternfish(lanternfish_list):
  for proagation_status in lanternfish_list:
    if proagation_status == 0:
      lanternfish_list.append(baby_lanternfish_status + 1)
  return lanternfish_list


def reset_internal_timer_for_new_lanternfish_parents(lanternfish_list):
  return [new_parent_status + 1 if i == 0 else i for i in lanternfish_list]


def decrement_each_lanternfish_status(lanternfish_list):
  return [i - 1 for i in lanternfish_list]


def process_one_day_of_lanternfish_reproduction(lanternfish_list):
  lanternfish_list = propagate_lanternfish(lanternfish_list)
  lanternfish_list = reset_internal_timer_for_new_lanternfish_parents(lanternfish_list)
  lanternfish_list = decrement_each_lanternfish_status(lanternfish_list)
  return lanternfish_list


def count_lanternfish_after_x_days(lanternfish_list, days):
  for day in range(days):
    lanternfish_list = process_one_day_of_lanternfish_reproduction(lanternfish_list)
  return len(lanternfish_list)


print(count_lanternfish_after_x_days(input_list, days_to_simulate))
