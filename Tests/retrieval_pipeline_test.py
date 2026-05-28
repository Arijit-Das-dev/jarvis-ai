from Backend.Core.Features.RagPipeLine.Retrieval_PipeLine import RETRIEVAL_PIPELINE_MODEL

def main():
    
    rp = RETRIEVAL_PIPELINE_MODEL()
    query = "what is code of conduct"
    output = rp.final_answer(user_query=query)
    return output

if __name__ == "__main__":
    main()