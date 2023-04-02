import requests
from bs4 import BeautifulSoup as bs
from csv import writer 
link1="https://www.dominos.co.in/store-location/hyderabad"
page=requests.get(link1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
print(page)
soup=bs(page.content,"html.parser")
soup1=soup.find("ul",{"class":"citylist-ul"})
list_of_cities=soup1.find_all("li")
list1_of_cities=[]
for i in list_of_cities:
    i=i.text
    for j in range(len(i)-1,-1,-1):
        if i[j]=="(":
            list1_of_cities.append(i[:j-1])
            break
with open("info.csv","w",encoding="utf8",newline="") as f:
    thewriter=writer(f)
    header=["City","Landmark","Full_Adress","Time"]
    thewriter.writerow(header)
    for city in list1_of_cities:
        link1=link1="https://www.dominos.co.in/store-location/"+city
        print(link1)
        page=requests.get(link1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
        print(page)
        soup=bs(page.content,"html.parser")
        add=soup.find_all("div",{"class":"panel-body"})
        for i in add:
            City=city
            Landmark=i.find("p",{"class","city-main-sub-title"}).text
            Adress_and_PhoneNo=i.find("p",{"class","grey-text mb-0"}).text
            Timing=i.find("div",{"class","col-xs-9 col-md-9 pl0 search-grid-right-text"}).text[8:23]
            info=[City,Landmark,Adress_and_PhoneNo,Timing]
            thewriter.writerow(info)
