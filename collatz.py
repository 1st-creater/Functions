def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
        elif num % 2 == 1:
            num = 3 * num + 1
            print(num)
        elif num == 1:
            return num


print('Enter number:')
try:
    user = int(input())
except NameError as ValueError:
    print('Print enter an integer value.')
collatz(user)




# print와 return의 차이
# print는 원하는 값을 화면상에 출력하는 역할
# return은 다른 곳에서 이 값을 다시 사용할 수 있도록 실제 값을 가져다주는 역할, 따라서 이 반환값은 변수에 저장 가능
# 이런 방식으로 문제를 풀 경우에는 return 구문이 필요하다

# def collatz(number):
#
#     if number % 2 == 0:
#         print(number // 2)
#         return number // 2
#
#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#         return result
#
# n = input("Give me a number: ")
# while n != 1:
#     n = collatz(int(n))