from Backend.Core.Features.RagPipeLine.Ingestion_PipeLine import INGESTION_PIPELINE_MODEL

ipm = INGESTION_PIPELINE_MODEL()

def test():

    document = ipm.load_all_docs(file_path="Assets/pdf") # load all docs
    chunks = ipm.text_to_chunks(document)
    return chunks

if __name__ == "__main__":
    test()