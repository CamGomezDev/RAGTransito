# RAG-CodigoTransito

## Overview

RAG-CodigoTransito is a project designed to facilitate interaction with Colombia's national transit code through a chat system. This project leverages the power of language models to provide users with the ability to query and receive responses about transit regulations.

## Project Structure

- **src/**: Contains the source code for the project.
  - `graph_wrapper.py`: Handles the graph-related functionalities.
  - `document_loader.py`: Responsible for loading and processing documents.
  - `retriever_utils.py`: Provides utility functions for the retriever.
- **data/**: Directory for storing data files.
- **chat_transit.ipynb**: A Jupyter notebook demonstrating how to use the chat system to consult with the transit code.
- **preprocess_document.ipynb**: A Jupyter notebook for preprocessing the transit code txt file, which was generated from the PDF.
- **requirements.txt**: Lists the dependencies required for the project.

## Installation

To set up the project, ensure you have Python installed and then install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. **Environment Setup**: Ensure you have a `.env` file with the necessary API keys (OpenAI and LangSmith).
2. **Running the Notebook**: Open `chat_transit.ipynb` in Jupyter Notebook and follow the instructions to interact with the transit code.
3. **Example Query**: You can ask questions like "¿Cuándo debo hacer la revisión tecno-mecánica de mi carro?" to get responses based on the transit code.

## Dependencies

The project relies on the following Python packages:

- `langchain==0.3.22`
- `langchain-core==0.3.50`
- `langchain-openai==0.3.12`
- `langgraph==0.3.24`
- `chromadb==1.0.0`
- `python-dotenv==1.1.0`
- `tiktoken==0.9.0`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
