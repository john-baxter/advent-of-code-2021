input_text = open('inputs/20211206_lanternfish_input.txt', 'r')
input_string = input_text.read()
input_list = [int(i) for i in input_string.split(',')]


new_parent_status = 6
baby_lanternfish_status = 8
days_to_simulate_part_one = 80
days_to_simulate_part_two = 256


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
    print(day)
    lanternfish_list = process_one_day_of_lanternfish_reproduction(lanternfish_list)
  return len(lanternfish_list)


lanternfish_life_stage_tally_list = [0 for i in range(9)]
for fish in input_list:
  lanternfish_life_stage_tally_list[fish] += 1
  

def update_tally_list_for_one_day(tally_list):
  placeholder_for_idx_0 = tally_list[0]
  tally_list = tally_list[1:]
  tally_list.append(placeholder_for_idx_0)
  tally_list[6] += placeholder_for_idx_0
  return tally_list


def simulate_life_cycle_propagation_of_lanternfish(tally_list, days_in_simulation):
  for i in range(days_in_simulation):
    tally_list = update_tally_list_for_one_day(tally_list)
  return sum(tally_list)


print(simulate_life_cycle_propagation_of_lanternfish(lanternfish_life_stage_tally_list, 256))
