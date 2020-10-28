import random
import requests
from bs4 import BeautifulSoup
import codecs

def read_all_vocab():
    vocab_file = open("Bütün_kelimeler.txt","r")
    vocabs = vocab_file.read()
    vocab_list = vocabs.split("\n")
    vocab_file.close()
    return vocab_list


def mix_vocab(v):
    vocab_days = []
    day_list = []
    while len(vocab_days) < 57:
        day_list = []
        while len(day_list) < 10:
            while True:
                random_vocab = random.randint(1,len(v)-1)
                vocab = v[random_vocab]
                flag = 0
                for i in range(len(vocab_days)):
                    if vocab in vocab_days[i]:
                        flag = 1
                        break
                if flag == 0:
                    day_list.append(vocab)
                    break
        vocab_days.append(day_list)
        
    return vocab_days


def write_days(d):
    f = open("days.txt","w")
    for i in range(len(d)):
        for k in d[i]:
            f.write(k)
            f.write("\n")
        f.write("*****")


def find_meanings(v):
    f = codecs.open("days_meanings.txt","w", encoding="utf-8")
    for i in range(len(v)):
        for j in v[i]:

            url = "https://tureng.com/tr/turkce-ingilizce/"+j
            r=requests.get(url, timeout=50)

            soup = BeautifulSoup(r.content,"html.parser")
            gelen_veri = soup.find_all("table", {"class":"table table-hover table-striped searchResultsTable"})
            veriler = gelen_veri[0].contents[7]
            anlamlar = veriler.find_all("a")
            anlam = anlamlar[1].text
            f.write(anlam)
            f.write("\n")
        f.write("*****")


liste = read_all_vocab()
mixed = mix_vocab(liste)
write_days(mixed)
find_meanings(mixed)