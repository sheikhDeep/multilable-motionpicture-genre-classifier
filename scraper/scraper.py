from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

genres = ['comedy', 'sci-fi', 'horror', 'romance', 'action', 'thriller', 'drama', 'mystery', 'crime', 'adventure', 'fantasy']
columns = ['title', 'description', 'genres']

motion_picture_details = []

if __name__ == "__main__":

    # Selenium web-driver path
    webdriver_path = ""
    driver = webdriver.Chrome(webdriver_path)
    
    # Base imdb url(list type) for scraping
    base_url = ""
    driver.get(base_url)

    # Type the number of pages you want to scrape in the range parameter
    for i in range(400):
        rows = driver.find_elements(By.CLASS_NAME, 'lister-item')
        for row in rows:
            title = row.find_element(By.CLASS_NAME, 'lister-item-header').find_element(By.TAG_NAME, 'a').text
            descripton = row.find_element(By.CSS_SELECTOR, 'div[class="lister-item-content"] > p:nth-of-type(2)').text
            genres = row.find_element(By.CLASS_NAME, 'lister-item-content').find_element(By.CLASS_NAME, 'genre').text

            contains = genres.find(",")
            if contains != -1:
                genres = genres.split(', ')
            else:
                l = []
                l.append(genres)
                genres = l
            
            tvc = {"title" : title, "description" : descripton, "genres" : genres}
            motion_picture_details.append(tvc)

       
            df = pd.DataFrame(data=motion_picture_details, columns=columns)
            df.to_csv("motion_picture_details.csv", index=False)

        try:
            button = driver.find_element(By.ID, 'main').find_element(By.CLASS_NAME, 'next-page')
            ActionChains(driver).move_to_element(button).click(button).perform()
            time.sleep(2)
        except:
            print("No next buttons")
        
    
    driver.close()