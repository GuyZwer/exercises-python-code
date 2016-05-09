s1 = raw_input()
swap_str = ''
for letter in s1:
    if letter == letter.lower():
        swap_str += letter.upper()
    elif letter == letter.upper():
        swap_str += letter.lower()
    else:
        swap_str += letter


print swap_str

