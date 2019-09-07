success = False
for number in range(0, 3):
    print(f'Attemp {number}')
    if success:
        print('Success')
        break
else:
    print('Failed')
