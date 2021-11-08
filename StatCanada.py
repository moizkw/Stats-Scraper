from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def main():
    struct = {"Jurisdiction":None,
            "CUSTODY number":None,
            "CUSTODY rate":None,
            "CUSTODY percent change in rate from 2016/2017":None,
            "COMMUNITY SUPERVISION number":None,
            "COMMUNITY SUPERVISION rate":None,
            "COMMUNITY SUPERVISION percent change in rate from 2016/2017":None,
            "TOTAL CORRECTIONAL SERVICES number":None,
            "TOTAL CORRECTIONAL SERVICES rate":None,
            "TOTAL CORRECTIONAL SERVICES percent change in rate from 2016/2017":None,
            "TOTAL CORRECTIONAL SERVICES percent change in rate from 2013/2014":None}

    keys = list(struct.keys())

    with open("avg_adults_in_correctional_services.json", "w") as f:
        f.write('{"Average daily counts of adults in correctional services, by type of supervision and jurisdiction, 2017/2018": [\n')

    link = urlopen('https://www150.statcan.gc.ca/n1/pub/85-002-x/2019001/article/00010/tbl/tbl01-eng.htm')
    soup = BeautifulSoup(link, 'html.parser')

    for i in range(3,19):
        th = soup.find('th', attrs={'id':('s_704_'+str(i)+'-1')})
        struct["Jurisdiction"] = th.get_text(strip=True)
        for x in range(1,11):
            y=2
            if x>=7: y=4
            elif x>=4: y=3
            header = (f"s_704_{i}-1 h_704_1-{y} u_704_2-{x}")
            td = soup.find('td', attrs={'headers':header})
            struct[keys[x]] = td.get_text(strip=True)

        with open("avg_adults_in_correctional_services.json", "a") as f:
            json.dump(struct, f)
            f.write(',\n')

    with open("avg_adults_in_correctional_services.json", "a") as f:
        f.write(']}')

if __name__ == "__main__":
    main()