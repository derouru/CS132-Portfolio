
for i in range(10):
    ratio =  c14_women[i]/(c14_men[i]+c14_women[i]) if (c14_men[i]+c14_women[i]) > 0 else 0.00
    total = (c14_men[i]+c14_women[i])
    print("Occupation type ", i, ". M = ", c14_men[i], " W = ", c14_women[i], " | Ratio: ", ratio, " | N = ", total)

for i in range(22):
    ratio = c16_women[i]/(c16_men[i]+c16_women[i]) if (c16_men[i]+c16_women[i]) > 0 else 0.00 
    total = (c16_men[i]+c16_women[i])
    print("Business type ", i, ". M = ", c16_men[i], " W = ", c16_women[i],  " | Ratio: ", ratio, " | N = ", total)

for i in range(7):
    ratio = c23_women[i]/(c23_men[i]+c23_women[i]) if (c23_men[i]+c23_women[i]) > 0 else 0.00
    total = (c23_men[i]+c23_women[i])
    print("Worker type ", i,". M = ", c23_men[i], " W = ", c23_women[i],  " | Ratio: ", ratio, " | N = ", total)