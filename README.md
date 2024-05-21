# BenchmarkR – A Tool for Benchmarking Large Language Models with Trusted Ground Truth at Scale


## Usage

URLs:
/admin
/ingest/ingest_pdf
/generate/generate_frq



## Setup

(1) Install Requirepents
```
conda env create -f "env.yml
```
(2) Run Redis
```
docker-compose up 
```
(3) Run Celery Workers & flower
```
celery -A benchmarkR worker --loglevel=info 
```
```
celery --broker=redis://localhost:6379// flower
```
(4) Setup Database
```
python manage.py makemigrations; python manage.py migrate;
```
(5) Add superuser
```
python manage.py createsuperuser
```
(6) Run Django Server
```
python manage.py runserver;
```
