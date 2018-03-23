import csv
import collections

def FIread(filename):
    CsvFile = csv.reader(open(filename),delimiter=',')
    CsvList = []
    for num in CsvFile:
        CsvList.append(num)
    total = len(CsvList)
    FIndk = []
    for num in range(0,total):
        FIndk.append(CsvList[num][5][0:15].strip())
    return collections.Counter(FIndk),total

file1 = 'biblioNDK.csv'

result = FIread(file1)

file2 = 'bibliokyocera.csv'

result2 = FIread(file2)

file3 = 'biblioepson.csv'

result3 = FIread(file3)

file4 = 'bibliomurata.csv'

result4 = FIread(file4)

re_total = result[0] + result2[0] + result3[0] + result4[0]

for k,v in sorted(re_total.items()):
#for k,v in re_total.items():
    kensuNDK = result[0][k]/result[1]*100
    kensukyocera = result2[0][k]/result2[1]*100
    kensuepson = result3[0][k]/result3[1]*100
    kensumurata = result4[0][k]/result4[1]*100
    print (k,',','{:.2f}'.format(kensuNDK),',','{:.2f}'.format(kensukyocera),',','{:.2f}'.format(kensuepson),',','{:.2f}'.format(kensumurata))
