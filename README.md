# Data Engineering Lifecycle – Analytics Serving Layer

## Problem Statement

Business teams such as Product Analytics, Marketing, and Operations require
fast, reliable access to analytical data to make data-driven decisions.

While raw data is already ingested and transformed in a central data lake,
analytics teams often struggle with:
- Querying large datasets efficiently
- Accessing consistent, business-ready metrics
- Performing ad-hoc analysis without impacting upstream pipelines

The goal of this project is to design and demonstrate an **analytics serving layer**
that exposes curated, query-optimized datasets from a data lake to analytics users.
This enables self-service analytics, faster insights, and scalable reporting
without requiring direct access to raw or intermediate data layers.


## Architecture
![Analytics Serving Architecture](img/architecture.png)

This project represents the **serving layer** of the data engineering lifecycle.

Transformed data is stored in Amazon S3 and queried using Amazon Athena.
The query results are then used in Python to build interactive analytics dashboards.

High-level flow:

Transformed Data (S3)  
→ Amazon Athena (SQL Queries)  
→ Python (Pandas + AWS Wrangler)  
→ Interactive Dashboard (Charts & Widgets)


## Tools and Technologies

- Amazon S3 – Storage for transformed data
- Amazon Athena – Serverless SQL query engine
- AWS Glue – Data transformation (upstream process)
- Python – Data analysis and visualization
- Pandas – Data manipulation
- AWS Wrangler – Athena integration with Python
- Seaborn – Data visualization
- Jupyter Notebook – Interactive analysis and dashboards


## What Is Happening in This Project

In this project, data that has already been transformed using AWS Glue is stored in
Amazon S3 in a structured format suitable for analytics.

Amazon Athena is used to run SQL queries directly on the data stored in S3 without
loading it into a database. These queries retrieve sales-related insights such as
total sales by country, product line, and time period.

The query results are loaded into Python using AWS Wrangler and Pandas.
Interactive dashboards are then built using visualization libraries and widgets,
allowing users to explore sales data dynamically.


## What I Learned

- How the serving layer fits into the data engineering lifecycle
- How Amazon Athena can query data directly from S3 using SQL
- How fact and dimension tables support analytical queries
- How to use AWS Wrangler to connect Athena with Python
- How to build interactive dashboards using Pandas, Seaborn, and widgets
- How transformed data can be easily explored once it is analytics-ready


## Challenges Faced

- Understanding how Athena queries data directly from S3
- Designing efficient SQL joins between fact and dimension tables
- Handling date and time conversions for analytics
- Building interactive dashboards that respond to user inputs
- Ensuring query results are structured correctly for visualization

## Execution and Deployment

This project is executed in a Jupyter Notebook environment.

- Transformed data is already available in Amazon S3
- Amazon Athena is used to execute SQL queries on the data
- Queries are executed using AWS Wrangler within Python
- Query results are visualized using interactive charts and widgets

The project focuses on demonstrating the analytics serving layer
without deploying additional AWS infrastructure to avoid unnecessary costs.


