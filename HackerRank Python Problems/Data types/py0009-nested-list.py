details = []             #Nested list to store name and score.... [[name1, score1], [name2], score2],.......]
sc=[]                    #Score list
na=[]                    #Name list

#Input name and score and append the pair as nested list 
for i in range(int(input())):
    name = input()
    score = float(input())
    details.append([name, score])
    
#Create a list of scores, covert it into a set, then convert back to a list of unique values of scores and sort it.
sc = sorted(list(set(details[a][1] for a in range(len(details)))))

#Compare the second lowest value from the sorte unique score list with the details array and find names of the matching score value
for p in range(len(details)):
    if sc[1] == details[p][1]:
        na.append(details[p][0])
        
#Sort the names and print names
na = sorted(na)
for i in range(len(na)):
    print(na[i])