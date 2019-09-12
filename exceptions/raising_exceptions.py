# we learned how o handle exception, now lets learn how to raise
# exceptions


def cal_age(age):
    if age <= 0:
        raise ValueError("Age can't be zero")
    return 10/age


try:
    cal_age(0)
except ValueError:
    print('Error')
