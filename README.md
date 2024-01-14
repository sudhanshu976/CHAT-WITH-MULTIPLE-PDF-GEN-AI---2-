# Chat with Multiple PDFs using Gemini Pro

This Streamlit application allows users to chat with multiple PDFs using Gemini Pro. The application utilizes Google's Generative AI for embeddings and Gemini Pro for conversational question-answering.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - For Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Set up your Google API key:

   - Create a `.env` file in the project directory.
   - Add your Google API key to the `.env` file:

     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

6. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Access the application through the provided URL after running the application.
2. Upload multiple PDFs using the "Upload PDFs" section in the sidebar.
3. Enter your question in the "Enter your question here" text input.
4. Click the "Ask" button to initiate the conversation with the uploaded PDFs.

## Dependencies

- Streamlit
- PyPDF2
- google.generativeai
- python-dotenv
- langchain-google-genai
- langchain
- langchain-community

## Notes

- The application uses Gemini Pro for chat-based question-answering.
- Google's Generative AI is used for generating embeddings.
- The application splits the PDF text into chunks and stores them as vectors for efficient similarity searches.

Feel free to explore and enhance the functionality based on your requirements!