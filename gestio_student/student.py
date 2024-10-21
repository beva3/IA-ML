from traiteents import *



data = {
    'name' : ['Nanja','Valih','Tsanta'],
    'attendence':[12,23,21],
    'assignment':[12,34,21],
    'project':[4,5,6],
    'exam':[12,15,7],
    'is_pass':[True,False,True]
}

df = pd.DataFrame(data)

print(df)