---
# News Research Tool

This repository contains a news research tool built using the Ollama model and Chainlit. The tool is designed to help users quickly summarize news articles and extract relevant information, making it easier to stay informed and analyze large amounts of content.

## Features

- **News Summarization**: Generates concise summaries of news articles.
- **Relevant Information Extraction**: Retrieves key facts, events, and details from articles.
- **Contextual Insights**: Provides a deeper understanding of the article's main points.
- **User-Friendly Interface with Chainlit**: Easy-to-use web-based interface for seamless interactions.

## Technology Stack

- **[Ollama Model](https://ollama.com/)**: Used for natural language processing (NLP) tasks such as summarization and information extraction. The model used is an open source LLM model known as Meta's Llama 3.1 in 8 Billion parameters size.
- **[Chainlit](https://chainlit.io/)**: Provides the interface for interacting with the tool.
- **Python**: The programming language used for implementation.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Bishal-Nakoda/News-Research-using-LLM.git
    cd News-Research-using-LLM
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.x installed. Then, run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Ollama Model**:
    To use this, you need to install Ollama on your computer. After that using the below command:
    ```bash
    ollama pull llama3.1
    ```
## Usage

1. **Seeding the Vector Database**:
    Run the following command to seed the vector database:
    ```bash
    python db.py
    ```

2. **Start the Application**:
    Run the following command to launch the Chainlit interface:
    ```bash
    chainlit run main.py -w
    ```

3. **Interacting with the Tool**:
    - Once the interface is open in your browser, you can ask question directly.
    - The tool will display a summary and highlight key information, such as important dates, names, and topics.


## Example Workflow

![image](https://github.com/user-attachments/assets/7820777b-3aac-4848-97a4-4129160ad106)


## Contributing

Contributions are welcome! Whether it's a bug report, feature request, or a pull request, feel free to contribute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or feedback, reach out to:

- **Email**: bishalnakoda37@gmail.com
- **LinkedIn**: [Bishal Nakoda](https://www.linkedin.com/in/bishal-nakoda/)
- **GitHub**: [Bishal-Nakoda](https://github.com/Bishal-Nakoda)

---

This README should give users clear instructions on how to install, use, and contribute to the project. Let me know if you need further adjustments!
