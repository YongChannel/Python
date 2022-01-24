import os

with open('C:/works/python/lec05/대전.csv', 'r', encoding='euc-kr') as f:
    lines = f.readlines()
    guList = lines[0].strip('\n').split(',')
    print(guList)

    for line in lines[1:]:
        dongList = line.strip('\n').split(',')
        print(dongList)

        for gu, dong in zip(guList, dongList):
            path = 'C:/works/python/lec05'
            dirPath = path + '/대전' + '/' + gu + '/' + dong
            if not os.path.exists(dirPath) and dong != "":
                os.makedirs(dirPath)
                filePath = dirPath + '/' + dong + '.hwp'
                with open(filePath, 'wb') as f:
                    f
