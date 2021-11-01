# Mission-Mars
## Overview
The purpose of this project is to create a web app to display the latest information about the planet Mars including the latest news, the featured images, Mars data and the images of Mars's hemispheres using Splinter, BeautifulSoup and Bootstrap components.

## Results
The full resolution Mars's Hemisphere Images and the titles were scraped for each hemisphere and added to a dictionary using Beautiful Soup and Splinter.
![hemispheres](https://github.com/chinzjay/Mission-Mars/blob/main/Resources/hemispheres.PNG)
|:--:|
|Fig 1. Full Resolution Mars Hemisphere Images scraped and displayed on the web app.|

The scraping.py file was updated to retrieve the full-resolution image URL and title for each hemisphere. 

![code_snippet](https://github.com/chinzjay/Mission-Mars/blob/main/Resources/code_snippet.PNG)
|:--:|
|Fig 2. Function used to scrape data about Mars's hemispheres.|

Mongo database was then updated to contain the full-resolution image URL and title for each hemisphere image. With the updated code, the web app contains the latest news about Mars, the Featured Images, Data about Mars and the Full-Resolution Images and Titles for the hemispheres. Finally the web app was updated to make it mobile-responsive, and additional Bootstrap 3 components were added to style the webpage.
## Summary
Following are the data scraped and displayed on the updated Mars web app.
- Latest news from https://redplanetscience.com/.
- Featured image from https://spaceimages-mars.com/.
- Data about Mars from https://galaxyfacts-mars.com/.
- Image urls and Titles for each hemisphere from https://marshemispheres.com/.
