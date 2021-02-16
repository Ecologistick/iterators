import json


class Iteration:

  def __init__(self, start, end, data):
    self.start, self.end = start-1, end
    
  def __iter__(self):
    return self

  def __next__(self):
    self.start += 1
    if self.start == self.end:
      raise StopIteration
    return self.start



def open_file(file):
  with open(file) as f:
    data = json.load(f)
  return data


def create_link(country):
  country = country.replace(" ", "_")
  return "https://en.wikipedia.org/wiki/" + country


if __name__ == '__main__':
  f = open("links.txt", "w")
  data =  open_file("countries.json")
  for item in Iteration(0, len(data), "countries.json"):
    f.write(data[item]['name']['common'] +' - ' + create_link(data[item]['name']['common']+ '\n'))
  f.close()