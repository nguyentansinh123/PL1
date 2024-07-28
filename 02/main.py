from bs4 import BeautifulSoup
import requests


html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text

soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:

    job_published_date = job.find("span", class_="sim-posted").span.text

    if 'few' in job_published_date:

        company_name = job.find("h3", class_="joblist-comp-name").text.replace(' ','')
        skills = job.find("span", class_="srp-skills").text.replace(' ','')


        print(f'''
        Company Name : {company_name.strip()}
        Required Skills: {skills.strip()}
        Publish Date: {job_published_date.strip()}
        ''')

        print(' ')