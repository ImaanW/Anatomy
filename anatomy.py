import sys

count_of_args = len(sys.argv)
if count_of_args > 1:
    print('there is more than one args')
    print('the zeroth arg is' + sys.argv[0])
    print('the 1st arg is' + sys.argv[1])
    print('the 2st arg is' + sys.argv[2])
else:
    where = 'World'
    print("hello,", where)
print('Goodbye from' + sys.argv[0])



