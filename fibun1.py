import csv
CsvFile = csv.reader(open('biblio.csv'),delimiter=',')
CsvList = []
for num in CsvFile:
    CsvList.append(num)
for num in range(0,len(CsvList)):
    print(num,CsvList[num][5][0:15].strip())
