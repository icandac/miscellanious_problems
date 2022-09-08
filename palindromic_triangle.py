# Palindromic Triangle

nmbr = int(input())
res = []
    
for _ in range(1,nmbr+2):
    dumarr = [i for i in range(1,_)]
    dumarrinv = dumarr[::-1]
    dumarrinv = dumarrinv[1:]
    dum = dumarr+dumarrinv
    if _>1:
        res.append(''.join(map(str, dum)))

    
print('\n'.join(res))

# for i in range(1,int(input())+1):
#     print( (10**i-1)**2 // 81)