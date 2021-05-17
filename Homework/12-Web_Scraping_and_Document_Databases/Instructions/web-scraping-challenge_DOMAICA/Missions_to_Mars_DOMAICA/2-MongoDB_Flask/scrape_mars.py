# DEPENDENCIES
import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# mongoDB Setup
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# declare mars_db
db = client.mars_db
# #declare collection inside mars_db name marsdata
marsdata = db.marsdata


# Open Chrome Browser to proceed
# def call_splinter():
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless=False)
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser("chrome", **executable_path, headless=False)

def scrape():

    # Drop current collections in mongoDB so we do
    # not duplicate record each time we run this code
    # marsdata.drop()
    
    ######################
    # MARS NEWS 1st scrape portion
    ######################
    # Visit the NASA news page indicated by instructions
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # HTML Object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.select_one("ul.item_list li.slide")
    # scrape the article title 
    news_title = results.find('div', class_='content_title').text
    # scrape the article subheader / paragraph
    news_paragraph = results.find('div', class_='article_teaser_body').text

    ########################################
    # JPL MARS SPACE IMAGES - FEATURED IMAGE 2nd segment to scrape
    ########################################
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # HTML Object 
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    image_title = soup.find('h1', class_="media_feature_title").text.strip()
    results = soup.find_all('img', class_="headerimage fade-in")
    # loop
    for result in results:
    # image obtained by src
        featured_image_url = result['src']
    # Website Url 
    main_url = 'https://spaceimages-mars.com/'
    # Full url as base + extension website url obtained with scrapped route
    featured_image_url = main_url + featured_image_url
    
    
    ########################################
    # MARS - EARTH FACTS COMPARISON TABLE 3rd segment to scrape
    ########################################
    # Visit Mars Space Images through splinter module
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    extraction_df = pd.read_html(url)
    # make a dataframe with table[0] for mars earth comparison for required html  
    mars_earth_df = extraction_df[0]
    mars_earth_df.rename(columns={0:'Mars - Earth Comparison', 1:'Mars', 2:"Earth"}, inplace=True)
    # drop 1st row. By selecting all rows from first row onwards
    mars_earth_df = mars_earth_df.iloc[1: , :]

    # mars_fact_html = mars_facts_df.to_html(index=False)
    mars_earth_comparison_html = mars_earth_df.to_html(index=False)

    ########################################
    # MARS HEMISPHERES. Last scrapping
    ########################################
    url = "https://marshemispheres.com/"
    browser.visit(url)

    # HTML Object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # TITLES / NAMES
    hemi_names = []
    results = soup.find_all('div', class_="collapsible results")
    hemispheres = results[0].find_all('h3')

    # Get text and store in list
    for name in hemispheres:
        hemi_names.append(name.text)


    # IMAGES
    
    # Search for thumbnail links
    thumbnail_results = results[0].find_all('a')
    thumbnail_links = []
    base_url = "https://marshemispheres.com/"
    for thumbnail in thumbnail_results:
        # If the thumbnail element has an image...
        if (thumbnail.img):
            # then grab the attached link
            thumbnail_url = base_url + thumbnail['href']
            # Append list with links
            thumbnail_links.append(thumbnail_url)
    
    # Search for full images
    full_imgs = []
    
    for url in thumbnail_links:
       
        browser.visit(url)
        
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Scrape each page for the relative image path
        results = soup.find_all('img', class_='wide-image')
        relative_img_path = results[0]['src']
        
        # Combine the reltaive image path to get the full url
        img_link = base_url + relative_img_path
        
        # Add full image links to a list
        full_imgs.append(img_link)

        # create empty list to append dictionary
        mars_db_content = []

        # create empty dictionary
        mars_dictionary = {}

        mars_dictionary['title']= hemi_names
        mars_dictionary['image_url']= full_imgs
        mars_db_content.append(mars_dictionary)

    # Close the browser after scraping
    browser.quit()


    # Return results
    mars_data_insert ={

        'news_title' : news_title,
        'paragraph': news_paragraph,

        'featured_image': featured_image_url,
        'featured_image_title': image_title,
        'images': full_imgs,
        'thumbs': thumbnail_links,
        'titles': hemi_names,

        'facts_table': mars_earth_comparison_html,

        'hemisphere_content': mars_dictionary
        }

    # insert new content returned from scrape into MongoDB collection marsdata
    marsdata.insert_one(mars_data_insert)