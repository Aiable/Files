long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
text = long_text.split('\n')
text_list = []
for i in text:
    text = i.strip(' ')
    text_list.append(text)
del text_list[0]
del text_list[len(text_list)-1]
end_file = {}
b = 1
index_list = []
for i in text_list:
    if str(b) + '.' in i:
        b += 1
        index_list.append(text_list.index(i))
sub_fund = []


def func(list1, index_list, n):
    try:
        if n == 0:
            end_file['name'] = list1[n]
        elif n == 1:
            end_file['lei'] = list1[n]

        else:

            if n in index_list:
                idx = index_list.index(n)
                for i in range(index_list[idx], index_list[idx + 1]):
                    res = {}
                    if i == list(range(index_list[idx], index_list[idx + 1]))[0]:
                        list1[i].split(".")
                        list1[i].strip(' ')
                        res['title'] = list1[i]
                        sub_fund.append(res)
                    else:
                        lst = []
                        lst.append(list1[i])
                        res['isin'] = lst
                        sub_fund.append(res)
    except:
        res = {}
        res['title']=list1[index_list[len(index_list)-1]]
        lst = []
        for i in range(index_list[len(index_list)-1]+1,len(list1)):
            lst.append(list1[i])
        res['isin']= lst
        sub_fund.append(res)
        return

    n += 1
    func(list1, index_list, n)

func(text_list, index_list, 0)
end_file['sub_fund'] = sub_fund
print(end_file)