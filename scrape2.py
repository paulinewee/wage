from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# Specify the path to your ChromeDriver
CHROMEDRIVER_PATH = 'C:\\Program Files (x86)\\chromedriver.exe'

l = list()
o = {}

# Update the URL with your actual API key
TARGET_URL = "https://api.scrapingdog.com/scrape?api_key=6553d1417df6ba70399b7d26&url=https://www.glassdoor.com/Job/new-york-python-jobs-SRCH_IL.0,8_IC1132348_KO9,15_IP3.htm?includeNoSalaryJobs=true&pgc=AB4AAoEAPAAAAAAAAAAAAAAAAfkQ90AAdwEBAQtEzo8VunEQLF8uBoWr%2BRnCsnMFj0JNOLbRUXIkLkFAzjjZlKDW1axVwiTVV%2BbXo8%2BX471WNF8IEWPMdAwCPhbzQe1T1HHMEVPYFwQLM8h1NnGMDPcEwo7tpQ7XL65R7DMDR26n0NhBU7lFGCODAwxNTsJRAAA%3D&dynamic=false"

# Use a different variable name for the driver
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

driver.get(TARGET_URL)

# Allow time for the page to load (you might need to adjust the sleep duration)
time.sleep(5)

resp = driver.page_source
driver.quit()  # Use quit() instead of close() to close the entire browser

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

df = pd.DataFrame(l)
df.to_csv('jobs.csv', index=False, encoding='utf-8')
