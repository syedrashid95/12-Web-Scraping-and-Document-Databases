# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import pymongo
from selenium import webdriver

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.mission_to_mars_db
mars_info = db.mission_to_mars_info

# Set Executable Path & Initialize Chrome Browser
def init_browser():
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)

def scrape():
    browser = init_browser()
    mars_data= {}
#Scrape title and paragraph
itle = soup.find("div",class_="content_title").text
paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {title}")
print(f"Para: {paragraph}")

def scrape_feature_image():
    
main_url = 'https://www.jpl.nasa.gov'

jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

browser.visit(jpl_url)
time.sleep(1)
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

#Find the Feautured Image
featured_image = []

for image in image_soup.find_all('div',class_="img"):
    featured_image.append(image.find('img').get('src'))

#Find the image URL


feature_image_url = "https://www.jpl.nasa.gov/" + feature_image

feature_image_dict = {"image": feature_image_url}

return feature_Image_dict

#Parse HTML with Beautiful Soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

# Navigating to Twitter
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)

# Pulling latest tweet from @marswxreport
html = browser.html
tweet_soup = BeautifulSoup(html, 'html.parser')
mars_weather = tweet_soup.find("p", class_="tweet-text").text
print(mars_weather)

# Navigating to Mars facts site
url_facts = "https://space-facts.com/mars/"
browser.visit(url_facts)

# Using pandas to scrape table
tables = pd.read_html(facts_url)

 # Isolating df from list and minor clean-up
df = pd.DataFrame(tables[0])

df.columns=['tables','Result']

df.to_html

# Navigating to hemisphere image site

hemispheres_main_url = 'https://astrogeology.usgs.gov'
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)

# Create our Path
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemi_url)

#Create our database
hemi_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop
    browser.find_by_css("h3")[item].click()
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    hemisphere["title"] = browser.find_by_css("h2.title").text
    hemi_url.append(hemisphere)
    browser.back
    return hemi_urls