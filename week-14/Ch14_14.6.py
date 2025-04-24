import urllib.request
import ssl
import certifi

def fetch_secret():
    url = 'http://thinkpython.com/secret.html'
    context = ssl.create_default_context(cafile=certifi.where())  # Uses certifi properly

    try:
        with urllib.request.urlopen(url, context=context) as response:
            for line in response:
                print(line.decode('utf-8').strip())
    except Exception as e:
        print(f"Failed to fetch the secret message: {e}")

fetch_secret()
