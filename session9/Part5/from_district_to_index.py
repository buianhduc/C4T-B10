Names = ['ST','BD','BTL','CG','DD','HBT']
Populations = [150300,247100,333300,266800,420900,318000]
Max = Populations[1]
PosMax = 1
Min = Populations[1]
PosMin = 1
for i in range(1,len(Populations)):
    if(Max < Populations[i]):
        Max=Populations[i]
        PosMax=i
    if(Min > Populations[i]):
        Min = Populations[i]
        PosMin=i
print("District that has the most population is ", Names[PosMax],'\n')
print("District that has the least population is ", Names[PosMin],'\n')

