def count_numbers(k, n, flag) :  
  
    # Base case  
    if (n == 1) :  
  
        # If 0 wasn't chosen previously  
        if (flag) :  
            return (k - 1)  
        else :  
            return 1
  
    # If 0 wasn't chosen previously  
    if (flag) :  
        return (k - 1) * (count_numbers(k, n - 1, 0) +
                          count_numbers(k, n - 1, 1))  
    else : 
        return count_numbers(k, n - 1, 1)  
  
# Driver code  
n = 1
k = 3
print(count_numbers(k, n, True)) 