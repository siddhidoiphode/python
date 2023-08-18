if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    st=set(arr)
    arr=list(st)
    arr.sort()
    print(arr[-2])
    
