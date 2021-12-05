arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

def duplicateZeros(arr):
  arr2 = [i for i in arr]
  i=0
  j = 0
  while i < len(arr):
     if not arr2[j]:
        arr[i] = 0
        i+=1
        if i<len(arr):
           arr[i] = 0
     else:
        arr[i] = arr2[j]
     j+=1
     i+=1
  return arr

result = duplicateZeros(arr)
print(result)
