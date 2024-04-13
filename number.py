#계산

num1 = int(input("정수를 입력하시오: "))
num2 = int(input("정수를 입력하시오: "))
num3 = int(input("정수를 입력하시오: "))
num4 = int(input("정수를 입력하시오: "))
num5 = int(input("정수를 입력하시오: "))

numbers = [num1, num2, num3, num4, num5]
print(numbers)

#total = num1 + num2 + num3 + num4 + num5
total = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
print("데이터 합계: {}".format(total))

average = total / len(numbers)
print("데이터 평균: {:.2f}".format(average))