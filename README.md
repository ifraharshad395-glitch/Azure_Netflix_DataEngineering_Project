# Azure_Netflix_DataEngineering_Project

## Project Overview

This project is an end-to-end **Data Engineering pipeline built on Microsoft Azure**, designed to automate the ingestion and processing of Netflix-related datasets using **Azure Data Factory and Azure Data Lake Storage Gen2**.

The pipeline follows a structured data ingestion workflow where source files are dynamically identified, validated, and processed before being stored in the data lake.

![image alt](https://github.com/ifraharshad395-glitch/Azure_Netflix_DataEngineering_Project/blob/ec66e67462e7483f06343bdac3f514f1eed0c329/resourcegroup_and_resources.png)

## Architecture

**Source → Azure Data Factory → ADLS Gen2**

Azure Data Factory was used to orchestrate the pipeline and automate file ingestion into Azure Data Lake Storage.

### Azure Data Factory Activities

The pipeline uses the following activities:

* **Web Activity** — used to interact with an external API/source and retrieve the required information.
* **Set Variable Activity** — used to store and manage dynamic values during pipeline execution.
* **Validation Activity** — used to verify that the required files or data are available before continuing the pipeline.
* **ForEach Activity** — used to dynamically iterate over multiple files/items and process them individually.

### Pipeline Flow

```text
External Source
      │
      ▼
 Web Activity
      │
      ▼
 Set Variable
      │
      ▼
 Validation
      │
      ▼
   ForEach
      │
      ▼
   ADLS Gen2
```
![image alt](https://github.com/ifraharshad395-glitch/Azure_Netflix_DataEngineering_Project/blob/ec66e67462e7483f06343bdac3f514f1eed0c329/pipeline.png)

## Technologies Used

| Category               | Technology                        |
| ---------------------- | --------------------------------- |
| Cloud Platform         | Microsoft Azure                   |
| Data Orchestration     | Azure Data Factory                |
| Data Lake              | Azure Data Lake Storage Gen2      |
| Source/API Integration | Web Activity                      |
| Pipeline Logic         | Set Variable, Validation, ForEach |

## Key Concepts Demonstrated

* Azure Data Factory pipeline orchestration
* Dynamic pipeline execution
* External API/source integration
* Pipeline variables
* Data validation
* Iterative file processing
* Azure Data Lake Storage Gen2
* Cloud-based data ingestion
