
f = open("input_day1.txt","r")

food_items = f.readlines()
calorie_sum = 0
fattest_elfs_sorted = [0] * 3
for calorie in food_items:
    if (calorie ==  "\n"):
        if calorie_sum > fattest_elfs_sorted[0]:
            fattest_elfs_sorted[0] = calorie_sum
            fattest_elfs_sorted.sort() # Sorts in acending order
        calorie_sum = 0
    else:
        calorie_sum += int(calorie)

print('The elf carrying the most calories carries ' + str(fattest_elfs_sorted[-1]) + ' calories')

top_3_elf_sum = 0
for elf_calories in fattest_elfs_sorted:
    top_3_elf_sum += elf_calories
print('The total calorie sum of the three elves that carries the most calories is ' + str(top_3_elf_sum) + ' calories')