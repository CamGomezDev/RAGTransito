from langchain.load import dumps, loads

def get_unique_union(documents: list[list]):
    """ Unique union of retrieved docs with article numbers """
    # Flatten list of lists, and convert each Document to string
    # We'll add the article number to the string representation to make it part of uniqueness check
    flattened_docs = [dumps(doc.page_content + doc.metadata.get('source_article', '')) 
                    for sublist in documents 
                    for doc in sublist]
    unique_docs = list(set(flattened_docs))

    # When loading back, we need to split the content and metadata
    loaded_unique_docs = []
    for doc_str in unique_docs:
        doc = loads(doc_str)
        # Get original document from documents list to preserve metadata
        original_doc = next((d for sublist in documents 
                        for d in sublist 
                        if d.page_content + d.metadata.get('source_article', '') == doc), None)
        if original_doc:
            loaded_unique_docs.append(original_doc)

    return loaded_unique_docs

def format_context_with_articles(docs):
    """Format context with article numbers"""
    formatted_contexts = []
    for doc in docs:
        article_num = doc.metadata.get('source_article', 'N/A')
        formatted_contexts.append(f"[Artículo {article_num}] {doc.page_content}")

    return "\n\n".join(formatted_contexts)