import os
from dataclasses import dataclass


@dataclass
class Portal:
    in_x: int
    in_y: int
    out_x: int
    out_y: int


# VARIABLES
INPUT_FILENAME = "input-teleportation-4f57"
OUTPUT_FILENAME = f"output-{INPUT_FILENAME}"

INPUTS_DIRECTORY = "Input_Files"
OUTPUTS_DIRECTORY = "Output_Files"

INPUT_FILE_TYPE = "txt"
OUTPUT_FILE_TYPE = "txt"

INPUT_FILE_PATH = f"{INPUTS_DIRECTORY}{os.sep}{INPUT_FILENAME}.{INPUT_FILE_TYPE}"
OUTPUT_FILE_PATH = f"{OUTPUTS_DIRECTORY}{os.sep}{OUTPUT_FILENAME}.{OUTPUT_FILE_TYPE}"

# INPUT

input_file = open(file=INPUT_FILE_PATH, mode="r")
input_file_list = list(input_file.read().split("\n"))
input_file.close()

# PROCESS


def calculate_distance(x1:int, y1:int, x2:int, y2:int):
    x_difference = abs(x2-x1)
    y_difference = abs(y2-y1)
    difference = x_difference + y_difference
    return difference


def find_nearest_portal(start_x: int, start_y: int):
    smallest_difference:int = 9999999999999999999999999999999999
    best_portal_so_far: Portal = None
    for portal in portals:
        difference = calculate_distance(int(start_x), int(start_y), int(portal.in_x), int(portal.in_y))
        if difference < smallest_difference:
            smallest_difference = difference
            best_portal_so_far = portal
        # elif difference == smallest_difference:
        #     if portal.in_x < best_portal_so_far.in_x:
        #         smallest_difference = difference
        #         best_portal_so_far = portal
        #     elif portal.in_x == best_portal_so_far.in_x:
        #         if portal.in_y < best_portal_so_far.in_y:
        #             smallest_difference = difference
        #             best_portal_so_far = portal
    assert smallest_difference != 9999999999999999999999999999999999
    return smallest_difference, best_portal_so_far


results = []

case_amount = int(input_file_list[0])
line_index = 1
for case in range(case_amount):
    rest = 0
    portals = []
    sum_of_differences = 0
    smallest_difference = 0
    grid_size = [int(x) for x in input_file_list[line_index].split(" ")]
    assert len(grid_size) == 2
    line_index += 1
    start_x, start_y = [int(x) for x in input_file_list[line_index].split(" ")]
    assert grid_size[0] > start_x >= 0 and grid_size[1] > start_y >= 0
    line_index += 1
    current_x, current_y = start_x, start_y

    number_of_portals = int(input_file_list[line_index])
    line_index += 1
    # portals
    for i in range(0, number_of_portals):
        portals.append(Portal(*input_file_list[line_index].split(" ")))
        line_index += 1

    while len(portals) > 0:
        portals.sort(key=lambda portal: (portal.in_x, portal.in_y))
        smallest_difference, best_portal = find_nearest_portal(current_x, current_y)
        sum_of_differences += smallest_difference
        current_x = best_portal.out_x
        current_y = best_portal.out_y
        portals.remove(best_portal)
    rest = sum_of_differences % 100_003
    results.append(rest)
# OUTPUT

output_list = []
for i in range(len(results)):
    output_list.append("".join(f"Case #{i + 1}: {results[i]} \n"))  # Case #1: result ...
output = "".join(output_list)

# OUTPUT

output_file = open(file=OUTPUT_FILE_PATH, mode="w")
output_file.write(output)
output_file.close()
