from google.cloud import storage

def upload_blob(img_name):
    client = storage.Client()

    bucket = client.get_bucket('noteify')

    imageBlob = bucket.blob(img_name)
    imageBlob.upload_from_filename(filename='./imgs/'+img_name)
