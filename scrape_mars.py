#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:07:32 2020

@author: carlyfabris
"""

from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def scrape():
    # Beautiful Soup Start up
    
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(2)
    
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # Mars News
    
    #Finding the artilce 
    article_location = soup.find('div', class_="list_text")
    #Finding the title of the article
    title_location = article_location.find('div', class_="content_title")
    article_title = title_location.find('a').text
    #Finding the body of the article
    body= article_location.find('div', class_="article_teaser_body").text
    print(f"{article_title} : {body}")
    
    
    # Mars Images
    
    
    image_website = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_website)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('a', class_="fancybox")['data-fancybox-href']
    image_url = f"https://www.jpl.nasa.gov{image_url}"
    image_url
    
    # Mars Weather
    
    
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    mars_weather = tweet.span.text
    mars_weather = mars_weather.replace('\n',' ')
    mars_weather
    
    # Mars Facts
    
    
    table_url = "https://space-facts.com/mars/"
    tables = pd.read_html(table_url)
    tables
    
    mars_info = tables[0]
    mars_info = mars_info.rename(columns = {0:"Description", 1:"Value"})
    
    # Info back to html
    mars_html = mars_info.to_html(index = False, classes="table-striped")
    
    # Mars Hemispheres
    
    
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    hemispheres = ["Cerberus Hemisphere", "Schiaparelli Hemisphere",
                 "Syrtis Major Hemisphere", "Valles Marineris Hemisphere"]
    hemisphere_images_urls = []

    for sphere in hemispheres:
        browser.click_link_by_partial_text(sphere)
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
        image_link = soup.find("img", class_="wide-image")["src"]
        image_link = f"https://astrogeology.usgs.gov{image_link}"
        title = sphere
        hemisphere_dict = {"Title":title, "Img_URL":image_link}
        hemisphere_images_urls.append(hemisphere_dict)
        browser.visit(hemispheres_url)


    mars_dict = {"News_Title": article_title,
                 "News": body,
                 "Featured_Mars_Image": image_url,
                 "Mars_Weather":mars_weather,
                 "Mars_Table":mars_html,
                 "Hemisphere_Info":hemisphere_images_urls}
    return mars_dict


                 




