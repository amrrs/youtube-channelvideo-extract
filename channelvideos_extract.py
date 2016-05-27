import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

browser = webdriver.Chrome()

#change your channel url here

browser.get("https://www.youtube.com/user/googleindia/videos")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")


#considering the number of videos in your channel change this below figure

no_of_loadmore = 100

try:
    while no_of_loadmore:
        browser.find_element_by_class_name("load-more-text").click()
        time.sleep(1)
        no_of_loadmore-=1
except:
    pass

#scrape the content by xpath

post_elems = browser.find_elements_by_xpath('//div/h3/a')
links = browser.find_elements_by_xpath('//*[@id="channels-browse-content-grid"]/li/div/div[1]/div[2]/h3/a')

with open('googleindia_vids.csv', 'w',newline='') as csvfile:
    autowriter = csv.writer(csvfile)
    autowriter.writerow(['Title','URL'])
    for i in range(0,len(post_elems)-1):
        autowriter.writerow([post_elems[i].text,links[i].get_attribute('href')])

#iterate thru the elements and print it

for post in post_elems:
  print(post.text) 

for link in links:
    print(link.get_attribute('href'))




