## File name : text_recognizer_aws.py
## Created on: 30th Sept 2020
## Description : Extract the necessary information from documents using AWS Textract API


import boto3
import time

# Document 
s3BucketName = "textract-console-us-east-2-683c5a84-1e08-4da1-8913-3988404b5ded" # provide the bucket name
documents = ["input_form_a.pdf", "input_form_b.pdf"] # provide the documents name in list

# starts the text extraction process using Bucket Name and document name
def startJob(s3BucketName, document):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
        DocumentLocation={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': document
            }
        })

    return response["JobId"]

# check the JobStatus when completed returns the status.
def isJobComplete(jobId):
    time.sleep(5)
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]
    print("Job status: {}".format(status))

    while (status == "IN_PROGRESS"):
        time.sleep(5)
        response = client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]
        print("Job status: {}".format(status))

    return status


def getJobResults(jobId):
    pages = []

    time.sleep(5)

    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)

    pages.append(response)
    print("Resultset page recieved: {}".format(len(pages)))
    nextToken = None
    if ('NextToken' in response):
        nextToken = response['NextToken']

    while (nextToken):
        time.sleep(5)

        response = client.get_document_text_detection(
            JobId=jobId, NextToken=nextToken)

        pages.append(response)
        print("Resultset page recieved: {}".format(len(pages)))
        nextToken = None
        if ('NextToken' in response):
            nextToken = response['NextToken']

    return pages


# Process document.
for document in documents:
    response = None

    jobId = startJob(s3BucketName, document)
    print("Started job with id: {}".format(jobId))
    if (isJobComplete(jobId)):
        response = getJobResults(jobId)

    # grouping all text in a list
    lines = []
    for resultPage in response:
        for item in resultPage["Blocks"]:
            if item["BlockType"] == "LINE":
                lines.append(item["Text"])

    res = {}

    # looping the list to get the required words/sentence
    for i in range(len(lines)):
        if 'ADDRESS OF PREMISE' in lines[i]:
            res['address'] = lines[i + 1]
        if 'PRESENCEOF' in lines[i]:
            res['presence'] = lines[i + 1]


    print(res)
