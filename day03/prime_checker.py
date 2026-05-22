# for num in range(1,21):
#     for i in range(2,num):
#         if num % i == 0:
#             print(num,"its not prime number")
#             break
#     else:
#         print(num, "prime number")

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


num = 11

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")