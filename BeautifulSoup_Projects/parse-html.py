from bs4 import BeautifulSoup
import os

relative_file_path = 'Path/to/html/file/file_name.html'
current_directory = os.getcwd()
absolute_file_path = os.path.join(current_directory, relative_file_path)
file = os.path.abspath(absolute_file_path)


with open(file) as f:
    doc = BeautifulSoup(f, "html.parser")


for heading in doc.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    print(heading.name + ' ' + heading.text.strip())
# print(doc.prettify()) 
# print(doc.title.string)
# head = doc.find('img') ### this is how to access each tags from html doc (head, h1...etc)
# print(head['class']) 

