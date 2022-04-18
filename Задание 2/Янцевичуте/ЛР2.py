def parts_sums(ls):
  ls1 = []
  for i in range(len(ls)):
    sum = 0
    for j in range(i,len(ls)):
      sum += ls[j]
    ls1.append(sum)
  ls1.append(0)
  return ls1

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
lsK = [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

print(parts_sums(ls))
print(lsK)