#size = int(input())
#numbers = list(map(int, input().split()))
size = 10
numbers = [64630,11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
numbers_sort=sorted(numbers)
sum1=0
for i in range(0,size):
    sum1=sum1+numbers[i]

if size%2==0: 
    median_index1=round(size/2)
    median_index2=round(size/2)-1
    median=(numbers_sort[median_index1]+numbers_sort[median_index2])/2
else:
    median_index1=round(size/2)
    median=numbers_sort[median_index1]

check1=0
count1=0
int_list=[]
mode_list=[]
for i in range(0,size):
    check1=numbers[i]
    count1=0
    for j in range(0,size-1):
        if check1==numbers[j]:
            count1=count1+1
    int_list=[numbers[i],count1]
    mode_list.append(int_list)

print(sum1/10)
print(median)
print(min(mode_list)[0])