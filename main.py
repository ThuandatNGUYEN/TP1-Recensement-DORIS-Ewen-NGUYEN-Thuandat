import csv

from matplotlib import pyplot as plt

# fonction pour charger les fichiers
def load_data(file_path, delim):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        temp = [[cell.replace(" ", "").strip() for cell in row] for row in reader]
    del temp[0]
    return temp


# charge les données dans les variables
common_metadata = load_data('metadonnees_communes.csv', ';')
data2008 = load_data('donnees_2008.csv', ',')
data2016 = load_data('donnees_2016.csv', ',')
data2021 = load_data('donnees_2021.csv', ';')

# trie les données 2008 & 2016
aglototal = ["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches",
             "Champs-sur-Yonne", "Charbuy", "Chevannes", "Chitry",
             "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille",
             "Gurgy", "Gy-l'Évêque", "Irancy", "Jussy", "Lindry",
             "Mon´eteau", "Montigny-la-Resle", "Perrigny", "Quenne",
             "Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan",
             "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles",
             "Vincelottes"]

for data_index, data in enumerate([data2008, data2016]):
    data = [line for line in data if len(line) > 6 and line[6] in aglototal]
    if data_index == 0:
        data2008 = data
    else:
        data2016 = data

#  trie les données 2021
allowed_num = []
for line in common_metadata:
    if line[3] in aglototal and line[2] not in allowed_num:
        allowed_num.append(line[2])
data2021 = [line for line in data2021 if line[2] in allowed_num]

# préparation du graphique
# avec y1 = Population Totale, y2 = Population comptée à part, y3 = Population Municipale
x = [2008, 2016, 2021]
y1 = [0, 0, 0]
y2 = [0, 0, 0]
y3 = [0, 0, 0]

for data_index, data in enumerate([data2008, data2016]):
    for line in data:
        if data_index == 0:
            y1[0] += int(line[9])
            y2[0] += int(line[8])
            y3[0] += int(line[7])
        else:
            y1[1] += int(line[9])
            y2[1] += int(line[8])
            y3[1] += int(line[7])

for line in data2021:
    y1[2] += int(line[5])
    y2[2] += int(line[4])
    y3[2] += int(line[3])

plt.figure(figsize=(7, 5))
plt.plot(x, y1, label='Population Totale')
plt.plot(x, y2, label='Population comptée à part')
plt.plot(x, y3, label='Population Municipale')
plt.title("Graphique de l'évolution de lagglomeration totale.")
plt.ylabel('Population')
plt.xlabel('Années')
for i in range(len(x)):
    plt.annotate("{:.2f}".format(y1[i]), (x[i], y1[i]))
    plt.annotate("{:.2f}".format(y2[i]), (x[i], y2[i]))
    plt.annotate("{:.2f}".format(y3[i]), (x[i], y3[i]))
plt.legend()
plt.show()
