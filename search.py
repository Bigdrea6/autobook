from bs4 import BeautifulSoup as bs
import lxml

def clear(html):
    soup=bs(html,"lxml")
    table=soup.find_all("td")
    num=[14, 27, 40, 53, 66, 79, 92]
    hi=[]
    yotei=[]
    free=0
    for i in range(14,len(table)):
        hoge=str(table[i])
        if i in num:
            hi.append(table[i].text)
        elif 'Empty' in hoge:
            yotei.append('x')
        else:
            yotei.append('o')
            free+=1
    ans=[]
    dummy=["dummy"]
    j=0
    for i in range(len(yotei)):
        if i==0:
            ans.append(hi[0])
            j+=1
        elif i%12==0:
            ans.append(yotei[i])
            ans.append(hi[j])
            j+=1
        else:
            ans.append(yotei[i])
    if free==0:
        return dummy
    else:
        return ans
