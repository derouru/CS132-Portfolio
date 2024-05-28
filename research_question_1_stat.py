import pandas as pd 
import math

df = pd.read_csv('research_question_1_data.csv')
ttest = pd.read_csv('research_question_1_ttest.csv')

# print(df)

year = df[df.columns[0]]
sex = df[df.columns[1]]
age = df[df.columns[2]]
c11 = df[df.columns[3]]
c12 = df[df.columns[4]]
c14 = df[df.columns[5]]
c16 = df[df.columns[6]]
c23 = df[df.columns[7]]
p_values = ttest[ttest.columns[1]]
significant = ttest[ttest.columns[5]]

women_working = 0
men_working = 0
women_jobs = 0
men_jobs = 0

c14_men = [0]*10
c14_women = [0]*10
c16_men = [0]*22
c16_women = [0]*22
c23_men = [0]*7
c23_women = [0]*7

for i in range(1000):
    
    if sex[i] == 1 and age[i] >= 18:

        if c11[i] == 1: men_working += 1
        if c12[i] == 1: men_jobs += 1

        if 1 <= c14[i] <= 3:
            c14_men[0] += 1
        elif 11 <= c14[i] <= 14:
            c14_men[1] += 1 
        elif 21 <= c14[i] <= 26:
            c14_men[2] += 1
        elif 31 <= c14[i] <= 35:
            c14_men[3] += 1
        elif 41 <= c14[i] <= 44:
            c14_men[4] += 1
        elif 51 <= c14[i] <= 54:
            c14_men[5] += 1
        elif 61 <= c14[i] <= 63:
            c14_men[6] += 1
        elif 71 <= c14[i] <= 75:
            c14_men[7] += 1
        elif 81 <= c14[i] <= 83:
            c14_men[8] += 1
        elif 91 <= c14[i] <= 96:
            c14_men[9] += 1
        
        if 1 <= c16[i] <= 2:
            c16_men[0] += 1
        elif c16[i] == 3:
            c16_men[1] += 1
        elif 5 <= c16[i] <= 9:
            c16_men[2] += 1
        elif 10 <= c16[i] <= 33:
            c16_men[3] += 1
        elif c16[i] == 35:
            c16_men[4] += 1
        elif 36 <= c16[i] <= 39:
            c16_men[5] += 1
        elif 41 <= c16[i] <= 43:
            c16_men[6] += 1
        elif 45 <= c16[i] <= 47:
            c16_men[7] += 1
        elif 49 <= c16[i] <= 53:
            c16_men[8] += 1
        elif 55 <= c16[i] <= 56:
            c16_men[9] += 1
        elif 58 <= c16[i] <= 63:
            c16_men[10] += 1
        elif 64 <= c16[i] <= 66:
            c16_men[11] += 1
        elif c16[i] == 68:
            c16_men[12] += 1
        elif 69 <= c16[i] <= 75:
            c16_men[13] += 1
        elif 77 <= c16[i] <= 82:
            c16_men[14] += 1
        elif c16[i] == 84:
            c16_men[15] += 1
        elif c16[i] == 85:
            c16_men[16] += 1
        elif 86 <= c16[i] <= 88:
            c16_men[17] += 1
        elif 90 <= c16[i] <= 93:
            c16_men[18] += 1
        elif 94 <= c16[i] <= 96:
            c16_men[19] += 1
        elif 97 <= c16[i] <= 98:
            c16_men[20] += 1
        elif c16[i] == 99:
            c16_men[21] += 1
        
        match c23[i]:
            case 0: c23_men[0] += 1
            case 1: c23_men[1] += 1 
            case 2: c23_men[2] += 2 
            case 3: c23_men[3] += 3 
            case 4: c23_men[4] += 4 
            case 5: c23_men[5] += 5 
            case 6: c23_men[6] += 6 
    
    elif sex[i] == 2 and age[i] >= 18:

        if c11[i] == 1: women_working += 1
        if c12[i] == 1: women_jobs += 1

        if 1 <= c14[i] <= 3:
            c14_women[0] += 1
        elif 11 <= c14[i] <= 14:
            c14_women[1] += 1 
        elif 21 <= c14[i] <= 26:
            c14_women[2] += 1
        elif 31 <= c14[i] <= 35:
            c14_women[3] += 1
        elif 41 <= c14[i] <= 44:
            c14_women[4] += 1
        elif 51 <= c14[i] <= 54:
            c14_women[5] += 1
        elif 61 <= c14[i] <= 63:
            c14_women[6] += 1
        elif 71 <= c14[i] <= 75:
            c14_women[7] += 1
        elif 81 <= c14[i] <= 83:
            c14_women[8] += 1
        elif 91 <= c14[i] <= 96:
            c14_women[9] += 1
        
        if 1 <= c16[i] <= 2:
            c16_women[0] += 1
        elif c16[i] == 3:
            c16_women[1] += 1
        elif 5 <= c16[i] <= 9:
            c16_women[2] += 1
        elif 10 <= c16[i] <= 33:
            c16_women[3] += 1
        elif c16[i] == 35:
            c16_women[4] += 1
        elif 36 <= c16[i] <= 39:
            c16_women[5] += 1
        elif 41 <= c16[i] <= 43:
            c16_women[6] += 1
        elif 45 <= c16[i] <= 47:
            c16_women[7] += 1
        elif 49 <= c16[i] <= 53:
            c16_women[8] += 1
        elif 55 <= c16[i] <= 56:
            c16_women[9] += 1
        elif 58 <= c16[i] <= 63:
            c16_women[10] += 1
        elif 64 <= c16[i] <= 66:
            c16_women[11] += 1
        elif c16[i] == 68:
            c16_women[12] += 1
        elif 69 <= c16[i] <= 75:
            c16_women[13] += 1
        elif 77 <= c16[i] <= 82:
            c16_women[14] += 1
        elif c16[i] == 84:
            c16_women[15] += 1
        elif c16[i] == 85:
            c16_women[16] += 1
        elif 86 <= c16[i] <= 88:
            c16_women[17] += 1
        elif 90 <= c16[i] <= 93:
            c16_women[18] += 1
        elif 94 <= c16[i] <= 96:
            c16_women[19] += 1
        elif 97 <= c16[i] <= 98:
            c16_women[20] += 1
        elif c16[i] == 99:
            c16_women[21] += 1
        
        match c23[i]:
            case 0: c23_women[0] += 1
            case 1: c23_women[1] += 1 
            case 2: c23_women[2] += 2 
            case 3: c23_women[3] += 3 
            case 4: c23_women[4] += 4 
            case 5: c23_women[5] += 5 
            case 6: c23_women[6] += 6 


