import json

x = '{ "ip": "8.8.8.8", "version": "IPv4" }'

ipinfo = json.loads(x)
ips = ipinfo["ip"]
print(ips)

y = json.dumps(x)
print(y)

print(json.dumps(("hello","guys")))
print(json.dumps(42))