student_data={'id1':{'name':['max'],'class':['VIII'],'subject':['eng,math,science']},
              'id2':{'name':['bob'],'class':['VII'],'subject':['eng,math,science']},
              'id3':{'name':['snowlin'],'class':['V'],'subject':['eng,math,science']},
              'id4':{'name':['john'],'class':['IV'],'subject':['eng,math,science']},
              'id5':{'name':['angela'],'class':['I'],'subject':['eng,math,science']},
              'id6':{'name':['harish'],'class':['II'],'subject':['eng,math,science']},}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)