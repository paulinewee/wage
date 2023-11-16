# in this project, we're going to:
# 1. Scrape the Glassdoor website for job postings
# 2. 

from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

l = list()
o = {}

target_url = "https://www.glassdoor.com/Job/new-york-python-jobs-SRCH_IL.0,8_IC1132348_KO9,15.htm?clickSource=searchBox"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get(target_url)

driver.maximize_window()

time.sleep(2)

resp = driver.page_source

driver.close()

# bs4
soup = BeautifulSoup(resp, 'html.parser')

allJobsContainer = soup.find("ul", {"class": "JobsList_jobsList__Ey2Vo"})


# Check if the element was found
if allJobsContainer:
    allJobs = allJobsContainer.find_all("li")

    for job in allJobs:
        try:
            o["name-of-company"] = job.find("div", {"class": "EmployerProfile_employerInfo__GaPbq"}).text
        except:
            o["name-of-company"] = None

        try:
            o["name-of-job"] = job.find("a", {"class": "JobCard_seoLink__WdqHZ"}).text
        except:
            o["name-of-job"] = None

        try:
            o["location"] = job.find("div", {"class": "JobCard_location__N_iYE"}).text
        except:
            o["location"] = None

        try:
            o["salary"] = job.find("div", {"class": "JobCard_salaryEstimate___m9kY"}).text
        except:
            o["salary"] = None

        l.append(o)

        o = {}

print(l)
print('done')
