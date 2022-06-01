first_name = 'Imaan'
hobby = 'Nails'
food = 'Pizza'
print(type(first_name))
# most nested happens first ; Bidmas
#shows as a string
print(dir(hobby))
# shows all built in capabilities
upper_case_first_name = first_name.upper()
# adds a method
print(upper_case_first_name)
print(first_name)
lucky_number = 8
print(type(lucky_number))
# presents as a interger
price = 4.99
print(type(price))
# presents as a float - floating point numbers
broccoli_fan = True
print(type(broccoli_fan))
# presents as a bool - true false yes/no
lucky_number_doubled = lucky_number * 2
print(lucky_number_doubled)
first_name_doubled = first_name * 2
print(first_name_doubled)
#multipler has been overloaded, string repeated
sum_result = lucky_number + 10
print(sum_result)
about_me = first_name + " likes to eat " + food + " has the hobby of " + hobby
print(about_me)
#concatination  and glues the objects together
stein = 1
pint = 1
stein += pint
print(stein)
# augumented/compound assignments - operator on the left before the assingments - gives the vules of stein to 2
