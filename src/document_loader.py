import re
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def clean_section_text(text):
    """
    Remove the article header up to the next uppercase letter.
    """
    
    
    header_pattern = r'^(?:ARTÍCULO|ARTICULO|Artículo|Articulo)\s+\d+.*?(?=[A-ZÁÉÍÓÚÑ])'
    cleaned_text = re.sub(header_pattern, '', text, flags=re.DOTALL)
    return cleaned_text.strip()

def extract_article_sections(text):
    """
    Extract sections of text between article markers and assign article numbers.
    Only matches when starting with capital A ('ARTÍCULO' or 'Artículo').
    Returns a list of (text, article_number) tuples with cleaned section text.
    """
    # Pattern that only matches when starting with capital A
    article_pattern = r'(?:ARTÍCULO|ARTICULO|Artículo|Articulo)\s+(\d+)'
    
    # Find all article markers with their positions
    article_matches = list(re.finditer(article_pattern, text))
    
    article_sections = []
    
    # Process each article section
    for i in range(len(article_matches)):
        start_pos = article_matches[i].start()
        article_num = article_matches[i].group(1)

        # Get end position (either next article or end of text)
        if i < len(article_matches) - 1:
            end_pos = article_matches[i + 1].start()
        else:
            end_pos = len(text)
        
        section_text = text[start_pos:end_pos]
        # Clean the section text by removing the header
        cleaned_section = clean_section_text(section_text)
        article_sections.append((cleaned_section, article_num))
    
    return article_sections

def load_and_process_document(file_path):
    """
    Load and process a document, creating a vector store from its contents.
    """
    # Load local text file
    loader = TextLoader(file_path)
    docs = loader.load()

    # Process the original text to get article sections
    original_text = docs[0].page_content
    article_sections = extract_article_sections(original_text)

    # Modified text splitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=300,
        chunk_overlap=50
    )

    # Create splits with article metadata
    splits = []
    for section_text, article_num in article_sections:
        section_splits = text_splitter.create_documents(
            texts=[section_text],
            metadatas=[{
                "source": file_path,
                "source_article": article_num
            }]
        )
        splits.extend(section_splits)

    # Index with the enhanced metadata
    vector_store = Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings()
    )

    return vector_store 