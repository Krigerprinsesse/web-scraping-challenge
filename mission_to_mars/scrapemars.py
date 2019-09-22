import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import re

def init_browser():
    executable_path = {"executable_path": "../chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    url_nasa = 'https://mars.nasa.gov/news/'
    response = requests.get(url_nasa)
    soup = BeautifulSoup(response.text, 'html.parser')


    results = soup.find_all('div', class_='content_title')
    news_title = results[0].text.split('\n\n')[1]

    results2 = soup.find_all('div', class_='rollover_description_inner')
    news_p = results2[0].text.split('\n')[1]

    print(news_title)
    print(news_p)

    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': '..\chromedriver.exe'}

    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_jpl)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.is_element_present_by_tag("more info", wait_time=20)
    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    word = 'Full-Res JPG: '
    stringList = soup.find_all('p')
    for myString in stringList:
        if word in myString:
            featured_image_url = myString.a['href']
            print(f'Image link: {featured_image_url}')

    url_mars_weather = 'https://twitter.com/marswxreport?lang=en'

    response = requests.get(url_mars_weather)

    soup = BeautifulSoup(response.text, 'html.parser')
    mars_weather = soup(text=re.compile('InSight sol'))[0]
    print(mars_weather)

    url_mars_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_mars_facts)
    marsfactsdf = tables[1]
    marsfactsdf.columns = ['Measurement', 'Value']
    marsfactsdf
    html_table = marsfactsdf.to_html()


    url_mars_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    executable_path = {'executable_path': '..\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_mars_hemispheres)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    myLinks = soup.find_all('div', class_='item')

    myLink = myLinks[0].find('h3').text
    browser.click_link_by_partial_text(myLink)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi1_title_en = soup.find_all('h2', class_='title')[0].text
    hemi1_title = hemi1_title_en.split(' Enhanced')[0]
    print(hemi1_title)

    hemi1_link = soup.find('div', class_='downloads').find_all('li')[1].find('a')['href']


    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_mars_hemispheres)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    myLinks = soup.find_all('div', class_='item')

    myLink = myLinks[1].find('h3').text
    browser.click_link_by_partial_text(myLink)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi2_title_en = soup.find_all('h2', class_='title')[0].text
    hemi2_title = hemi2_title_en.split(' Enhanced')[0]
    print(hemi2_title)

    hemi2_link = soup.find('div', class_='downloads').find_all('li')[1].find('a')['href']


    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_mars_hemispheres)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    myLinks = soup.find_all('div', class_='item')

    myLink = myLinks[2].find('h3').text
    browser.click_link_by_partial_text(myLink)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi3_title_en = soup.find_all('h2', class_='title')[0].text
    hemi3_title = hemi3_title_en.split(' Enhanced')[0]
    print(hemi3_title)

    hemi3_link = soup.find('div', class_='downloads').find_all('li')[1].find('a')['href']


    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_mars_hemispheres)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    myLinks = soup.find_all('div', class_='item')

    myLink = myLinks[3].find('h3').text
    browser.click_link_by_partial_text(myLink)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi4_title_en = soup.find_all('h2', class_='title')[0].text
    hemi4_title = hemi4_title_en.split(' Enhanced')[0]
    print(hemi4_title)

    hemi4_link = soup.find('div', class_='downloads').find_all('li')[1].find('a')['href']

    hemisphere_image_urls = [
        {'title': hemi1_title, 'img_url': hemi1_link,
        'title': hemi2_title, 'img_url': hemi2_link,
        'title': hemi3_title, 'img_url': hemi3_link,
        'title': hemi4_title, 'img_url': hemi4_link}
    ]
    pageData = {
    'mars_news_title': news_title,
    'mars_news_blurb': news_p,
    'featured_image_url': featured_image_url,
    'mars_weather': mars_weather,
    'html_table': html_table,
    'hemisphere_image_urls': hemisphere_image_urls
    }

    return pageData