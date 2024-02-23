# BeautifulSoup4 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# It is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
#
## Common use cases for BeautifulSoup4:
# - Web scraping
# - Data extraction
# - Data cleaning
# - Data transformation
# - Data analysis
# - Data visualization
# - Data storage
#
# Examples of BS4

# Example 1: Parsing HTML

from bs4 import BeautifulSoup

html = """

<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>

</body>
</html>

"""

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())


# Example 2: Navigating the parse tree

soup_html = BeautifulSoup(html, 'html.parser')

print(soup_html.title)
print(soup_html.title.name)
print(soup_html.title.string)
print(soup_html.title.parent.name)
print(soup_html.p)
# print(soup_html.p['class'])
print(soup_html.a)
print(soup_html.find_all('a'))
print(soup_html.find(id='link3'))


# Example 3: Searching the parse tree

soup_search = BeautifulSoup(html, 'html.parser')

print(soup_search.find_all('p'))
print(soup_search.find_all('p')[0])
print(soup_search.find_all('p')[0].get_text())
print(soup_search.find(id='link3'))
# print(soup_search.find(id='link3').get('href'))


# Example 4: Modifying the parse tree

soup_modify = BeautifulSoup(html, 'html.parser')

print(soup_modify.p)
soup_modify.p.string = 'This is a modified paragraph.'
print(soup_modify.p)


# Example 5: Output

soup_output = BeautifulSoup(html, 'html.parser')

print(soup_output.prettify())
print(soup_output.prettify(formatter='html'))
print(soup_output.prettify(formatter='xml'))
print(soup_output.prettify(formatter='minimal'))


