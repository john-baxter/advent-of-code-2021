import numpy as np
from giant_squid_test_input import bingo_numbers, bingo_card_1, bingo_card_2, bingo_card_3

all_bingo_cards = [
  bingo_card_1,
  bingo_card_2,
  bingo_card_3,
]

# input_text = open('inputs/20211204_giant_squid_test_input.txt')

# with open('inputs/20211204_giant_squid_test_input.txt', "r") as file:
#   # bingo_numbers = list(file.readline())
#   # bingo_numbers = (file.readline()).split(",")
#   bingo_numbers = [int(i) for i in file.readline().split(",")]
  
# array_from_file = np.loadtxt('inputs/20211204_giant_squid_test_input.txt', dtype=str)
# array_from_file = np.genfromtxt('inputs/20211204_giant_squid_test_input.txt', dtype=str)

# with open('inputs/20211204_giant_squid_test_input.txt', "r") as file:
#   lines = (line for line in file if not line.startswith('\n'))
#   FH = np.loadtxt(lines, delimiter=',', skiprows=1)



def check_if_bingo(bingo_card):
  return check_rows_for_bingo(bingo_card) or check_columns_for_bingo(bingo_card)


def check_rows_for_bingo(bingo_card):
  bingo_status = True
  for row in bingo_card:
    if 'X' not in row:
      bingo_status = False
  return bingo_status


def check_columns_for_bingo(bingo_card):
  return check_rows_for_bingo(bingo_card.T)


def calculate_score_from_card(bingo_card):
  card_total = 0
  for row in bingo_card:
    for number in row:
      try:
        card_total += int(number)
      except:
        card_total += 0
  return card_total


def replace_called_number_with_X(bingo_card, called_number):
  return np.where(bingo_card == called_number, 'X', bingo_card)


def mark_called_number_in_all_cards(called_number, all_bingo_cards):
  for i in range(len(all_bingo_cards)):
    if called_number in all_bingo_cards[i]:
      all_bingo_cards[i] = replace_called_number_with_X(all_bingo_cards[i], called_number)
  return all_bingo_cards


def calculate_final_score(bingo_card, called_number):
  return calculate_score_from_card(bingo_card) * called_number


def call_each_number_in_turn_and_mark_cards(list_of_numbers, list_of_cards):
  for i in range(len(list_of_numbers)):
    mark_called_number_in_all_cards(list_of_numbers[i], list_of_cards)
  return list_of_cards


def check_all_cards_for_bingo(list_of_cards):
  for card in list_of_cards:
    if check_if_bingo(card):
      return card
    else:
      pass
    
    
def beat_squid_at_bingo(list_of_cards, list_of_numbers):
  winning_card = None
  for i in range(len(list_of_numbers)):
    list_of_numbers = mark_called_number_in_all_cards(list_of_numbers[i], list_of_cards)
    try:
      winning_card = check_all_cards_for_bingo(list_of_cards)
    except:
      continue
    if winning_card is not None:
      winning_score = calculate_final_score(winning_card, int(list_of_numbers[i]))
      return winning_score
      # return calculate_final_score(winning_card, list_of_numbers[i])



print(beat_squid_at_bingo(all_bingo_cards, bingo_numbers))
# print(
#   calculate_final_score(
#     replace_called_number_with_X(
#       bingo_card_1, 13
#     ), 10
#   )
# )
# print(
#   calculate_score_from_card(
#     replace_called_number_with_X(
#       bingo_card_1, 13
#     )
#   )
# )
# print(len(all_bingo_cards))
# print(mark_called_number_in_all_cards(13, all_bingo_cards))
# print(13 in bingo_card_1)
# print(replace_called_number_with_X(bingo_card_1, 13))
# print(13 in bingo_card_1)
# print(replaced_called_number_with_X(bingo_card_1, 22))
