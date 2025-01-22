
# Agenetic-AI-Practical

This repository contains two AI projects:

1. **Financial_AI-Agent** - An AI agent for financial decision-making that leverages Phidata and Groq for query analysis and model interaction.
2. **Multiagent_AI_RAG_using_vectordb** - A PDF analyzer that allows users to chat with documents by providing the document URL, utilizing Groq, Docker, and Phidata.
3. **Video Summarizer** - contain script for the summarizing the video with proper content and explanation by adding the special comments and bullet points  


## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Overview

### Financial_AI-Agent

The **Financial_AI-Agent** is designed to interact with users and perform financial analysis based on their queries. By leveraging **Phidata** for agent creation and **Groq** for model interaction, the agent searches the internet, analyzes data, and provides relevant results. This system assists in financial decision-making by interpreting user queries and processing them through AI models for valuable insights.

### Multiagent_AI_RAG_using_vectordb

The **Multiagent_AI_RAG_using_vectordb** project focuses on enabling users to interact with PDF documents. The system allows a user to provide a document URL, after which it processes and analyzes the PDF content. Using **Groq**, **Docker**, and **Phidata**, the system leverages a multi-agent architecture to offer a conversation-like interface where users can ask questions or engage with the document’s content.

### Video Summarizer 

The **Video Summarizer** project focus on the summarizing the video with proper content and explanation by adding the special comments and bullet points  

## Technologies Used

- **Python** - The primary programming language used for both projects.
- **Phidata** - Used for agent creation and data processing in both projects.
- **Groq** - Used for model interaction and query analysis.
- **Docker** - Used for containerizing the multi-agent system and enabling easier deployment in **Multiagent_AI_RAG_using_vectordb**.
- **Gemini** - Use for the generating the summary of the video.


## Project Structure

The project contains the following folder structure:

```
Agenetic-AI-Practical/
├── Financial_AI-Agent/
│   ├── financial_agent.py
│   ├── app.py
├── Multiagent_AI_RAG_using_vectordb/
│   ├── pdf_assistan.py
├── README.md
```

- **Financial_AI-Agent/** - Contains scripts for the financial AI agent, including user query processing, internet search, and analysis tasks.
- **Multiagent_AI_RAG_using_vectordb/** - Contains scripts for analyzing and interacting with PDF documents via a chat-like interface.
- **Video Summarizer** - contain script for the summarizing the video with proper content and explanation by adding the special comments and bullet points  


## Setup and Installation

Follow the steps below to set up and install the project on your local machine.

### Prerequisites

1. **Python** - Version 3.x. Install from [python.org](https://www.python.org/).
2. **Git** - For version control. Install from [git-scm.com](https://git-scm.com/).
3. **Docker** (for Multiagent_AI_RAG_using_vectordb) - Install from [docker.com](https://www.docker.com/get-started).

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/atharv2001j/Agenetic-AI-Practical.git
   cd Agenetic-AI-Practical
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   (Ensure that you include all dependencies such as **Phidata**, **Groq**, etc., in the `requirements.txt` file.)

4. [Optional] Install **Docker** and set up containers if needed for **Multiagent_AI_RAG_using_vectordb**.

   ```bash
   docker-compose up
   ```

## How to Run

### Running Financial_AI-Agent

To run the **Financial_AI-Agent**:

1. Navigate to the `Financial_AI-Agent/` directory:

   ```bash
   cd Financial_AI-Agent
   ```

2. Run the script for agent creation or query processing:

   ```bash
   python agent_creation.py  # or another relevant script
   ```

3. The agent will process user queries and interact with models using **Groq** and **Phidata**.

### Running Multiagent_AI_RAG_using_vectordb

To run the **Multiagent_AI_RAG_using_vectordb**:

1. Navigate to the `Multiagent_AI_RAG_using_vectordb/` directory:

   ```bash
   cd Multiagent_AI_RAG_using_vectordb
   ```

2. Start the Docker containers (if required) to set up the environment:

   ```bash
   docker-compose up
   ```

3. Run the PDF interaction system:

   ```bash
   python pdf_analyzer.py  # or another relevant script
   ```

4. Provide a document URL, and the system will allow you to chat with the document.

## Contributing

We welcome contributions to improve the project! To contribute:

1. Fork the repository.
2. Clone your forked repository locally:

   ```bash
   git clone https://github.com/your-username/Agenetic-AI-Practical.git
   ```

3. Create a new branch for your changes:

   ```bash
   git checkout -b feature-branch-name
   ```

4. Make your changes and commit them:

   ```bash
   git add .
   git commit -m "Description of the changes"
   ```

5. Push to your forked repository:

   ```bash
   git push origin feature-branch-name
   ```

6. Create a pull request to the main repository.


```

