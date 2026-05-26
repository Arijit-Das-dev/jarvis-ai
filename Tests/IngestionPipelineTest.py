from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL

def test():

    ipm = INGESTION_PIPELINE_MODEL()
    document = ipm.load_all_docs(file_path="Assets/pdf") # load all docs
    return document

if __name__ == "__main__":
    test()