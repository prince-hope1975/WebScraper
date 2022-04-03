import requests
import os
from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)
test_file = open(os.getcwd() + "/index.html")

# soup = BeautifulSoup(page.content, "html.parser")
soup = BeautifulSoup(test_file, "html.parser")

print(soup.find_all(class_="styles_subitem__EWugG"))
add = soup.find_all(class_="styles_subitem__EWugG")
file = open("index.html", "w")
for a in add:
    print(a)
    file.write(a)
file.close()


# results = soup.find(id="ResultsContainer")
# job_elements = results.find_all("div", class_="card-content")

# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# print(results.prettify())
# print(page.text)