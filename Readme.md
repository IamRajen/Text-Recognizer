# Text Recognizer - Google Cloud Vision and AWS Textract API

Python code for Text recognition using Google Cloud Vision API and AWS Textract API. This code will help you to filter the required words from documents. As we all know extracting the required information from documents or forms manually are too much expensive and time consuming task.  

So this couple lines of code will help you to get the required information by just providing some required parameter and steps which is shared below.



### <u>Google Cloud Vision</u>

Reference : https://cloud.google.com/vision/overview/docs/get-started

Code/File :  **text_recognizer_gcp.py** 

Before you begin : https://cloud.google.com/vision/docs/setup

Instructions : Make some changes as commented in the code. 

The documents to be processed by text-recognizer needs to be added to the "Google Storage" and the below documents list to be updated.

`documents = ["gs://imag_reg/input_form_a.pdf" , "gs://imag_reg/input_form_b.pdf"] # add your document link as needed`

`project_id = 'image-rec-249212' # your project ID here`

`os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r"image-rec-249212-1b96a4b53001.json" # download the json file and use here`



### <u>AWS Textract API</u>

Reference : https://aws.amazon.com/textract/

Code/File :  **text_recognizer_aws.py** 

How it Works : https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html 

Instructions : Make some changes as commented in the code. Make sure you don't include your ACCESS_ID 						and ACCESS_KEY in the code directly for security concerns. Consider using environment 						configs and injecting them in the code.

The documents to be processed by text-recognizer needs to be added to the "S3 Bucket". 

`s3ucketName = "textract-console-us-east-2-683c5a84-1e08-4da1-8913-3988404b5ded" # provide the bucket name`

Below documents list to be updated as per the files to be processed from "S3 Bucket".

`documents = ["input_form_a.pdf", "input_form_b.pdf"] # provide the documents name in list`







