#!/bin/python3
import time


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        
            
        n = int(input().strip())
        start = time.time()
        
        if n%3==0:
            n3=n//3-1
        else:
            n3=n//3
             
        if n%5==0:
            n5=n//5-1
        else:
            n5=n//5
            
        if n%15==0:
            n15=n//15-1
        else:
            n15=n//15
        
        if n<=3:
            print(int(0))
        elif n<4:
            print(int(3))
        elif n<16:
            print(int((n3 * (n3 + 1) * 3) / 2+(n5 * (n5 + 1) * 5) / 2))
        elif n>=16:
            print(int(((n3 * (n3 + 1) * 3) // 2)+((n5 * (n5 + 1) * 5) // 2)-((n15 * (n15 + 1) * 15) // 2)))
            
            
finish = time.time()
print('Execution time: ',finish-start)
