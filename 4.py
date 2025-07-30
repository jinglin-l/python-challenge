import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

response = urllib.request.urlopen(url)
n = 500

while n > 0: 
    response = urllib.request.urlopen(url)
    import re
    content = response.read().decode("utf-8")
    match = re.search(r"nothing is (\d+)", content)

    if not match and content.endswith("Yes. Divide by two and keep going."):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={int(int(url.split('=')[-1]) / 2)}"
    elif match:
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={match.group(1)}"
    else:
        print(content)
        break
    n -= 1
