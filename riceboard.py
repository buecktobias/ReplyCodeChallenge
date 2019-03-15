import os

# VARIABLES
INPUT_FILENAME = "input-riceboard-8c95"
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


def pow_of_2_exp_mod(base, exp, mod):
    if exp == 1:
        return base % mod

    # a^b % c = (a^(b/2) % c * a^(b/2) % c) % c
    part_mod = pow_of_2_exp_mod(base, int(exp / 2), mod)
    return (part_mod * part_mod) % mod


results = []

# Assume that M (mod) is a prime (https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
T = int(input_file_list[0])
for i in range(T):
    R, N, M = [int(x) for x in input_file_list[i + 1].split(" ")]
    exponent = N * N
    # a^(p-1) % p = 1
    # reduce the exponent by M-1 (p-1) 's
    exponent %= (M - 1)

    # https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation
    binary_exp = bin(exponent)[2:]
    binary_exp_len = len(binary_exp)

    exponents = [2 ** k for k in range(binary_exp_len) if int(binary_exp[binary_exp_len - 1 - k]) == 1]

    mod_product = 1
    for exp in exponents:
        mod_product *= pow_of_2_exp_mod(R, exp, M)
    rest = mod_product % M
    results.append(rest - 1 if rest != 0 else M - 1)

# PROCESS

output_list = []
for i in range(len(results)):
    output_list.append("".join(f"Case #{i + 1}: {results[i]} \n"))  # Case #1: result ...
output = "".join(output_list)

# OUTPUT

output_file = open(file=OUTPUT_FILE_PATH, mode=WRITE_MODE)
output_file.write(output)
output_file.close()
