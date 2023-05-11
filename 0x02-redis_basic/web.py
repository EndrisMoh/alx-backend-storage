#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
import requests
redc = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ Get a page and cache the value"""
    redc.set(f"cached:{url}", count)
    resp = requests.get(url)
    redc.incr(f"count:{url}")
    redc.setex(f"cached:{url}", 10, redc.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
