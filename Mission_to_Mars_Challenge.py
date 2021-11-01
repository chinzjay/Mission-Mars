
#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Setup splinter
executable_path={'executable_path':ChromeDriverManager().install()}
browser=Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url='https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


#set up the HTML parser
html=browser.html
news_soup=soup(html, 'html.parser')
slide_elem=news_soup.select_one('div', class_='list.text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title=news_soup.find('div', class_='content_title').text
news_title


# Use the parent element to find the paragraph text
news_p=news_soup.find('div', class_='article_teaser_body').text
news_p


#  ### Featured Images

# Visit URL
url='https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem=browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html=browser.html
img_soup=soup(html, 'html.parser')


# Find the relative image url
img_url_rel=img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url=f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df=pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df.head()


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# Hemispheres
# 

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

html=browser.html
hem_soup=soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.  
for i in range(4):
    #create empty dictionary
    hemispheres={}
    browser.find_by_css('a.product-item h3')[i].click()
    elem=browser.find_link_by_text('Sample').first
    img_url=elem['href']
    title=browser.find_by_css("h2.title").text
    hemispheres["img_url"]=img_url
    hemispheres["title"]=title
    hemisphere_image_urls.append(hemispheres)
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()


