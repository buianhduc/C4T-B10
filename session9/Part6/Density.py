import numpy 
def Sum(myNumber):
    SUM=0
    for i in myNumber:
        SUM+=i;
    return SUM

Names = ['ST','BD','BTL','CG','DD','HBT']
Populations = [150300,247100,333300,266800,420900,318000]
Area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
Density = numpy.arange(len(Names))
for i in range(len(Names)):
    Density[i] = Populations[i]/Area[i]
print(Sum(Density)/(len(Names)+1))

