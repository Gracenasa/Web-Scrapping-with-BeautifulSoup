from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import psycopg2

# --- DATABASE CONNECTION ---
conn = psycopg2.connect(
    host="localhost",
    database="Scrapping",     
    user="postgres",        
    password="__"     
)
cursor = conn.cursor()

def find_jobs():
    print("Scraping jobs...")

    base_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation='
    
    for page in range(1, 6):  # Adjust range for how many pages you want
        url = f"{base_url}&sequence={page}&startPage={page}"
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        if not jobs:
            print(f"No jobs found on page {page}. Stopping.")
            break

        for job in jobs:
            date_posted = job.find('span', class_='sim-posted').text
            if 'few' in date_posted:
                job_title = job.find('h2', class_ = 'heading-trun').text.strip()
                company_name = job.find('h3', class_='joblist-comp-name').text
                skills = list(job.find('div', class_='more-skills-sections').stripped_strings)
                experience_level = job.find('i', class_='srp-icons experience').next_sibling.strip()
                application_link = job.a['href']
                timestamp = datetime.now()

                try:
                    cursor.execute("""
                        INSERT INTO jobs (company_name, job_title, skills, experience, link, timestamp)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (link) DO NOTHING
                    """, (
                        company_name.strip(),
                        job_title,
                        ', '.join(skills),
                        experience_level,
                        application_link,
                        timestamp
                    ))
                    conn.commit()
                    print(f"✔ Inserted: {company_name.strip()} | Page: {page}")
                except Exception as e:
                    print(f"DB insert error: {e}")


if __name__ == '__main__':
    try:
        while True:
            find_jobs()
            time_wait = 10
            print(f"Waiting {time_wait} minutes...\n")
            time.sleep(time_wait * 60)
    finally:
        cursor.close()
        conn.close()

