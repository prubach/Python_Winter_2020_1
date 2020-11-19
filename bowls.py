
def sum_bowls(n):
    if n == 1:
        return n
    else:
        return n + sum_bowls(n - 1)

print(sum_bowls(998))


#n = int(input("enter the number: "))
n = 1000000
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("N", n, "numbers is: ", sum )