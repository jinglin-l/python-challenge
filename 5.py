from urllib.request import urlopen
import pickle

raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
# print(raw)


# print(pickle.loads(raw))

# inspect shape 
def count_dimensions(data):
    if not isinstance(data, list):
        return 0
    return 1 + max(count_dimensions(item) for item in data) if data else 1

print("Dimensions:", count_dimensions(pickle.loads(raw)))


def ascii_art(data):
    for row in data:
        for tup in row:
            print(tup[0] * tup[1], end="")
        print()
ascii_art(pickle.loads(raw))



