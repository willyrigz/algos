def minutes_to_hours(minutes):
    hours = minutes / 60.0
    return hours

def age_foo(age):
    new_age = float(age) + 50
    return(new_age)

def cel_to_fah(cel):
    if cel < -273.15:
        return 'Value too low'
    fahr = float(cel) * 9/5 + 32
    return fahr

def str_len(str):
    str_len = len(str)
    return str_len

# print(minutes_to_hours(34))  

# age = input("Please enter your age: ")
# print(age_foo(age))

# celsius = float(input("Please enter Celsius: "))
# print(cel_to_fah(celsius))

# my_str = input("Please enter a string: ")
# print(str_len(my_str))
# temperatures=[10,-20,-289,100]
# for t in temperatures:
#     print(cel_to_fah(t))

def duplicate_string(my_string):
    my_dict = {}
    string_status = 'All Unique'
    for c in my_string:
        if c in my_dict:
            my_dict[c] = my_dict[c]+1
            string_status = 'Duplicate Found'
        else:
            my_dict[c] = 1
    
    for k,v in my_dict.items():
        if v > 1:
            print(k,v)
    return string_status

print(duplicate_string('rapsontech'))
prime_factor = []
def factorization(my_number, prime_factors):
    
    while my_number % 2 == 0:
        prime_factors.append(2)
        my_number = int(my_number/2)
        # factorization(the_number,prime_factors)
    for i in range(3, my_number,2):
        while my_number % i == 0:
            prime_factors.append(i)
            my_number = int(my_number/i)
            # factorization(the_number,prime_factors)
    return(prime_factors)
# factorization(240, prime_factor)

print('This')
print(factorization(315, prime_factor))
        