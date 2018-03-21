import csv
import collections
CsvFile = csv.reader(open('biblio.csv'),delimiter=',')
CsvList = []
for num in CsvFile:
    CsvList.append(num)
total = len(CsvList)
FI = []
for num in range(0,total):
    FI.append(CsvList[num][5][0:15].strip())
count_dict = collections.Counter(FI)

print(count_dict)
