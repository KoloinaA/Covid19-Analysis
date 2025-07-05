import pandas as pd;
import matplotlib;
import matplotlib.pyplot as plt;
matplotlib.use('Agg');
data= pd.read_csv("moving-average-case-fatality-rate-of-covid-19.csv");
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
filtre = data[data["Case fatality rate of COVID-19 (short-term, %)"] > 3];
print(filtre);
#enlever les lignes avec NaN
data_sans_nan= data.dropna;
#remplacer nan par une autre valeur
iconnue= data.fillna("Inconnue");
#supprimer les duplicata
data_sans_duplicata =data.drop_duplicates();

#plt.hist(data["Case fatality rate of COVID-19 (short-term, %)"].dropna(), bins=30, color='skyblue')
#plt.xlabel("Taux de létalité (%)")
#plt.ylabel("Nombre de pays/dates")
#plt.title("Histogramme du taux de létalité court terme COVID-19")
#plt.savefig("histogramme_covid.png")

data= data.dropna(subset=["Case fatality rate of COVID-19 (short-term, %)"])
#case en fatality / entity
moyennes = data.groupby("Entity")["Case fatality rate of COVID-19 (short-term, %)"].mean()
moyennes = moyennes.sort_values(ascending=False)
top_20=moyennes.head(20)

# Affichage moyenne letalite / pays
plt.figure(figsize=(12, 6))
top_20.plot(kind="bar", color="coral")
plt.ylabel("Taux de létalité moyen (%)")
plt.title("Top 20 des pays par taux de létalité COVID-19 (moyenne)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("taux_letalite_par_pays.png")
