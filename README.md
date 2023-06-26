# Factoid Finance Source Code
Source code for TSA Project Factoid Finance

## Features
- Authentication System
- Static Pages
- Portfolio Dashboard (List View with Graphs etc)
- Detail Asset View
- Fundamental Analysis
- News Sentiment Analysis
- Scanner
- Watchlist, charts, etc

## Technical Stack
- Django
- HTML/CSS/JS
- PostGres & Redis
- Docker
- Kubernetes
- Github Actions CI/CD
- Logging
- Gunicorn, Nginx
- Vultr full deployment 

## TODO List
Immediate:
    - Clean up template
      - Category News
      - Dashboard
      - Detail Views
    - Stock Screener + Schedule
    - Stock Analysis + Schedule
    
. All User stuff + Stock pages
. Get data and perform calculation
. Automated scraping and crawling
. News Feed analysis
. Redis + Celery
. UI overload
6/23 - 6/26 . Production and Buffer Other stuff

## Usage
Run celery:
```bash
docker-compose exec web /home/myuser/.local/bin/celery -A factoid_finance worker -B -l info
```

## Colorscheme
#81FFD9 - Inside
#051726 - Background
