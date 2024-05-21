# BenchmarkR – A Tool for Benchmarking Large Language Models with Trusted Ground Truth at Scale

## Setup

(1) Install Requirepents
```
conda env create -f "env.yml
```
(2) Run Redis
```
docker-compose up 
```
(3) Run Celery Workers
celery -A benchmarkR worker --loglevel=info 