# Write a function group(list, size) that take a list and splits into smaller lists of given size
def group(list,size):
  return [list[i:i+size] for i in range(0,len(list),size)]
print group([1,4,3,4,5,3,7,8,9],4)
