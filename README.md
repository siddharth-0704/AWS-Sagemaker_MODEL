# Iris Flower Detection using AWS SageMaker, Lambda, and API Gateway
This project demonstrates a serverless machine learning application hosted on AWS that predicts the species of an iris flower based on its physical attributes (sepal length, sepal width, petal length, petal width).

Key Features:
Model Training with SageMaker
The machine learning model was trained using SageMaker, leveraging its managed infrastructure to build and deploy a classification model for the famous Iris dataset.
Real-time Predictions with Lambda
A Lambda function serves as the backend, running the deployed SageMaker endpoint to process incoming requests and return predictions.
API Gateway Integration
API Gateway provides a secure and scalable RESTful API interface to the application, allowing users to send requests with flower dimensions and receive predictions in real time.

Workflow Overview:
Preprocess the Iris dataset and train the model on SageMaker.
Deploy the trained model as an endpoint on SageMaker.
Create a Lambda function to interact with the SageMaker endpoint.
Use API Gateway to expose the Lambda function as a RESTful API.

Technologies Used:
AWS SageMaker- Model training and deployment.
AWS Lambda- Backend function for inference.
AWS API Gateway- API creation and management.
Python- For data preprocessing, training, and Lambda function.

How to Use:
Clone this repository.
Follow the setup instructions to configure AWS services.

Use the API endpoint to submit requests in the format:
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

Receive predictions for the iris species: Setosa, Versicolor, or Virginica.

Results:
The project achieves high accuracy using a simple, interpretable machine learning model. It highlights the power of AWS's serverless architecture to deploy and manage ML applications.
