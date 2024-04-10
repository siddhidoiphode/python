li = student_marks[query_name]
for values in li:
  sum=sum+values
  n+=1
ave=sum/n
ans='{:.2f}'.format(ave)
print(ans)
