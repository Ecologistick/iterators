import json


class Iteration:

  def __init__(self, data):
    with open(data) as f:
      open_data = json.load(f)
    self.start, self.end, self.data = 0, len(open_data), open_data
    
  def __iter__(self):
    return self

  def __next__(self):
    self.start += 1
    if self.start == self.end:
      raise StopIteration
    country_name = self.data[self.start]['name']['common']
    country_link = "https://en.wikipedia.org/wiki/" + country_name.replace(" ", "_") 
    final_link = country_name + ' - ' + country_link
    return self.start, final_link

 


if __name__ == '__main__':
  with open('country_links.txt', 'w') as country_links_file:
    for result in Iteration("countries.json"):
      number, link = result
      country_links_file.write(f'{link}\n')

  