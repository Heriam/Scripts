import requests
import random
from jinja2 import Environment, PackageLoader

url = "http://192.168.56.99/sdn/seerengine/v1.0/collectors"
env = Environment(loader=PackageLoader("rest"))
template = env.get_template("body.json")
count = 5000

def _get_random_ip():
    return "%s.%s.%s.%s" % (random.randint(1,254), random.randint(1,254), random.randint(1,254), random.randint(1,254))

for i in range(count):
    content = template.render(name=str(i), port=random.randint(0, 65535), ip_address=_get_random_ip())
    response = requests.post(url, content)
    print(response.content)