import requests

if __name__ == '__main__':


 resp = requests.get('https://apis.tianapi.com/guonei/index?key=ed2804d172389369537515cc60be6b08&num=10')
 if resp.status_code == 200:
    data_model =  resp.json()['result']
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-'*60)