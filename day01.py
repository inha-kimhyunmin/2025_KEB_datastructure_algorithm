
#O(n)
num = int(input("Input Number : "))
sum = 0
for i in range(num + 1):
    sum = sum + i

print(sum)


print(num*(num+1)//2)