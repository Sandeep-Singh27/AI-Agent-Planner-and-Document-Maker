# AI Agent Planner & Document Maker

An autonomous, multi-stage AI workflow built with **FastAPI**, **LangChain**, and **Mistral AI** that converts high-level user requests into structured, publication-ready `.docx` documents through automated planning and sequential task execution.

---

## Architecture Overview

The system uses a decoupled two-layer agent architecture:

    User Request (POST /agent)
              │
              ▼
    ┌──────────────────┐
    │  Planner Layer   │  Deconstructs request into Plan Name, Goals, and Sequential Tasks
    └─────────┬────────┘
              │ (PlanSchema)
              ▼
    ┌──────────────────┐
    │ Execution Layer  │  Iteratively completes tasks, refining document state step-by-step
    └─────────┬────────┘
              │ (ExecutionResult)
              ▼
    ┌──────────────────┐
    │ Document Builder │  Parses structured sections into formatted .docx via python-docx
    └─────────┬────────┘
              │
              ▼
       File Download (.docx)

1. **Planner Layer:** Uses `mistral-small-latest` with structured outputs (`PlanSchema`) to decompose the user's objective into high-level goals and ordered sub-tasks.
2. **Execution Layer:** A sequential loop that feeds each planned task along with the accumulated document state into the execution chain (`ExecutionResult`), updating the document section-by-section.
3. **Document Exporter:** Translates validated Pydantic models into cleanly formatted Microsoft Word (`.docx`) documents with auto-generated headings and paragraphs.

---

## Tech Stack

- **Backend:** FastAPI, Uvicorn
- **LLM Framework:** LangChain (`langchain-mistralai`, `langchain-core`)
- **LLM Model:** Mistral AI (`mistral-small-latest`)
- **Validation & Schemas:** Pydantic v2
- **Document Processing:** `python-docx`
- **Environment Management:** `python-dotenv`

---

## Project Structure

    ├── generated/              # Output folder for generated .docx files
    ├── src/
    │   ├── generate_document.py# DOCX rendering logic
    │   ├── llm.py              # LangChain chains for Planning and Execution
    │   ├── prompts.py          # Prompt templates for planner and executor
    │   └── schema.py           # Pydantic schemas (PlanSchema, ExecutionResult, etc.)
    ├── main.py                 # FastAPI application & entry point
    ├── requirements.txt        # Python dependencies
    └── .env                    # API keys and environment variables

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- A valid [Mistral AI API Key](https://console.mistral.ai/)

### 2. Installation

Clone the repository and install the dependencies:

    git clone [https://github.com/Sandeep-Singh27/AI-Agent-Planner-and-Document-Maker.git](https://github.com/Sandeep-Singh27/AI-Agent-Planner-and-Document-Maker.git)
    cd AI-Agent-Planner-and-Document-Maker
    pip install -r requirements.txt

### 3. Environment Setup

Create a `.env` file in the root directory:

    MISTRAL_API_KEY=your_mistral_api_key_here

### 4. Running the Server

Start the FastAPI application:

    uvicorn main:app --reload

The API will be available at `[http://127.0.0.1:8000](http://127.0.0.1:8000)`. Interactive documentation is available at `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)`.

---

## API Usage

### Endpoint: `POST /agent`

**Request Body:**

    {
      "request": "Write a comprehensive project proposal for a smart city waste management system."
    }

**Response:**
Returns a downloadable `.docx` file containing the generated, structured document.
