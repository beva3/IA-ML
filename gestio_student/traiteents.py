import pandas as pd

data = {
    'name' : ['Nanja','Valih','Tsanta'],
    'attendence':[12,23,21],
    'assignment':[12,34,21],
    'project':[4,5,6],
    'exam':[12,15,7],
    'somme':[0,0,0],
    'is_pass':[True,False,True]
}

MAX_REQUIR={
    'at':5,
    'as':25,
    'proj':40,
    'ex':30
}

def is_pass(note_student):
    if note_student > 50:
        return True
    else : return False

def update_data(data_student):
    print("update")
    df = pd.DataFrame(data_student)
    df['somme'] = df[['attendence', 'assignment', 'project', 'exam']].sum(axis=1)
    
    df['is_pass'] = df['somme'].apply(is_pass)

    return df