file_path = 'day1.txt'

with open(file_path, 'r') as file:
    crazy_list = file.readlines()

final_numbers = []

my_numbers = ''

for line in crazy_list:
    for char in line:
        if char.isdigit():
            my_numbers += char
    final_numbers.append(my_numbers)
    my_numbers = ''
    string_holder = ''

print(final_numbers)

final_sum = 0

for element in final_numbers:
    string_holder = ''
    string_holder += element[0] + element[-1]
    final_sum += int(string_holder)
    print(final_sum)
    print(int(string_holder))

print(final_sum)