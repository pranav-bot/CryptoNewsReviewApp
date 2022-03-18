from Api_test import *
from LanguageProcessor import *

coinname=str(input("Enter Coin Name"))


for i in range(5):
    title = [informationgather(coinname)[0][i]]
    desc = informationgather(coinname)[1][i]
    sentimentanalysis(title, desc)


