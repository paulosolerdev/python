largest_so_far = -1

print(f'Before, largest number is: {largest_so_far}')

for the_num in [9, 41, 52, 12, 5, 7, 8, 15, 85]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(f'{largest_so_far} {the_num}')

print(f'After, largest number is: {largest_so_far}')
