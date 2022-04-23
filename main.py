"""Two sums - Matthew Imamura

tags: Algorithm, math"""

print("This program asks the user for a target and looks for all the possible")
print("pairs of variable that sums up to that value.")

"Creates the array of values that will be add together to get the target"
nums = [1, 2, 3, 4, 5]
print(nums)

"Asks the user for the target"
print("Input a target amount between 3 - 10")
target = input('> ')
target = int(target)

"Adds all the numbers together and print out the values that equals to the target"

# base_num is the first number that will be added to all the other numbers
for base_num in nums:
    # second num will go through all the numbers and add it to the base_num
    for second_num in nums:
        if second_num == 5:
            break
        number1 = nums[int(base_num - 1)]
        number2 = nums[int(second_num)]
        answer = number1 + number2
        if answer == target:
            print(number1, number2)
