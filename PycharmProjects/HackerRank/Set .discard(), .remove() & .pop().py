n = input()
s = set(map(int, raw_input().split()))

command_number = int(raw_input())
for loop in range(command_number):
    input_command = raw_input().split()
    make_a_command = str("s.") + str(input_command[0])
    try:
        make_a_command += "(" + str(input_command[1]) + ")"
    except IndexError:
        make_a_command = str("s.") + str(input_command[0]) + "()"
    exec make_a_command

print sum(list(s))


