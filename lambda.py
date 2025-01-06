import boto3
import json
import ast

def lambda_handler(event, context):
    # Correct the service name to 'sagemaker-runtime' as a string
    runtime_client = boto3.client('sagemaker-runtime')
    
    endpoint_name = 'xgboost-2024-10-05-09-57-36-602'
    
    # Check if 'body' exists in event and parse it
    if 'body' in event:
        input_data = ast.literal_eval(event['body'])  # Note: 'body', not 'Body'
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing request body'})
        }
    
    # Construct the sample data in CSV format
    sample = '{},{},{},{}'.format(input_data['x1'], input_data['x2'], input_data['x3'], input_data['x4'])
    
    # Invoke the SageMaker endpoint
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',
        Body=sample
    )
    
    # Decode the response from the endpoint
    result = int(float(response['Body'].read().decode('ascii')))
    
    # Return the result or some success message
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': result})
    }
