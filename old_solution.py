#!/bin/python3

import sys
import time



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    inicio = time.time()
    suma=0
    if n%3==0:
        for i in range((n//3)):
        
            suma+=i*3
    else:
        for i in range((n//3)+1):
        
            suma+=i*3
            
            
            
            
    if n%5==0:
        for i in range((n//5)):
            if i%3!=0:
        
                suma+=i*5
                
    else:
        
        for i in range((n//5)+1):
                if i%3!=0:
            
                    suma+=i*5
    print('Solution: ',suma)
    

fin = time.time()
print('Execution time: ',fin-inicio) # 1.5099220275878906
