from calendar import month_name


def return_10():
    return 10

def add(num_01, num_02):
    return num_01 + num_02

add_result = add(1, 2)

def subtract(num_01, num_02):
    return num_01 - num_02

subtract_result = subtract(10, 5)

def multiply(num_01, num_02):
    return num_01 * num_02

multiply_result = multiply(4, 2)

def divide(num_01, num_02):
    return num_01 / num_02

divide_result = divide(10, 2)

def length_of_string(test_string):
    return len(test_string)

string_length = length_of_string("A string of length 21")
    
def join_string(string1, string2):
    return string1 + string2

joined_string = join_string("Mary had a little lamb, ", "its fleece was white as snow")

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

add_result = add_string_as_number("1", "2")

month_names = {
    1: ["January", "Jan"],
    2: "February",
    3: ["March", "Mar"],
    4: ["April", "Apr"],
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: ["September", "Sept"],
    10: ["October", "Oct"],
    11: "November",
    12: "December"
}

def number_to_full_month_name(month_number):
    return month_names[month_number][0]

result = number_to_full_month_name(1)

result = number_to_full_month_name(3) 

result = number_to_full_month_name(9)

def number_to_short_month_name(month_number):
    return month_names[month_number][1]

result = number_to_short_month_name(1)

result = number_to_short_month_name(4)

result = number_to_short_month_name(10)

def find_volume_of_cube(length_of_side):
    return length_of_side * length_of_side  * length_of_side

volume_of_cube = find_volume_of_cube(2)

def string_reverser(string):
    return string [::-1]

reversed_string = string_reverser("Hello")

def celsius_converter(Faren):
    return round(((Faren - 32) * 5/9), 3 )

in_celsius = celsius_converter(0)

def palendrome_checker(string):
    if string == string [::-1]:
        return True
    else:
        return False

is_palendrome = palendrome_checker("hannah")


