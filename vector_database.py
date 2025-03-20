from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

pdfs_directory = 'pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name,"wb")as f:
        f.write(file.getbuffer())
        

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    document = loader.load()
    return document

# file_path='universal_declaration_of_human_rights.pdf'
# documents = load_pdf(file_path)
# print(len(documents))



