num_list1 = [45,29,546,478,245,34]
num_list2 = [74,15,35,456,782,12,1,5,78,5]


def ascen_order(num_list1,num_list2):
    for h in range(len(num_list1)-1,0,-1):
        for i in range(h):
            if num_list1[i]>num_list1[i+1]:
                temp = num_list1[i]
                num_list1[i] = num_list1[i+1]
                num_list1[i+1] = temp
                
    for w in range(len(num_list2)-1,0,-1):
        for t in range(w):
            if num_list2[t]>num_list2[t+1]:
                temp = num_list2[t]
                num_list2[t] = num_list2[t+1]
                num_list2[t+1] = temp

              
ascen_order(num_list1,num_list2)
print (num_list1)
print (num_list2)
