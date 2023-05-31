
#!-------------------------------------------------------------------------------------------------------------------------------------
#%                                                      Stars Pattern
#!-------------------------------------------------------------------------------------------------------------------------------------
## Example-1

#%  *
#%    *
#%      *
#%        *
#%          *
'''
n=int(input("Enter n value: "))
stars=1
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp+=1
    print()
'''






## Example-2

#%          *
#%        *
#%      *
#%    *
#%  *
'''
n=int(input("Enter n value: "))
stars=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp-=1
    print()
'''






## Example-3

#%  * * * * *
#%  * * * *
#%  * * *
#%  * *
#%  *
'''
n=int(input("Enter n value: "))
stars=n
for i in range(n):
    for j in range(stars):
        print('*',end=' ')
    stars-=1
    print()
'''






## Example-4

#%  * * * * *
#%    * * * *
#%      * * *
#%        * *
#%          *
'''
n=int(input("Enter n value: "))
stars=n
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp+=1
    stars-=1
    print()
'''






## Example-5

#%  *
#%  * *
#%  * * *
#%  * * * *
#%  * * * * *
'''
n=int(input("Enter n value: "))
stars=1
for i in range(n):
    for i in range(stars):
        print('*',end=' ')
    stars+=1
    print()
'''






## Example-6

#%          *
#%        * *
#%      * * *
#%    * * * *
#%  * * * * *
'''
n=int(input("Enter n value: "))
stars=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp-=1
    stars+=1
    print()
'''





## Example-7

#%          *
#%        * * *
#%      * * * * *
#%    * * * * * * *
#%  * * * * * * * * *
'''
n = int(input("Enter n value: "))
stars=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp-=1
    stars+=2
    print()
'''






## Example-8

#%  * * * * * * * * *
#%    * * * * * * *
#%      * * * * *
#%        * * *
#%          *
'''
n = int(input("Enter n value: "))
stars=2*n-1
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    sp+=1
    stars-=2
    print()
'''





## Example-9

#%          *
#%        * * *
#%      * * * * *
#%    * * * * * * *
#%  * * * * * * * * *
#%    * * * * * * *
#%      * * * * *
#%        * * *
#%          *
'''
n = int(input("Enter n value: "))
stars=1
sp=n//2
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        stars+=2
        sp-=1
    else:
        stars-=2
        sp+=1
'''






## Example-10

#%  *
#%  * *
#%  * * *
#%  * * * *
#%  * * * * *
#%  * * * *
#%  * * *
#%  * *
#%  *
'''
n = int(input("Enter n value: "))
stars=1
for i in range(n):
    for k in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        stars+=1
    else:
        stars-=1
'''






## Example-11

#%          *
#%        * *
#%      * * *
#%    * * * *
#%  * * * * *
#%    * * * *
#%      * * *
#%        * *
#%          *
'''
n = int(input("Enter n value: "))
stars=1
sp=n//2
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for k in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        stars+=1
        sp-=1
    else:
        stars-=1
        sp+=1
'''






## Example-12

#%  *                 *
#%  * *             * *
#%  * * *         * * *
#%  * * * *     * * * *
#%  * * * * * * * * * *
#%  * * * *     * * * *
#%  * * *         * * *
#%  * *             * *
#%  *                 *
'''
n = int(input("Enter n value: "))
stars=1
sp=n-1
for i in range(n):
    for k in range(stars):
        print('*',end=' ')
    for s in range(sp):
        print(' ',end=' ')
    for k in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        stars+=1
        sp-=2
    else:
        stars-=1
        sp+=2
'''








## Example-13
#%  *
#%    *
#%      *
#%        *
#%          *
#%        *
#%      *
#%    *
#%  *
'''
n = int(input("Enter n value: "))
stars=1
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        sp+=1
    else:
        sp-=1
'''






## Example-14

#%          *
#%        *
#%      *
#%    *
#%  *
#%    *
#%      *
#%        *
#%          *
'''
n = int(input("Enter n value: "))
stars=1
sp=n//2
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(stars):
        print('*',end=' ')
    print()
    if i<n//2:
        sp-=1
    else:
        sp+=1
'''