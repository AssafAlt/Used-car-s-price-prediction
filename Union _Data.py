import os
import pandas as pd
Final_DataBase = pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        Final_DataBase = Final_DataBase.append(pd.read_csv(file))

Final_DataBase.to_csv('DataBase.csv', index=False)








