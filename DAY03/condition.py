#conditional

height = int(input("What is your height in cm? "))

if height > 120:
    print('You can ride')
    age = int(input("What is your age? "))
    bill = 0

    if age <= 7:
        bill = 7
    elif age <= 18:
        bill = 10
    elif age >= 45 and age <= 55:
        print('Thanks parents!!')
    else:
        bill = 12
    print(f'ticket price is ${bill}')

    wants_photo = input('Do you want a photo? (Y OR N): ')
    if (wants_photo == 'Y'):
        bill += 3

    print(f"Total price is {bill}")
else:
    print('Sorry,')
