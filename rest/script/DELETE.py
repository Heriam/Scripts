import requests

url = "http://192.168.56.99/sdn/seerengine/v1.0/collectors/"

collectors = eval(str(requests.get(url).content,encoding = "utf-8"))["collectors"]
for collector in collectors:
    resp = requests.delete(url=url+collector.get("id"))
    print(resp.status_code)