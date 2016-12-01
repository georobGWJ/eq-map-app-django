import http.client

conn = http.client.HTTPConnection("earthquake.usgs.gov")

headers = {
    'cache-control': "no-cache",
    }

conn.request("GET", "/fdsnws/event/1/query?format=csv&starttime=1900-01-01&endtime=2016-11-09&minmagnitude=3&latitude=37.784&longitude=-122.395&maxradiuskm=50", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))