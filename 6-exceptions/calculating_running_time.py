from timeit import timeit

code1="""
def cal_age(age):
    if age <= 0:
        raise ValueError("Age can't be zero")
    return 10/age


try:
    cal_age(0)
except ValueError as error:
    print(error)
"""
print('firstAttempt',timeit(code1,number=100000))

