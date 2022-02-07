import pandas as pd
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='6e0889093eff41548dc316635e3d2e38')

#all_articles = newsapi.get_everything(q='Solana',
 #                                     from_param='2022-01-03',
  #                                    to='2022-02-01',
   #                                   language='en',
    #                                  sort_by='relevancy')


req_data = {"id": [], "publishedAt": [], "name": [], "title": [], "description": [] }

#for i in range(0,5):
 #   print(all_articles['articles'][i]['title'])
#  print(all_articles['articles'][i]['description'])
  #  print()
cryptocurrencies=['Bitcoin', 'Cardano', 'Polkadot', 'Solana', 'Ripple', 'Dogecoin', 'Vechain','Matic', 'Polygon', 'Litecoin', 'Dent', 'Mirror Protocol', 'Ardor', 'Civic', 'Frontier', 'BUSD', 'Tether USD', '0x Protocol', 'Ontology', 'Paxos Gold', 'BitTorrent', 'Decentreland', 'Mana', 'Stellar', 'Shiba Inu', 'Basic Attention Token', 'Curve DAO Token', 'Chainlink', 'Cryptocurrency', 'Decentralised', 'Arweave', 'Origintoken', 'NFT', 'Uniswap', 'Binance', 'Coinswap', 'DFI Money']

#for i in range(len(cryptocurrencies)):
 #   all_articles = newsapi.get_everything(q=cryptocurrencies[i],
  #                                        from_param='2022-01-04',
   #                                       to='2022-02-01',
    #                                      language='en',
     #                                     sort_by='relevancy')
    #x = len(all_articles['articles'])
    #for i in range(x):
     #   req_data["id"].append(all_articles['articles'][i]['source']['id'])
      #  req_data["name"].append((all_articles['articles'][i]['source']['name']))
       # req_data["publishedAt"].append(all_articles['articles'][i]['publishedAt'])
        #req_data["title"].append(all_articles['articles'][i]['title'])
        #req_data["description"].append(all_articles['articles'][i]['description'])


#df = pd.DataFrame(req_data)
#df.to_csv("test-dataset.csv")

titledata=[]
descdata=[]

def informationgather(input) :
    all_articles = newsapi.get_everything(q=input,
                                          from_param='2022-01-04',
                                          to='2022-02-01',
                                          language='en',
                                          sort_by='relevancy')
    x = len(all_articles['articles'])
    for i in range(5):
        titledata.append(all_articles['articles'][i]['title'])
        descdata.append(all_articles['articles'][i]['description'])
    return (titledata , descdata)





