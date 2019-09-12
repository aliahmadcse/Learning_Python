def user(**user):
    for key in user.keys():
        print(user[key])


user(id=1, name='Ali', age=19)
