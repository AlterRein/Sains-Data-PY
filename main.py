import pandas as pd

df = pd.DataFrame(
    {
        "Nama" : ["Syfa", "Abdul", "Ibnu", "Santi"],
        "Umur" : ["17", "19", "18", "18"],
        "Skill" : ["Python", "Java", "C++", "C"]
    },
    index= [1, 2, 3, 4]
)
repivot_df = df.pivot(index='Umur', columns='Skill', values='Nama')
renamee_df = df.rename(columns = {'Skill' : 'Ability'})

print(df)
print("\n")
print(renamee_df)
print("\n")
print(repivot_df.isnull())

python_not_null = repivot_df[repivot_df['Python'].notnull()]
print(python_not_null)