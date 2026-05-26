import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from Backend.Core.Features.LLmModelCore.llmService import embedding_model_provider
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

#SETTING UP INGESTION PIPELINE MODEL
class INGESTION_PIPELINE_MODEL:

    # ==============================================
    # LOADING ALL FOLDERS TO THE LANGCHAIN DIRECTORY
    # ==============================================
    def load_all_docs(self, file_path: str):

        # checking if that folder path exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} Not found")

        # load all folders + files to the Langchain Directory
        loader = DirectoryLoader(
            path=file_path,
            glob="*.pdf",
            loader_cls=PyPDFLoader         
        )

        # List of document objects
        """
        documents = [
            Document(Page1 of xFile),
            Document(Page2 of xFile),
            Document(Page3 of xFile),

            Document(Page1 of yFile),
            Document(Page2 of yFile),
            Document(Page3 of yFile)
        ]
        """
        documents = loader.load()

        # checking if any files exists inside that folder
        if not documents:
            raise ValueError("No pdf found in that Folder")

        # inserting the basic info with the documents into the files
        for document in documents:
            source = document.metadata.get("source", "")
            document.metadata["file_name"] = os.path.basename(source)

        # Printing all the files inside that document
        for i, document in enumerate(documents, 1):

            # Cleaning page content -> texts inside that pages
            document.page_content = document.page_content.strip()
            document.page_content = document.page_content.replace("\n", " ")
            document.page_content = " ".join(document.page_content.split())

            print(f"Page number : {i}")
            print(f"SOURCE FILE : {source}")
            print(f"Page content : {document.page_content}")
            print(f"FILE NAME : {document.metadata["file_name"]}\n\n\n")

        """ LOADED SUCCESSFULLY """
        print("="*50)
        print(f"{file_path} LOADED SUCCESSFULLY")
        print("="*50)
        print()
        return documents
    
    # =================
    # SPLIT INTO CHUNKS
    # =================
    def text_to_chunks(self, documents):

        print("\n SPLITTING PDFs INTO CHUNKS")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 800,
            chunk_overlap = 150,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = splitter.split_documents(documents)

        for i, chunk in enumerate(chunks):

            chunk.metadata["chunk_id"] = i
            chunk.metadata["length"] = len(chunk.page_content)

        for i, chunk in enumerate(chunks[:6]):
            print("="*60)
            print(f"CHUNK ID : {chunk.metadata["chunk_id"]}")
            print(f"CHUNK LENGTH : {chunk.metadata["length"]}")
            print(f"CHUNK SOURCE : {chunk.metadata.get("source")}")
            print(f"CHUNK PAGE CONTENT : {chunk.page_content}")

        print(f"TOTAL CHUNKS CREATED : {len(chunks)}")
        return chunks
    
    # ======================
    # CREATE VECTOR DATABASE
    # ======================
    def create_vector_db(self, chunks, db_path="DB/ChromaDB"):

        embeddings = HuggingFaceEmbeddings(
            model_name = embedding_model_provider.HUGGING_FACE_MODEL
        )

        vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path,
        collection_metadata={"hnsw:space": "cosine"}
        )

        print("CHROMA DB CREATED SUCCESSFULLY")
        return vector_store