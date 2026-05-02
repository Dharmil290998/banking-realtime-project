## 🏗️ Project Architecture

<p align="center">
  <img src="./project-architecture.png" alt="Banking Architecture" width="900"/>
</p>

---

## 📖 Architecture Explanation

This project demonstrates an **end-to-end modern data platform** for the banking domain, combining both **batch processing (analytics)** and **real-time streaming (operational insights)** using Azure and Databricks.

---

### 🔷 1. Batch Data Pipeline (Analytics / BI)

The batch pipeline is designed to process historical data and generate business insights.

- **Data Sources**: SQL Server, CSV files, and external APIs  
- **Azure Data Factory**: Handles ingestion, scheduling, and orchestration of pipelines  
- **Azure Data Lake (ADLS Gen2)**: Stores raw data in the Bronze layer, partitioned by `year/month/day`  
- **Databricks (Batch Processing)**: Implements Medallion Architecture:
  - **Bronze** → Raw data ingestion  
  - **Silver** → Data cleaning and transformation  
  - **Gold** → Aggregations and business KPIs  
- **Power BI**: Connects to Gold layer for dashboards, reporting, and analytics  

---

### 🔷 2. Real-Time Streaming Pipeline (Operational / API)

The streaming pipeline enables real-time processing of banking transactions for operational use cases.

- **Event Producers**: Mobile apps, internet banking, ATM/POS systems  
- **Azure Event Hub**: Ingests high-throughput real-time transaction streams  
- **Databricks Structured Streaming**:
  - Processes streaming data in near real-time  
  - Performs validation, enrichment (joins with master data), and transformations  
  - Builds real-time aggregates such as fraud detection and transaction velocity  
- **Azure Cosmos DB**:
  - Serves as a low-latency NoSQL database  
  - Stores real-time insights for fast access  
  - Uses optimized partitioning strategy (e.g., `account_id`)  
- **FastAPI**:
  - Exposes REST APIs for accessing processed data  
  - Implements business logic and authentication  
- **Web Application / Dashboard**:
  - Displays real-time monitoring, fraud alerts, and transaction insights  

---

## 🚀 Key Highlights

- Designed using **Medallion Architecture (Bronze, Silver, Gold)**  
- Supports both **batch and real-time processing**  
- Implements **scalable and distributed data processing using Apache Spark**  
- Enables **low-latency data serving using Cosmos DB**  
- Follows **production-grade practices** like schema evolution, checkpointing, and partitioning  

---

## 🛠️ Technologies Used

- Azure Data Factory  
- Azure Data Lake Gen2  
- Azure Databricks (PySpark, Structured Streaming)  
- Azure Event Hub  
- Azure Cosmos DB  
- Power BI  
- FastAPI  

---
