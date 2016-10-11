def find_max_min(arg):#created function find_max_min with arg as its parameter.
  ans = []
  max_num = max(arg)
  min_num = min(arg)
  if min_num == max_num:
    length = len(arg)
    ans.append(length)
  else:
    ans.append(min_num)
    ans.append(max_num)
  return ans
#the labels used rhime with the expected inputs and out puts 
#forexampla max_num to mean maximum number, Min_number for minimum number, arg for argument e.t.c
