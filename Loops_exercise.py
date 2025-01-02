## Level 1
for number in range(11):
    print(number)
else:
    print("The loop has ended")

count = 0
while count < 11:
    print(count)
    count +=1
else:
    print("the loop has ended")

for i in range(1,8):
    print('#'*i)


for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

lst = range(0,11)
for i in lst:
    print(f'{i} x {i} = {i*i}')

List =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for x in List:
    print(x)

for number in range(0,100):
    if number % 2 == 0:
        print(number)

for number in range(0,100):
    if number % 2 == 1: # condition for odd numbers; also != 0
        print(number) 


## Level 2
total_sum = 0
for number in range(101):
    total_sum += number

print(f"The sum of all numbers is {total_sum}.")

# Calculate the sum of all even and odd numbers from 0 to 100
sum_evens = 0
sum_odds = 0

for y in range(101):
    if y % 2 == 0:
        sum_evens += y
    else:
        sum_odds += y

print(f"The sum of all evens is {sum_evens}.")
print(f"And the sum of all odds is {sum_odds}.")



## Level 3
