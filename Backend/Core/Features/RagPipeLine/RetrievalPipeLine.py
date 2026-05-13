import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from Backend.Core.Features.LLmModelCore.llmService import embedding_model_provider
from Backend.Services.modelCohere import MODEL_COHERE
from langchain_chroma import Chroma


class RETRIEVAL_PIPELINE_MODEL:

    def __init__(self):
  
        self.TRANSFORMER = embedding_model_provider.HUGGING_FACE_MODEL
        self.DB_LOCATION = "DB/ChromaDB"
    
        self.EMBEDDING_MODEL = HuggingFaceEmbeddings(
            model_name = self.TRANSFORMER
        )
        self.DB = Chroma(
            
            persist_directory=self.DB_LOCATION,
            embedding_function=self.EMBEDDING_MODEL
        )
    
    def final_answer(self, user_query):

        results = self.DB.similarity_search_with_score(
            query=user_query,
            k=10
        )

        """FILTERING STAGE"""

        filtered_docs = []

        seen_contents = set()

        for doc, score in results:

            if score > 1.0:
                continue


            # Clean chunk text
            content = doc.page_content.strip()


            # =================================================
            # FILTER 2:
            # REMOVE VERY SMALL CHUNKS
            # =================================================

            if len(content) < 80:
                continue
            # =================================================
            # FILTER 3:
            # REMOVE DUPLICATES
            # =================================================

            if content in seen_contents:
                continue

            seen_contents.add(content)

            # =================================================
            # OPTIONAL METADATA FILTERING
            # =================================================
            # Example:
            #
            # if doc.metadata["file_name"] != "tensorflow.pdf":
            #     continue
            #

            # Store clean chunk
            filtered_docs.append((doc, score))

        
        # =====================================================
        # 6. SORT BY BEST SCORE
        # =====================================================
        # Lower score = better chunk

        filtered_docs = sorted(

            filtered_docs,

            key=lambda x: x[1]
        )

        # =====================================================
        # 7. FINAL TOP-K SELECTION
        # =====================================================
        # Keep only best chunks

        TOP_K = 3

        final_docs = filtered_docs[:TOP_K]


        # =====================================================
        # 8. DISPLAY RETRIEVED CHUNKS
        # =====================================================

        print("\n==============================")
        print("FINAL RETRIEVED CHUNKS")
        print("==============================")


        for i, (doc, score) in enumerate(final_docs, start=1):

            print(f"\nChunk {i}")

            print(f"\nSimilarity Score: {score}")

            print(f"\nFile Name:")
            print(doc.metadata.get("file_name"))

            print(f"\nPage Number:")
            print(doc.metadata.get("page"))

            print(f"\nChunk ID:")
            print(doc.metadata.get("chunk_id"))

            print(f"\nChunk Length:")
            print(doc.metadata.get("length"))

            print("\nCONTENT:")
            print(doc.page_content[:500])

            print("\n" + "-" * 60)

        # =====================================================
        # 9. BUILD FINAL CONTEXT
        # =====================================================
        # Combine all retrieved chunks into one context

        context = "\n\n".join(

            [doc.page_content for doc, _ in final_docs]
        )

        cohere = MODEL_COHERE()

        print("=="*50)
        print("MODEL OUTPUT")
        print("=="*50)
        
        final_output = cohere.askCohere(user_input=user_query, context=context)
        print(final_output)
        
        return final_output