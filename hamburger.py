import pandas as pd
import numpy as np
'''chicago_socioeconomic_data = pd.read_csv('C:/Users/Ebru/PycharmProjects/python6/venv/hamburger.csv')
print(chicago_socioeconomic_data.head(5))'''
chicago_socioeconomic_data = pd.read_csv('C:/Users/Ebru/PycharmProjects/python6/venv/chicago.csv')
print(chicago_socioeconomic_data[chicago_socioeconomic_data.City == 'Chicago'].value_counts())
print(chicago_socioeconomic_data[['Chicago']])
df = pd.read_csv("C:/Users/Ebru/PycharmProjects/python6/venv/hamburger.csv")
df.rename(columns={"Elementary, Middle, or High School": "b"})
df = pd.DataFrame(df)
column = df.columns
'''print(chicago_socioeconomic_data[chicago_socioeconomic_data.b == 'ED'].size())'''




