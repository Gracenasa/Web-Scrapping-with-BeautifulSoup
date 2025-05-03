# 🕸 Python Job Scraper with PostgreSQL Integration

This is a Python-based job scraper built during Week 3 of my Python learning journey. The goal is to scrape job listings from [TimesJobs](https://www.timesjobs.com/), extract key information, and store it in a PostgreSQL database for further use (dashboards, alerts, analytics, etc.).

I built this following a Youtube tutorial by [JimShapedCoding](https://youtu.be/XVv6mJpFOb0?si=awuaneLIlvMLXoKL) 

Note that the tutorial doesn't include database integration

---

## 🚀 What This Script Does

- **Scrapes real job postings** from a live job board
- **Extracts** key fields:
  - Job Title
  - Company Name
  - Required Skills
  - Experience Level
  - Link to Apply
  - Timestamp
- **Saves all jobs into a PostgreSQL database**
- **Avoids duplicates** using `ON CONFLICT DO NOTHING`
- **Runs every 10 minutes** in a continuous loop

---

## 📌 Key Technologies

- `BeautifulSoup` for HTML parsing  
- `requests` for pulling job listing pages  
- `psycopg2` for PostgreSQL integration  
- `time.sleep()` for scheduled scraping

---

## 🧱 Sample Table Structure

```sql
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    company_name TEXT,
    skills TEXT,
    experience TEXT,
    job_link TEXT UNIQUE,
    job_title TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
