
# * Create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

# * Store the return value in Mongo as a Python dictionary.

# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd 
import requests 
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_mars_news():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
   
    html = browser.html
    soup = bs(html, "html.parser")
    
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="rollover_description_inner").text

    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p

    browser.quit()
    return mars_data

def scrape_mars_images():
    browser = init_browser()
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(iamges_url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    images = soup.find_all('a', class_="fancybox")
    img_list = []
    for image in images:
        img = image['data-fancybox-href']
        img_list.append(img)
    
    featured_image_url = 'https://www.jpl.nasa.gov' + img
    featured_image_url

    mars_data['featured_image_url'] = featured_image_url 
    
    browser.quit()
    return mars_data

def scrape_mars_weather():
    browser = init_browser()
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    twit = t_soup.find_all("div", attrs={"data-testid":"tweet"} )
    for x in twit[1]:
        print(x.text)

        
    mars_data['weather_tweet'] = twit

    browser.quit()
    return mars_data

def scrape_mars_facts():
    browser = init_browser()
    facts_url = "http://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    mars_facts = pd.read_html(facts_url)
    
    mars_df = mars_facts[0]
    mars_df.columns = ['Description','Value']
    mars_df.set_index('Description', inplace=True)

    facts = mars_df.to_html()

    mars_data['mars_facts'] = facts

    browser.quit()
    return mars_data

def scrape_mars_hemispheres():
    browser = init_browser()
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    base_url = usgs_url.split("/search")
    images = h_soup.find_all("div", class_="description")

    hemisphere_image_urls = []
    for image in hemispheres:
        hems = {}
    
        hems_titles = image.find("h3").text
        hems["Title"] = hems_titles
    
        hems_url = image.find("a", class_="itemLink product-item")["href"]
        hems_links = base_url[0] + hems_url
    
        browser.visit(hems_links)
        html = browser.html
        hl_soup = bs(html, 'html.parser')
        image_urls = hl_soup.find("div", class_="downloads").find("ul").find("li").find('a')["href"]
        hems["URL"] = image_urls
    
        hemisphere_image_urls.append(hems)
        
    mars_data['mars_hemispheres'] = hemisphere_image_urls      

    browser.quit()
    return mars_data