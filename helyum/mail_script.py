import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


# saving name and other infos into csv file
df = pd.read_csv("artists_info.csv", sep="\t")
# df.to_csv("artists_info.csv", sep="\t", index=False)

url = "https://www.behance.net/martindepasquale?tracking_source=search_projects_appreciations"
url2 = "https://www.behance.net/marceloperezlopez?tracking_source=search_projects_appreciations"


def get_info(url):
    global df
    r = requests.get(url)
    data = r.text

    mails = []
    names = []
    last_names = []

    soup = BeautifulSoup(data, "html.parser")
    text = soup.find_all("div")

    def class_finder(div, class_name, regex):
        divs = soup.find_all(div, {"class": class_name})
        return re.findall(regex, str(divs))

    try:
        MAIL_RX = r"[\w\.-]+@[\w\*.-]+"
        mails.append(class_finder("div", "UserInfo-bio-OZA", MAIL_RX))
        if len(mails[0]) == 0:
            raise Exception("MailNotFound")
        else:
            print(mails)
    except Exception:
        print("Mail not found!")
    #
    # if mail in the profile info, append it to mails list
    #
    NAME_RX = r">(\w*.+)</h1>"
    namee = class_finder("h1", "ProfileCard-userFullName-ule", NAME_RX)
    names.append(namee[0].split()[0])
    last_names.append(namee[0].split()[1:])
    print(names, last_names)

    #############################
    #                           #
    #       SOCIAL MEDIA        #
    #                           #
    #############################
    urls = [url]

    sm_sites = [
        "twitter.com",
        "facebook.com",
        "instagram.com",
        "pinterest.com",
        "medium.com",
        "behance.com",
        "dribble.com",
        "linkedin.com",
    ]
    sm_sites_present = []
    columns = ["url"] + sm_sites
    DFF = pd.DataFrame(data={"url": urls}, columns=columns)

    def get_sm(row):
        r = requests.get(row["url"])
        output = pd.Series(dtype=str)

        soup = BeautifulSoup(r.content, "html5lib")
        all_links = soup.find_all("a", href=True)
        for sm_site in sm_sites:
            for link in all_links:
                if sm_site in link.attrs["href"]:
                    output[sm_site] = link.attrs["href"]
        return output

    sm_columns = DFF.apply(get_sm, axis=1)
    DFF.update(sm_columns)
    DFF = DFF.dropna(axis=1, how="all")
    print(DFF)
    #
    # if mails[0] not in df["Mail"].values:
    #     df = df.append(
    #         {"Mail": mails[0],"Ad": names[0],
    # "Soyad": " ".join(last_names[0]),
    # "Instagram URL": instagram_l,},ignore_index=True,)
    # else:
    #     print("already in")


get_info(url2)

# print(df)
# df.to_csv("artists_info.csv", sep="\t", index=False)
