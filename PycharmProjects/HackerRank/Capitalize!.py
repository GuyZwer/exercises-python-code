# Enter your code here. Read input from STDIN. Print output to STDOUT
list1 = map(str, raw_input().split(' '))
new_string = ''
for word in list1:
    word = word.capitalize()
    if word == '':
        new_string += ' '
    else:
        new_string += word + ' '

print new_string[0:-1]