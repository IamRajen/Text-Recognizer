## File name : text_recognizer_gcp.py
## Created on: 30th Sept 2020
## Description : Extract the necessary information from documents using Google Cloud Vision API


from google.cloud import documentai_v1beta2 as documentai
import os, io


# list will contain all the document links provided in the google storage..
documents = ["gs://imag_reg/input_form_a.pdf" , "gs://imag_reg/input_form_b.pdf"] # add your document link as needed

project_id = 'image-rec-249212' # your project ID here

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r"image-rec-249212-1b96a4b53001.json" # download the json file and use here

# function will provide you the text from the provided document
def get_document_text (input_uri, project_id):
    project_id = project_id
    input_uri=input_uri

    client = documentai.DocumentUnderstandingServiceClient()
    gcs_source = documentai.types.GcsSource(uri=input_uri)
    input_config = documentai.types.InputConfig(
                        gcs_source=gcs_source, mime_type='application/pdf')

    # Location can be 'us' or 'eu'
    parent = 'projects/{}/locations/us'.format(project_id)
    request = documentai.types.ProcessDocumentRequest(parent=parent,input_config=input_config)

    document = client.process_document(request=request)
    return document.text


# function will parse the document text and get the line by line text. Then will see for the required 
# comparative values in the text..
def parse_result(text):
    lines = text.split("\n")
    res = {}
    for line in lines:
        if 'ADDRESS OF PREMISE' in line:
            res['address'] = line.split("ADDRESS OF PREMISE")[-1].split('THIS AGREEMENT')[0]
        if 'PRESENCE OF' in line:
            res['presence'] = line.split('PRESENCE OF')[-1]
    return res


# looping through the documents to extract the required values..
for items in documents:
    text = get_document_text(items, project_id)
    result = parse_result(text)

    print(result)
