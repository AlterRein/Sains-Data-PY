import pandas as pd

df = pd.DataFrame(
    {
        "Nama" : ["Syfa", "Abdul", "Ibnu", "Santi"],
        "Umur" : ["17", "19", "18", "18"],
        "Skill" : ["Python", "Java", "C++", "C"]
    },
    index= [1, 2, 3, 4]
)

print(df)