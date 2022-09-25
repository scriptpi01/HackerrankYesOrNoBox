result_list=[]
t = int(input())
for i in range(t):
  size = int(input()) #5
  block = input().split()
  if size % 2 != 0 :
    if block[0] < block[size-1]:
      block.insert(size-(size//2+1),max(block)*10)
      block_reverse = block[::-1]
    elif block[0] > block[size-1]:
      block.insert(size-(size//2),max(block)*10)
      block_reverse = block[::-1]
    for j in range(int(size/2)): #0 1 2 3 4
      if block[j] < block[j+1] and block_reverse[j] < block_reverse[j+1]:
        result = 'No'
        break
      else:
        result = 'Yes'
  else:
    block_reverse = block[::-1]
    for j in range(int(size/2)): #0 1 2 3 4
      if block[j] < block[j+1] and block_reverse[j] < block_reverse[j+1]:
        result = 'No'       
        break
      else:
        result = 'Yes'
  result_list.append(result)
print('\n'.join(result_list))
