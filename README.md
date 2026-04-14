# Intelligent Document Processing System

## Overview

This project demonstrates how to build an AI-powered document processing system using Azure Document Intelligence.

The solution extracts structured data from invoices and receipts, enabling automation of manual data entry workflows.

## Key Features

* Extracts vendor name, invoice date, subtotal, tax, and total
* Uses Azure Document Intelligence prebuilt models
* Outputs structured data in JSON format
* Built with Python and Azure AI Services

## Architecture / Flow

1. Input: Invoice or receipt document
2. Processing: Sent to Azure Document Intelligence
3. Extraction: AI model identifies key fields
4. Output: Structured JSON data returned and saved

## Technologies Used

* Azure Document Intelligence
* Python
* JSON
* Azure AI Services

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/intelligent-document-processing-system.git
cd intelligent-document-processing-system
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add environment variables

Create a `.env` file:

```env
DOCUMENT_INTELLIGENCE_ENDPOINT=your_endpoint
DOCUMENT_INTELLIGENCE_KEY=your_key
```

### 6. Run the application

```bash
python app.py
```

## Example Output

The system returns structured JSON data containing key invoice fields, enabling integration into automated workflows.

## Business Use Case

This solution can be used in finance and operations to automate invoice processing, reduce manual data entry, and improve accuracy.

## Future Improvements

* Add a web interface (Streamlit)
* Support additional document types
* Export data to Excel or databases
