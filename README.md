# PDF Reader AI with LangChain, Ollama, FastAPI Backend and ReactJS Frontend 

This project is a chatbot application that interacts with PDF documents using LangChain and Ollama for natural language processing capabilities. It also features a frontend built using ReactJS for a user-friendly interface.

## Features

- **PDF Interaction**: The chatbot allows users to interact with PDF documents, extracting information and performing tasks based on natural language commands.
- **LangChain Integration**: LangChain provides language understanding capabilities, allowing the chatbot to interpret user commands and extract relevant information from PDFs.
- **ReactJS Frontend**: The frontend interface is built using ReactJS, providing a modern and responsive user experience.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine:

   ```bash
   git clone https://github.com/hssahdev/pdf_reader_ai
   ```

2. **Navigate to Project Directory**: Enter the project directory:

   ```bash
   cd pdf_reader_ai
   ```

3. **Set Up Ollama Server**: Download [Ollama](https://ollama.com/download) and make sure its running in background. You also need to download the LLM model Llama

    ```bash
    ollama run llama2    
    ```


4. **Start Docker Compose**: Run the Docker Compose configuration to start the services:

   ```bash
   docker-compose up
   ```

5. **Access the Application**: Once the services are up and running, you can access the application via your web browser. By default, the frontend should be accessible at `http://localhost:5173`.

## Configuration

- **docker-compose.yaml**: This file defines the services required for the project, including LangChain, Ollama, and the frontend ReactJS application.

## Dependencies

- **LangChain**: A natural language processing library used for language understanding and document interaction.
- **Ollama**: A conversational AI platform that enhances the chatbot's conversational abilities.
- **ReactJS**: A JavaScript library for building user interfaces, used for the frontend of the application.

## Contributing

Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with any enhancements or fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This project was created by [Your Name] and is maintained by the contributors. Special thanks to the developers of LangChain, Ollama, and ReactJS for their amazing tools and libraries.