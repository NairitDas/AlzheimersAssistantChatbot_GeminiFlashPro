Gentle Guardian: An Empathetic Companion Chatbot for Alzheimer's Patients

Welcome to **Gentle Guardian**, a compassionate and gentle companion chatbot designed for Alzheimer's patients. This web application uses Streamlit for the UI, along with Google's Generative AI to produce empathetic, supportive, and personalized responses.
```markdown
---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Flowchart Methodology](#flowchart-methodology)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview
**Gentle Guardian** is designed to provide a caring conversational experience for individuals with Alzheimer's. It includes features such as:
- A soothing, visually appealing interface
- Personalized conversation with memory assistance
- Session state management to maintain conversation history
- Auto-scroll for a seamless chat experience

The bot uses Google’s generative AI (`gemini-1.5-pro`) to generate responses based on a carefully crafted context prompt.

---

## Features
- **Empathetic Chatbot:** Tailored responses with an emphasis on empathy, personalization, and support.
- **Dynamic Context Building:** Maintains conversation context and personal details to improve response quality.
- **Custom UI Styling:** Beautiful, soothing design with gradients, custom fonts, and helpful reminders.
- **Flowchart Visualization:** A detailed flowchart that explains the entire methodology behind the chatbot.

---

## Installation

### Prerequisites
- Python 3.7 or above
- [Streamlit](https://streamlit.io/)
- [Graphviz](https://graphviz.org/)
- [google-generativeai Python package](https://pypi.org/project/google-generativeai/)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gentle-guardian.git
   cd gentle-guardian
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit google-generativeai graphviz
   ```

4. **Ensure you have Graphviz installed on your system:**
   - **For macOS:**  
     ```bash
     brew install graphviz
     ```
   - **For Ubuntu:**  
     ```bash
     sudo apt-get install graphviz
     ```
   - **For Windows:**  
     Download and install from [Graphviz's website](https://graphviz.org/download/).

5. **Configure your API key:**  
   Replace the placeholder API key in your code with your actual API key. It is recommended to use environment variables or a secure secrets management approach rather than hardcoding the key directly.

---

## Usage

1. **Run the Streamlit Application:**
   ```bash
   streamlit run your_app_filename.py
   ```
   Replace `your_app_filename.py` with the name of the file that contains your chatbot code.

2. **Interact with the Chatbot:**  
   Open the provided URL in your browser, and enjoy chatting with your gentle companion!

3. **Generate the Methodology Flowchart (Optional):**  
   Run the Python script that uses Graphviz to generate the flowchart:
   ```bash
   python generate_flowchart.py
   ```
   The flowchart file (`chatbot_methodology_flowchart.png`) will be saved in your project directory.

---

## Project Structure

```
gentle-guardian/
├── your_app_filename.py      # Main Streamlit chatbot code
├── generate_flowchart.py     # Python script to generate the flowchart
├── README.md                 # Project documentation (this file)
└── requirements.txt          # List of dependencies (optional)
```

---

## How It Works

1. **Initialization:**  
   - The code imports necessary libraries (Streamlit, Google Generative AI, datetime, etc.).
   - Configures the AI model and sets up the page with custom CSS styling.

2. **Sidebar and Layout:**  
   - A friendly sidebar with a water reminder and app description enhances user experience.
   - The main page displays a welcoming title and the current date.

3. **Session State Management:**  
   - The chatbot saves the conversation and personal details to ensure context is maintained across interactions.

4. **Context Building & Response Generation:**  
   - A context prompt guides the AI to be empathetic, personalized, and concise.
   - User messages update the context, and the AI generates caring responses.

5. **User Interaction:**  
   - A text input collects user messages, which are appended to the chat history.
   - A delete button allows for managing conversation history.
   - JavaScript auto-scroll ensures the newest messages are always visible.

---

## Flowchart Methodology

A detailed flowchart has been created using Graphviz to visually represent the chatbot's workflow:
- **Key Process Steps:** From initialization, UI setup, session management, input handling, to AI response generation.
- **Decision Points:** Includes handling user inputs, error management, and context updates.

You can generate this flowchart by running the provided Graphviz script in the repository.

---

## Future Improvements

- **API Key Security:**  
  Move API key management to environment variables or a secrets manager.

- **Enhanced Personalization:**  
  Use advanced NLP techniques to extract and manage user details more accurately.

- **Additional Features:**  
  Voice integration, multimedia support, and accessibility enhancements to further support the target audience.

- **Interactive Flowchart:**  
  Develop an interactive version of the methodology flowchart accessible directly within the web app.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Enjoy using **Gentle Guardian** to provide a supportive companion experience, and feel free to contribute or raise issues for any improvements!
```

This README file provides a clear, step-by-step explanation of your project, including setup, usage instructions, and an overview of the code and flowchart methodology. Enjoy documenting and sharing your project!
