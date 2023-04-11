from azure.storage.blob import BlobServiceClient

storage_account_key = "xemFmkdP4czrzigzwTuLHKjbCkoK76RLMOLLCze0E1esoxF9DkTAhQVlqGk8SFtwqxVDxgDr1b0r+ASt8Ag+wg=="
storage_account_name = "maurotestopslag"
connection_string = "DefaultEndpointsProtocol=https;AccountName=maurotestopslag;AccountKey=xemFmkdP4czrzigzwTuLHKjbCkoK76RLMOLLCze0E1esoxF9DkTAhQVlqGk8SFtwqxVDxgDr1b0r+ASt8Ag+wg==;EndpointSuffix=core.windows.net"
container_name = "testcontainer"

def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_path,"rb") as data:
        blob_client.upload_blob(data)
        print("Uploaded {file_name}.")
# calling a function to perform upload
uploadToBlobStorage('c:/Users/Student/Desktop/test_uplad.txt','test_uplad')