print("Total men working: ", men_working)
print("Total women working: ", women_working)
print("Total men with jobs: ", men_jobs)
print("Total women with jobs: ", women_jobs)

for i in range(10):
    ratio =  c14_women[i]/(c14_men[i]+c14_women[i]) if (c14_men[i]+c14_women[i]) > 0 else 0.00
    total = (c14_men[i]+c14_women[i])
    print("Occupation type ", i, ". M = ", c14_men[i], " W = ", c14_women[i], " | Ratio: ", ratio, " | N = ", total)

for i in range(22):
    ratio = c16_women[i]/(c16_men[i]+c16_women[i]) if (c16_men[i]+c16_women[i]) > 0 else 0.00 
    total = (c16_men[i]+c16_women[i])
    print(i, ",M,", c16_men[i])
    print(i, ",F,", c16_women[i]) 

for i in range(7):
    ratio = c23_women[i]/(c23_men[i]+c23_women[i]) if (c23_men[i]+c23_women[i]) > 0 else 0.00
    total = (c23_men[i]+c23_women[i])
    print(i, ",M,", c23_men[i])
    print(i, ",F,", c23_women[i]) 

for i in range(39):
    match significant[i]:
            case 0: print("no significant value at metric ", i)
            case 1: print("significant value at metric ", i)
            case 2: print("very significant metric at ", i)
            case 3: print("extremely significant metric at ", i)