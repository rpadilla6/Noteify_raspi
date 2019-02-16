from google.cloud import storage

client = storage.Client()

bucket = client.get_bucket('noteify')

imageBlob = bucket.blob('test.jpg')
imageBlob.upload_from_filename(filename='imgs/test.jpg')
