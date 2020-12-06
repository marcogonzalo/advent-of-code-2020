import os
import sys
import math

constants = {
    "MAX_COLUMN": 7,
    "MAX_ROW": 127
}


def calc_seat_id(bp):
    row, column = process_boarding_pass(bp)
    return eval(f'{row} * 8 + {column}')

def calc_lower_limit(lower, higher):
    return math.ceil(lower + (higher - lower) / 2)

def calc_higher_limit(lower, higher):
    return math.floor(higher - (higher - lower) / 2)

def process_boarding_pass(bp):
    front_row = 0
    back_row = constants['MAX_ROW']
    left_column = 0
    right_column = constants['MAX_COLUMN']
    row = 0
    column = 0
    for l in bp:
        if l == 'F':
            front_row = front_row
            back_row = calc_higher_limit(front_row, back_row)
        elif l == 'B':
            front_row = calc_lower_limit(front_row, back_row)
            back_row = back_row
        elif l == 'L':
            left_column = left_column
            right_column = calc_higher_limit(left_column, right_column)
        elif l == 'R':
            left_column = calc_lower_limit(left_column, right_column)
            right_column = right_column
    return front_row, left_column


dirname = os.path.dirname(os.path.realpath(__file__))
f = open(dirname + "/input.txt", "r")
highest_seat_id = 0
lowest_seat_id = sys.maxsize
seats = []
for l in f.readlines():
    seat_id = calc_seat_id(l.strip())
    seats.append(seat_id)
    if seat_id > highest_seat_id: highest_seat_id = seat_id
    if seat_id < lowest_seat_id: lowest_seat_id = seat_id

print("Min seat id:",lowest_seat_id)
print("Max seat id:",highest_seat_id)

print("My seat is", [x for x in range(lowest_seat_id, highest_seat_id + 1) if x not in seats])
