n=int(input())

lst=list(map(int,input().split()))

count=0

for i in range(1,n):
    if lst[i]<lst[i-1]:
        count+=(lst[i-1]-lst[i])
        lst[i]=lst[i-1]

print(count)