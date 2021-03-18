ListAwal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
def counterClockwise(ListAwal):
    listA = [];listB = [];listC=[];listAkhir = []
    for item in ListAwal:
        a = item[0] ; b = item[1] ; c = item[2]
        listA.append(a);listB.append(b);listC.append(c)
        listCBA = [listC,listB,listA]
        listAkhir.append(listCBA)
    for item in (listCBA):
        item
        print(item)

counterClockwise(ListAwal)