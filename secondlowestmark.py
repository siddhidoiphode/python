if __name__ == '__main__':
    names=[]
    marks=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        marks.append(score)
    
    temp=[]
    temp.extend(marks)
    temp=set(temp)
    temp=list(temp)
    temp.sort()
    val=temp[1]
    
    final=[]
    for i in range(len(marks)):
        if marks[i]==val:
            final.append(names[i])
    final.sort()
    for i in final:
        print(i)
