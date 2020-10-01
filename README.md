# Mission_to_Mars

The project in this repository is an assignment completed for The George Washington University Data Analysis and Visualization Bootcamp.

In this project our goal was to create a website with basic facts about Mars. We wanted these facts, including news sources, to be scraped from the web at the time the website loads. Please read steps that were taken to complete this project.

## Scraping

### Mars News
https://mars.nasa.gov/news/ website was used to get the latest news on Mars using BeautifulSoup, splinter, and pandas in jupyter notebook.

### JPL Mars Space Images - Featured Image
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars website was used to scrape the featured images in full resolution.

### Mars Weather
https://twitter.com/marswxreport?lang=en website was used to scrape the latest tweets on the weather of Mars.

### Mars Facts
https://space-facts.com/mars/ website was used to scrape a table containing facts about the size of mars (Diameter, Mass, etc)

### Mars Hemispheres
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars website was used to scrape images of the different hemisphere of mars in high resolution.

## Flask
* A python script to run all of the scraping code was designed and all of the scraped data was placed into a Python dictionary.

* '/scrape' route which will import the Python script and call the scrape function was created.

## MongoDB:

* A new database and a new collection were created.

* All of the scraped data described above was stored in this  database.

* A route that will query the database and pass the mars data into HTML template was created.

