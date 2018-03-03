from collections import Counter

def youso(atai):
    a = []
    for num in range(0,int(len(str(atai)))):
        a.append((str(atai)[num]))

    kazu = [0,0,0,0,0,0,0,0,0,0]
    counter = Counter(a)
    for k,v in counter.items():
        index = int(k)
        yousosuu = int(v)
        kazu[index] = yousosuu
    return kazu

def kapukei(syoki,keta):
    a = []
    for num in range(0,int(len(str(syoki)))):
        a.append((str(syoki)[num]))
    a.sort()
    saisyo = int(''.join(a))
    a.reverse()
    saidai = int(''.join(a))
    saidai = saidai*10**(keta-len(str(saidai)))
    return saidai - saisyo

syoki = 1112
keta = int(len(str(syoki)))
for num in range(0,10):
    ato = kapukei(syoki,keta)
    print(syoki,ato)
    if youso(syoki)==youso(ato):
        print ("onaji")
        break
    else:
        print ("chigau")
    syoki = ato 

