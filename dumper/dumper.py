from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import requests
import json

MAX_THREADS = 256

database=[]

def save():
    f=open("database0-10k.bin","w")
    for medicine in database:
        f.write(str(medicine)+"\n")
    f.close()

def download_url(counter):
    r=requests.get(f"https://search.sastasundar.com/product_find?product_id={counter}")
    obj=json.loads(r.text)
    if obj["items"]!=[]:
        database.append(obj["items"][0]["ProductName"])
    print(f"Done {counter}")

futures=[]
try:
    for i in range(0,10000):
        with PoolExecutor(max_workers=MAX_THREADS) as executor:
            futures.append(executor.submit(download_url, str(i)))
except KeyboardInterrupt:
    save()

save()
