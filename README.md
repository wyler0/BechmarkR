# BenchmarkR – A Tool for Benchmarking Large Language Models with Trusted Ground Truth at Scale


## Usage

URLs:
/admin
/ingest/ingest_pdf --> Upload a PDF to use for benchmark question generation 
/generate/generate_submission --> Execute a generation. MCQ is not implemented, only FRQ.

I hoped to use hugging face evaluate and datasets libraries to execute evaluation, but time required to setup on-prem Ollama model for this did not fit requirements unfortunately.
/benchmark/...


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
(6) Add OpenAI Key to .env.django file
Write your open ai key on the line "OPENAI_API_KEY=..."

(6) Run Django Server
```
python manage.py runserver
```

