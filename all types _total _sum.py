list = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_even=0
count_odd=0
sum_even=0
sum_odd=0
average_even=0
average_odd=0
total_sum=0
total_count=0
total_average=0
while i<len(list):
    if list[i]%2==0:
        count_even+=list[i]
        sum_even+=list[i]
        average_even=average_list/list[i]
    elif list[i]%2==1:
        count_odd+=list[i]
        sum_odd+=list[i]
        average_odd=average_list/list[i]
    else:
        total_sum=sum_even+sum_odd
        total_count=count_even+count_odd
        total_average=average_even+average_odd
    i+=1
print(count_even)
print(count_odd)
print(sum_even)
print(sum_odd)
print(average_even)
print(average_odd)
print(total_sum)
print(total_count)
print(total_average)


        
        
    
        
    
    


    
    
    
        

