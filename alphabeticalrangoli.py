ele = ''
n = int(input(" enter number: "))
store = "abcdefghijklmnopqrstuvwxyz"
col = (2 * ((2 * n) - 1)) - 1
for i in range(n - 1, 0, -1):
  if i == n - 1:
    print(store[i].center(col, '-'))
  ele = ele + "-" + store[i]
  ans = ele + "-" + store[i - 1] + "-"+"".join(reversed(ele))
  ans=ans[1:-1]
  print(ans.center(col, '-'))
for i in range(n-1):
  ans=ans[0:len(ans)//2]+ans[(len(ans)//2)+4:]
  print(ans.center(col, '-'))
