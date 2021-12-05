n = 5
weights = [1.01,1.99,2.5,1.5,1.01]
# output 3
weights.sort()
print(weights)

No_of_trips = 0
bag1_index = 0

weights_size = len(weights)-1
for i in range(1,weights_size,1):
    print(i)
    if weights[i] > 1.99:
        No_of_trips=No_of_trips+1
    elif weights[i] <= 1.99:
        if weights[bag1_index]+weights[i] <= 3:
            bag1_index = bag1_index+1
        No_of_trips=No_of_trips+1
    if bag1_index > i:
        break

print(No_of_trips)
