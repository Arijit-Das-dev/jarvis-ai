from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL

ipm = INGESTION_PIPELINE_MODEL()

def test():

    document = ipm.load_all_docs(file_path="Assets/pdf") # load all docs
    return document

if __name__ == "__main__":
    test()