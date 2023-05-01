def sum_even_numbers(my_list):
    sum = 0
    for num in my_list:
        if num % 2 == 0:
            sum += num
    return sum

if __name__ == "__main__":
    my_list = [4,3,8,7,9,10,11,5,2]
    answer = sum_even_numbers(my_list)
    print(f"The sum of even numbers in {my_list} is: {answer}")