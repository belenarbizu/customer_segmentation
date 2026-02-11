# Customer Segmentation with RFM, K-Means and FastAPI

## 📌 Project Overview

This project focuses on customer segmentation using RFM analysis (Recency, Frequency, Monetary) combined with K-Means clustering.
The goal is to group customers based on their purchasing behavior in order to identify valuable segments such as loyal customers, champions, or inactive users.

The project covers the full machine learning lifecycle, from data preprocessing and feature engineering to model training and deployment as a REST API.

The project includes:

- Data cleaning and preprocessing
- Feature engineering using RFM metrics
- Unsupervised learning with K-Means
- Real-time inference via FastAPI
- Simple web interface
- Docker containerization
- Public deployment

## 📊 Data Preprocessing

The preprocessing stage ensures data quality and consistency before feature engineering and modeling.

Key preprocessing steps:

- Removal of duplicated records
- Handling of missing values:

  - Missing CustomerID values were removed
  - Missing product descriptions were filled using StockCode mappings when possible

- Cancellation invoices (InvoiceNo starting with "C") were excluded
- Rows with non-positive Quantity or UnitPrice were removed
- InvoiceDate was converted to datetime format
- A new feature TotalPrice was created as Quantity × UnitPrice

These steps were designed to avoid noise and incorrect customer behavior signals.

## 🧮 Feature Engineering (RFM)

Customer behavior was summarized using RFM analysis, a widely used technique in customer analytics:

- Recency: Number of days since the customer’s last purchase
- Frequency: Number of unique invoices per customer
- Monetary: Total amount spent by the customer

RFM features were aggregated at the customer level and used as input for clustering.

## 🤖 Model

K-Means was selected as the clustering algorithm due to its simplicity, interpretability, and suitability for numerical features such as RFM metrics.

Key modeling steps:

- Feature scaling using StandardScaler
- Selection of the optimal number of clusters using the Elbow Method and Silhouette Score
- Training the final K-Means model with the selected number of clusters
- Interpretation and labeling of clusters based on RFM characteristics

The final model segments customers into 5 behavioral groups:

- Champions
- Top Customers
- Potential Loyalists
- Occasional Customers
- Lost Customers

## 🚀 API Deployment

The trained model was deployed as a REST API using FastAPI, allowing real-time customer segmentation.

### Available endpoints:

- ``POST /predict``

  Accepts RFM values and returns the predicted customer segment.
  
  Example request:
  ```
  {
  "recency": 10,
  "frequency": 5,
  "monetary": 250
  }
  ```
  Example response:
  ```
  {
  "cluster": 3,
  "name": "Potential Loyalists"
  }
  ```

- ``GET /health``

  Health check endpoint used to verify that the service is running correctly.
  ```
  { "status": "ok" }
  ```

### Input validation

Request data is validated using Pydantic, ensuring:

- Correct data types
- Non-negative values for RFM features
- Protection against invalid inputs at inference time

## 🖥 Web Interface
A minimal web interface allows users to:
- Input RFM values
- Submit a prediction request
- View the predicted customer segment

Built with:
- HTML
- Jinja2 templates
- FastAPI form handling

## 🐳 Docker
The application is fully containerized.

To build locally:
```
docker build -t customer-segmentation .
```
To run:
```
docker run -p 8000:8000 customer-segmentation
```

## ☁ Deployment
The project is deployed publicly using Render.

The containerized API is automatically built from GitHub and deployed via Docker.

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Jinja2
- Docker
- Render

## ✅ Conclusion

RFM analysis provides a compact and interpretable representation of customer behavior. K-Means clustering effectively identifies meaningful customer segments without labeled data. Deploying the model as an API enables real-time inference and integration with other systems. Input validation and health checks improve robustness and production readiness.

This project demonstrates how an unsupervised machine learning model can be designed, trained, interpreted, and deployed as a scalable service. From data preprocessing to cloud deployment, it showcases a complete end-to-end workflow bridging data science and software engineering.

In a real business context, this type of segmentation can support targeted marketing strategies, customer retention initiatives, and revenue optimization by enabling personalized actions for different customer groups.
