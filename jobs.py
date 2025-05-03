from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    print("Enter Skills You Lack")
    unfamiliar_skills = input('>')
    print(f"filtering out: {unfamiliar_skills}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        date_posted = job.find('span', class_ = 'sim-posted').text
        if 'few' in date_posted:
            job_title = job.find('h2', class_ = 'heading-trun').text.strip()
            company_name = job.find('h3', class_ = 'joblist-comp-name').text
            skills = list(job.find('div', class_='more-skills-sections').stripped_strings)
            experience_level = job.find('i', class_='srp-icons experience').next_sibling.strip()
            application_link = job.a['href']
            if unfamiliar_skills not in skills:
                print(f"Job Title: {job_title}")
                print(f"Company Name: {company_name.strip()}")
                print(f"Skills: {skills}")
                print(f"Experience: {experience_level} ")
                print(f"View Job: {application_link}")
                print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} seconds...")
        time.sleep(time_wait * 60)











