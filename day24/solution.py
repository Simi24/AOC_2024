from collections import defaultdict

initial_port_state = defaultdict(str)
operations = []


def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.__contains__(":"):
                _port = line.split(":")
                initial_port_state[_port[0]] = int(_port[1].strip())
            elif line.__contains__("->"):
                _operation = line.split("->")
                operations.append((_operation[0].strip().split(), _operation[1].strip()))

    print(initial_port_state)
    print(operations)


def AND(input1, input2):
    return 1 if input1 == 1 and input2 == 1 else 0


def OR(input1, input2):
    return 1 if input1 == 1 or input2 == 1 else 0


def XOR(input1, input2):
    return 1 if input1 != input2 else 0


def solve(operations, initial_port_state):
    while operations:
        for operation in operations:
            if operation[0][0] in initial_port_state and operation[0][2] in initial_port_state:
                res = 0
                if operation[0][1] == "AND":
                    res = AND(initial_port_state[operation[0][0]], initial_port_state[operation[0][2]])
                elif operation[0][1] == "OR":
                    res = OR(initial_port_state[operation[0][0]], initial_port_state[operation[0][2]])
                elif operation[0][1] == "XOR":
                    res = XOR(initial_port_state[operation[0][0]], initial_port_state[operation[0][2]])

                initial_port_state[operation[1]] = res
                operations.remove(operation)


def main():
    parse_input()
    solve(operations, initial_port_state)
    res = ""
    final_ports = []
    for key, value in initial_port_state.items():
        if key.startswith("z"):
            final_ports.append((key, value))

    final_ports.sort(reverse=True)
    for port in final_ports:
        res += str(port[1])

    print(res)
    print(int(res, 2))


if __name__ == "__main__":
    main()
