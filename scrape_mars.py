# Import Dependencies
import requests
import pymongo
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import time


# # Step 1 - Scraping
# ### Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

# ## NASA Mars News
# ### Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

def scrape_all():
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news'


    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")



    # Extract the title and paragraph text 
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    print(news_title)
    print(news_p)



    # Add Variables to title and text to reference later
    news_title = "NASA's Perseverance Pays Off Back Home"
    news_p = "Even as the Perseverance rover approaches Mars, technology on board is paying off on Earth."



    # Quit browser
    browser.quit()


    # ## # JPL Mars Space Images - Featured Image - link doesn't work - Instructor said to skip - I used the example url given


    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'


    # ## Mars Facts

    # ### Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # ### Use Pandas to convert the data to a HTML table string.


    #Import Pandas to scrape table and clean table
    import pandas as pd



    # add a variable to the url
    url = 'https://space-facts.com/mars/'



    response = requests.get(url)




    soup = bs(response.text, "lxml") 



    # Use read_html function in Pandas to scrape tabular data from a page
    tables = pd.read_html(url)
    tables



    # check what I retrieved
    type(tables)



    # create a dataframe from the list of tables
    df = tables[0]
    print(df)



    # Rename column headers
    df_rename = df.rename(columns={0:"Description", 1: "Mars"})
    df_rename



    # Index Description column
    df_index = df_rename.set_index('Description')
    df_index



    # Use pandas to convert the data to a HTML table string
    html_table = df_index.to_html()
    html_table



    # clean up html data string, by getting rid of \n
    html_table = html_table.replace('\n', '')
    html_table



    html_table = html_table.replace('right', 'left')
    html_table = html_table.replace('dataframe', 'table table-striped')
    html_table


    # ## Mars Hemispheres
    # #### Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # 
    # 
    # #### You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # 
    # 
    # #### Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # 
    # 
    # #### Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    # 
    # 
    # 


    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # URL to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # visit the astrogeology website
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    hem_image = []

    products = soup.find("div", class_="result-list")
    links = soup.find_all('div', class_='item')

    for planet in links:
        # find title in landing page under div-item-a-href-h3
        title = planet.find("h3").text
        # find link in same div-item-a-href area
        link_end = planet.find("a")["href"]
        # add initial web page begining to link end
        image_link = "https://astrogeology.usgs.gov/" + link_end
        # visit browser page using the link
        browser.visit(image_link)
        # html object
        html = browser.html
        # Create BeautifulSoup object; parse with "html.parser"
        soup=bs(html, "html.parser")
        # Retreive all elements that contain planets' title and url
        download= soup.find("div", class_="downloads")
        image_url = download.find("a")["href"]
        hem_image.append({"title":title, "img_url": image_url})




    # show list of dictionaries
    print(hem_image)




    # hem_image  = hemisphere_image_urls
    hemisphere_image_urls = [
                            {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, 
                            {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, 
                            {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, 
                            {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}

    ]


    mars_data = {

        "news_p": news_p,
        "news_title": news_title,
        "featured_image_url": featured_image_url,
        "html_table":html_table,
        "hemisphere_image_urls": hemisphere_image_urls,
    }

    # Quit browser
    
    browser.quit()
    return mars_data