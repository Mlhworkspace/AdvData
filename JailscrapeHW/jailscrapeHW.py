# i realize that I commented under the code and not above, will do differently next time
import requests, mechanize
# import requests and mechanize functions 
from bs4 import BeautifulSoup
#import the bs4 function set from Beautifulsoup
url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=10/31/2017'
#sets url variable to this website
br = mechanize.Browser()
# create variable br which utilizes the "mechanize" object and the "browser" method 
br.open(url)
# mechanize method to open the url
html = br.response().read()
# sets html to the mechanize browser methods of response and read

soup = BeautifulSoup(html, "html.parser")
# Transform the HTML into beautifulsoup object

main_table = soup.find('table',
# assigns main_table to the soup and to find the 'table' tag and ignore the rest
    
)
# From id to mrc_main_table is what is going to not be ignored
row_list = main_table.find_all('tr')
#establishes the "row_list" variable. Find each table row/select each table row
for r in row_list:
	# sets loop for every "r" in row list

    cell_list = r.find_all('td')
    # set variable cell_list for every cell with __ with the find_all method

    if len(cell_list) > 0:
    	# if the length of "cell_list " is greater than 0
        for c in cell_list:
        	# or each object in cell_kust
            print c.text.strip()
# print the text of each cell and removes the leading and trailing characters
        print '----------'
        # print '____________'

print 'IT WORKED!'
# print 'it worked' when the code works