def a(arabic):
    parts = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    arabic_roman = {1:"I",
             5:"V",
             10:"X",
             50:"L",
             100:"C",
             500:"D",
             1000:"M"}
    decompose = []
    for i in parts:
        while (arabic-i) > -1:
            arabic = arabic-i
            decompose.append(i)
    decompose_2 = []
    for i in decompose:
        first = int(str(i)[0])
        if first%4 == 0:
            other  = [i/4,(i/4)*5]
            for y in other:
                decompose_2.append(y)
        elif first%9==0:
            other  = [i/9,(i/9)*10]
            for y in other:
                decompose_2.append(y)
        else:
            decompose_2.append(i)
    decompose_2 = [int(i) for i in decompose_2]
    roman = ""
    for i in decompose_2:
        roman += arabic_roman[i]
    return roman
