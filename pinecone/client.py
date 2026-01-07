from pinecone import Pinecone



pc = Pinecone(api_key="pcsk_5teLqP_AxiqTkfbwmSa87nqAvdYZ8kDFMoSsAWTkYuM5V7VrooZnsnzCpHG7zLSKwDVgo8")
index = pc.Index("knowledge-base")
print(index)