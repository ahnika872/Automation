def fizz_buzz(n):
    for i in range(1,n):
        if i/3:
            print('Fizz')
        if i/5:
            print('Buzz')
        if i/3 and i/5:
            print('FizzBuzz')
print(fizz_buzz(9))