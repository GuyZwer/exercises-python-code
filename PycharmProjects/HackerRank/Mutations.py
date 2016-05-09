string = str(raw_input())
character = raw_input().split()
number = int(character[0])
letters = character[1]

new_string = string[:number] + str(letters) + string[number+1:]
print new_string