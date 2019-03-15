import os

# VARIABLES
INPUT_FILENAME = "input-password-aba8"
OUTPUT_FILENAME = f"output-{INPUT_FILENAME}"

INPUTS_DIRECTORY = "Input_Files"
OUTPUTS_DIRECTORY = "Output_Files"

INPUT_FILE_TYPE = "txt"
OUTPUT_FILE_TYPE = "txt"

READ_MODE = 'r'
WRITE_MODE = 'w'

INPUT_FILE_PATH = f"{INPUTS_DIRECTORY}{os.sep}{INPUT_FILENAME}.{INPUT_FILE_TYPE}"
OUTPUT_FILE_PATH = f"{OUTPUTS_DIRECTORY}{os.sep}{OUTPUT_FILENAME}.{OUTPUT_FILE_TYPE}"

# INPUT

input_file = open(file=INPUT_FILE_PATH, mode=READ_MODE)
input_file_list = list(input_file.readlines())
input_file.close()

# PROCESS
results = []
amount_cases: int = int(input_file_list[0])
for case in range(amount_cases):
    count = 0
    N, M = [int(x) for x in input_file_list[case * 2 + 1].split(" ")]
    if M > N:
        results.append(2 ** N)
        continue
    sequence: str = input_file_list[case*2 + 2].strip()
    for i in range(2 ** N):
        # while len(binary) < N:
        #     binary = "0" + binary
        binary = format(i, f'0{N}b')
        if sequence not in binary:
            count += 1
    results.append(count)


output_list = []
for i in range(len(results)):
    output_list.append("".join(f"Case #{i + 1}: {results[i]} \n"))  # Case #1: result ...
output = "".join(output_list)

# OUTPUT

output_file = open(file=OUTPUT_FILE_PATH, mode=WRITE_MODE)
output_file.write(output)
output_file.close()
