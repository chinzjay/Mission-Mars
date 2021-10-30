.. code:: ipython3

    #Import Splinter and BeautifulSoup
    from splinter import Browser
    from bs4 import BeautifulSoup as soup
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd

.. code:: ipython3

    #Setup splinter
    executable_path={'executable_path':ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)


.. parsed-literal::

    [WDM] - 
    
    [WDM] - ====== WebDriver manager ======
    [WDM] - Current google-chrome version is 94.0.4606
    [WDM] - Get LATEST driver version for 94.0.4606
    [WDM] - Driver [C:\Users\chinn\.wdm\drivers\chromedriver\win32\94.0.4606.61\chromedriver.exe] found in cache
    

.. code:: ipython3

    # Visit the mars nasa news site
    url='https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)




.. parsed-literal::

    True



.. code:: ipython3

    #set up the HTML parser
    html=browser.html
    news_soup=soup(html, 'html.parser')
    slide_elem=news_soup.select_one('div', class_='list.text')

.. code:: ipython3

    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title=news_soup.find('div', class_='content_title').text
    news_title




.. parsed-literal::

    "Media Get a Close-Up of NASA's Mars 2020 Rover"



.. code:: ipython3

    # Use the parent element to find the paragraph text
    news_p=news_soup.find('div', class_='article_teaser_body').text
    news_p




.. parsed-literal::

    "The clean room at NASA's Jet Propulsion Laboratory was open to the media to see NASA's next Mars explorer before it leaves for Florida in preparation for a summertime launch."



### Featured Images

.. code:: ipython3

    # Visit URL
    url='https://spaceimages-mars.com'
    browser.visit(url)

.. code:: ipython3

    # Find and click the full image button
    full_image_elem=browser.find_by_tag('button')[1]
    full_image_elem.click()

.. code:: ipython3

     # Parse the resulting html with soup
    html=browser.html
    img_soup=soup(html, 'html.parser')

.. code:: ipython3

    # Find the relative image url
    img_url_rel=img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel




.. parsed-literal::

    'image/featured/mars1.jpg'



.. code:: ipython3

    # Use the base URL to create an absolute URL
    img_url=f'https://spaceimages-mars.com/{img_url_rel}'
    img_url




.. parsed-literal::

    'https://spaceimages-mars.com/image/featured/mars1.jpg'



.. code:: ipython3

    df=pd.read_html('https://galaxyfacts-mars.com/')[0]
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    df.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Mars</th>
          <th>Earth</th>
        </tr>
        <tr>
          <th>description</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Mars - Earth Comparison</th>
          <td>Mars</td>
          <td>Earth</td>
        </tr>
        <tr>
          <th>Diameter:</th>
          <td>6,779 km</td>
          <td>12,742 km</td>
        </tr>
        <tr>
          <th>Mass:</th>
          <td>6.39 × 10^23 kg</td>
          <td>5.97 × 10^24 kg</td>
        </tr>
        <tr>
          <th>Moons:</th>
          <td>2</td>
          <td>1</td>
        </tr>
        <tr>
          <th>Distance from Sun:</th>
          <td>227,943,824 km</td>
          <td>149,598,262 km</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df.to_html()




.. parsed-literal::

    '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Mars</th>\n      <th>Earth</th>\n    </tr>\n    <tr>\n      <th>description</th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Mars - Earth Comparison</th>\n      <td>Mars</td>\n      <td>Earth</td>\n    </tr>\n    <tr>\n      <th>Diameter:</th>\n      <td>6,779 km</td>\n      <td>12,742 km</td>\n    </tr>\n    <tr>\n      <th>Mass:</th>\n      <td>6.39 × 10^23 kg</td>\n      <td>5.97 × 10^24 kg</td>\n    </tr>\n    <tr>\n      <th>Moons:</th>\n      <td>2</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>Distance from Sun:</th>\n      <td>227,943,824 km</td>\n      <td>149,598,262 km</td>\n    </tr>\n    <tr>\n      <th>Length of Year:</th>\n      <td>687 Earth days</td>\n      <td>365.24 days</td>\n    </tr>\n    <tr>\n      <th>Temperature:</th>\n      <td>-87 to -5 °C</td>\n      <td>-88 to 58°C</td>\n    </tr>\n  </tbody>\n</table>'



.. code:: ipython3

    browser.quit()

