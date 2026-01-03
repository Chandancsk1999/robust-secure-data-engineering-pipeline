<<<<<<< HEAD
Project structure:-

my\_project/

├── docs/

│   └── readme.md

├── resources/

│   ├── \_\_init\_\_.py

│   ├── dev/

│   │    ├── config.py

│   │    └── requirement.txt

│   └── qa/

│   │    ├── config.py

│   │    └── requirement.txt

│   └── prod/

│   │    ├── config.py

│   │    └── requirement.txt

│   ├── sql\_scripts/

│   │    └── table\_scripts.sql

├── src/

│   ├── main/

│   │    ├── \_\_init\_\_.py

│   │    └── delete/

│   │    │      ├── aws\_delete.py

│   │    │      ├── database\_delete.py

│   │    │      └── local\_file\_delete.py

│   │    └── download/

│   │    │      └── aws\_file\_download.py

│   │    └── move/

│   │    │      └── move\_files.py

│   │    └── read/

│   │    │      ├── aws\_read.py

│   │    │      └── database\_read.py

│   │    └── transformations/

│   │    │      └── jobs/

│   │    │      │     ├── customer\_mart\_sql\_transform\_write.py

│   │    │      │     ├── dimension\_tables\_join.py

│   │    │      │     ├── main.py

│   │    │      │     └──sales\_mart\_sql\_transform\_write.py

│   │    └── upload/

│   │    │      └── upload\_to\_s3.py

│   │    └── utility/

│   │    │      ├── encrypt\_decrypt.py

│   │    │      ├── logging\_config.py

│   │    │      ├── s3\_client\_object.py

│   │    │      ├── spark\_session.py

│   │    │      └── my\_sql\_session.py

│   │    └── write/

│   │    │      ├── database\_write.py

│   │    │      └── parquet\_write.py

│   ├── test/

│   │    ├── scratch\_pad.py.py

│   │    └── generate\_csv\_data.py







\# Secure End-to-End Data Engineering Pipeline



\## Overview

Production-grade ETL platform built using AWS, PySpark, and MySQL for ingesting raw data, validating schemas, transforming datasets, and generating analytics-ready data marts.



\## Architecture

S3 → Local Staging → Validation → Spark Transformations → Dimensional Modeling → Data Marts → S3 (Parquet) + MySQL



\## Key Features

\- Secure encryption \& decryption

\- Schema validation \& data quality checks

\- Staging \& metadata tracking

\- Error handling \& recovery

\- Partitioned Parquet storage

\- Customer \& Sales analytics data marts

\- Dev/QA/Prod configuration support



\## Tech Stack

Python, PySpark, AWS S3, MySQL, Spark SQL, Parquet



=======
# robust-secure-data-engineering-pipeline
Production-grade data engineering pipeline using AWS, Spark and MySQL
>>>>>>> 0047d80d617a8c8b6618b40654672d7158e8a0b0
