import math

def cgpaRes(won):

    running_total=0
    cred=0
    for sem in won:
        total_cred = won[sem]["totalCredit"] 
        sgpa = won[sem]["SGPA"]

        running_total += total_cred * sgpa

        cred += total_cred

        cgpa = math.floor((running_total/cred) * 10 ** 2) / 10 ** 2#(running_total/cred,2)


        won[sem]["CGPA"] = cgpa


    return won











def sgpaRes(data):
    del data['csrfmiddlewaretoken']
    #print(data)
    no_of_sem=int(data['noSem'][0])
    del data['noSem']

    count=0
    indie=[]
    for z,i in enumerate(range(1,no_of_sem+1)):
        for field in data.keys():
            if  i == int(field[0]):
                count+=1
        
        indie.append(int(count/3))
        count=0

    win=dict()
    for w,v in enumerate(indie):
        zzz=dict()
        for k in range(1,v+1):
            zz=dict()
            name = str(w+1) + "name" +str(k)
            credits = str(w+1) + "credits" +str(k)
            grades= str(w+1) +"grade"+str(k)
            zz['name']=data[name]
            zz['credits']= data[credits]
            zz['grade'] = data[grades]
            
            zzz[k]= zz
        win[w+1]=zzz
    #print(win)

    won=dict()
    for sim in win:
        lin=dict()
        final_cred=0
        cred_points = 0
        for sub in win[sim]:
            #print(sub)
            cred=int(win[sim][sub]['credits'])
            grad=int(win[sim][sub]['grade'])
            final_cred +=cred 
            cred_points += (cred * grad)
        lin["totalCredit"]= final_cred
        lin["totalPoints"]= cred_points
        lin["SGPA"] = math.floor((cred_points/final_cred) * 10 ** 2) / 10 ** 2 #round(cred_points/final_cred,2)
        won[sim] = lin
    
    return won


#data={'noSem': '2', '1name1': 'Maths', '1credits1': '3', '1grade1': '10', '1name2': 'IPSR', '1credits2': '2', '1grade2': '7', '1name3': 'IPSR', '1credits3': '3', '1grade3': '8', '1name4': 'foc', '1credits4': '3', '1grade4': '9', '1name5': 'foc', '1credits5': '2', '1grade5': '10', '1name6': 'python', '1credits6': '1', '1grade6': '7', '1name7': 'python', '1credits7': '4', '1grade7': '10', '1name8': 'physics', '1credits8': '2', '1grade8': '7', '1name9': 'physics', '1credits9': '3', '1grade9': '8', '2name1': 'calculus', '2credits1': '3', '2grade1': '9', '2name2': 'java', '2credits2': '1', '2grade2': '7', '2name3': 'java', '2credits3': '4', '2grade3': '9', '2name4': 'clt', '2credits4': '3', '2grade4': '8', '2name5': 'ET', '2credits5': '2', '2grade5': '8', '2name6': 'ET', '2credits6': '3', '2grade6': '9', '2name7': 'ml', '2credits7': '2', '2grade7': '9', '2name8': 'ml', '2credits8': '4', '2grade8': '10'}
#print(sgpaRes(data))

#data={1: {'totalCredit': 23, 'totalPoints': 200, 'SGPA': 8.7}, 2: {'totalCredit': 22, 'totalPoints': 195, 'SGPA': 8.86}}
#print(cgpaRes(data))
#print(semester)

