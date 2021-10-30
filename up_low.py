# Write a function that accept a string and caculates the number of upper case letters and lower case letters.
def up_low(str):
    count_upper = 0
    count_lower = 0

    for char in str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        else:
            pass
    print(f'upper case count:{count_upper}')
    print(f'lower case count:{count_lower}')


up_low('Hello, Jiyun Kim')
