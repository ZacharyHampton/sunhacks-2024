import os

proxies = [
    {
        "http": 'http://' + ':'.join(proxy.split(':')[2:]) + "@" + ':'.join(proxy.split(':')[:-2]),
        "https": 'http://' + ':'.join(proxy.split(':')[2:]) + "@" + ':'.join(proxy.split(':')[:-2])
    }
    for proxy in open("../proxies.txt").read().splitlines()
]