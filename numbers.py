numbers = input()
number_list = list(numbers)
number_list = numbers.split(' ')
number_list = [int(numbers) for numbers in number_list]
print(sum(number_list), max(number_list), min(number_list))