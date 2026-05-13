from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL

def test():

    ipm = INGESTION_PIPELINE_MODEL()
    document = ipm.load_all_docs(file_path="Assets/pdf") # load all docs
    chunks = ipm.text_to_chunks(documents=document) # split into chunks 
    vectorStore = ipm.create_vector_db(chunks=chunks) # store to vector db
    return vectorStore
    
if __name__ == "__main__":
    test()