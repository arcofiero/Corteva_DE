# AWS Deployment for Django Project

## **1. Database**

### - Amazon RDS (PostgreSQL)
* Managed service tailored for relational databases.
* Features to leverage:
  * **Automated Backups**: For consistent data backup.
  * **Multi-AZ Deployment**: Ensures high availability.

## **2. API Deployment**

### - Elastic Beanstalk
* Platform-as-a-Service (PaaS).
* Benefits:
  * Simplified deployment.
  * Auto-scaling and environment management.

### - EC2 (Alternative Method)
* Detailed setup involves:
  * **Web Server**: Nginx.
  * **App Server**: Gunicorn.

## **3. Scheduled Data Ingestion**

### - AWS Lambda
* Serverless compute service.
* Ideal for sporadic tasks like data ingestion.

### - CloudWatch Events
* Schedule Lambda executions.
* Automate data ingestion routines.

## **4. Additional Services**

### - API Gateway
* Interface for Lambda APIs.
* Ensures scalable and secure API deployment.

### - VPC
* Encapsulate resources in a private cloud network.

### - Security
* **Security Groups**: Define access rules.
* **IAM**: Assign granular permissions.

### - S3
* Cloud storage for backups or static files.

### - CloudWatch
* Oversee performance and health.
* Set alerts and alarms.

### - Elastic Load Balancing
* Manage and distribute incoming traffic.
* Enhances application availability.
