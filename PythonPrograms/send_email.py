import pandas as pd

ConfigQueries=pd.read_csv('C:\Python\scripts\IKEAWarningAlerts\Configuration.csv',encoding="ISO-8859-1")

for check in ConfigQueries.index:
    print(ConfigQueries['Application'][check])
