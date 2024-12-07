import re


if __name__ == "__main__":
    with open('day3.txt', 'r') as fp:
        program: str = fp.read()
    # print(program)
    pattern = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'

    sum = 0

    is_multiply_enabled = True
    for instruction in re.findall(pattern, program):
        if is_multiply_enabled and instruction.startswith('mul'):
            match = re.match(r'^mul\(([0-9]+),([0-9]+)\)$', instruction)
            if match is not None:
                a, b = int(match.group(1)), int(match.group(2))
                sum += a * b
                # print(match.group(1), match.group(2))

        if instruction.startswith('do'):
            is_multiply_enabled = instruction == 'do()'

    print(sum)
