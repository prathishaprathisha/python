def Smaxelements(list1, S): 
    final_list = [] 
  
    for i in range(0, S):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 
 
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
S = 2
Smaxelements(list1, S) 
