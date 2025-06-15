import requests

APP_ID = "ee10b8e0e13a65dcd5fd7559ec28b1ae3ba41829"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0004021082",
    "cdArea":"12101,12102,12103,12104,12105,12106",
    #"cdCat01": "A1101",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)

#データの種類　国民生活基礎調査 令和５年国民生活基礎調査 世帯 
#エンドポイント　https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
