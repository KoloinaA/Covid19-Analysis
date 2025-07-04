import pandas as pd
data= pd.read_csv("daily-new-confirmed-covid-19-cases-per-million-people.csv");
#afficher 5 première lignes
print(data.head());
#afficher le nombre de lignes et de colonnes
print(data.shape);
#stat descriptive
print(data.describe);
#type de données
print(data.dtypes);
#selectionner une colonne (Entity, Day,NewCase)
colonne = data["Entity"];
print(colonne);
#filtre nouveau cas confirmé par jour > 100
#filtre = data[data["NewCase"] > 100];
print(data.columns);
