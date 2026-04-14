import json
import os
from pathlib import Path

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

# Load environment variables from .env
load_dotenv()

# Read endpoint and key from environment variables
endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")

# Validate environment variables
if not endpoint or not key:
    raise ValueError("Missing endpoint or key in .env file")

# Create a Document Intelligence client
client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Path to the invoice file
file_path = Path("samples/invoice.pdf")

# Check that the file exists
if not file_path.exists():
    raise FileNotFoundError(f"File not found: {file_path}")

# Open the file and send it to Azure for analysis
with open(file_path, "rb") as f:
    poller = client.begin_analyze_document(
        model_id="prebuilt-invoice",
        body=f
    )

# Wait for the result
result = poller.result()
clean_output = []

for document in result.documents:
    fields = document.fields

    cleaned = {
        "VendorName": getattr(fields.get("VendorName"), "content", None) if fields.get("VendorName") else None,
        "InvoiceDate": getattr(fields.get("InvoiceDate"), "content", None) if fields.get("InvoiceDate") else None,
        "InvoiceTotal": getattr(fields.get("InvoiceTotal"), "content", None) if fields.get("InvoiceTotal") else None,
        "SubTotal": getattr(fields.get("SubTotal"), "content", None) if fields.get("SubTotal") else None,
        "TotalTax": getattr(fields.get("TotalTax"), "content", None) if fields.get("TotalTax") else None,
    }

    clean_output.append(cleaned)

print(json.dumps(clean_output, indent=2))

Path("output").mkdir(exist_ok=True)

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(clean_output, f, indent=2)

print("\nAnalysis complete. Results saved to output/result.json")

# Prepare a dictionary to store extracted fields
output = {}

# Loop through the analyzed documents and extract fields
for document in result.documents:
    for name, field in document.fields.items():
        output[name] = {
            "value": getattr(field, "value", None),
            "content": getattr(field, "content", None),
            "confidence": getattr(field, "confidence", None)
        }

# Print the extracted fields to the terminal
print(json.dumps(output, indent=2, default=str))

# Make sure the output folder exists
Path("output").mkdir(exist_ok=True)

# Save the extracted data to a JSON file
with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, default=str)

print("\nAnalysis complete. Results saved to output/result.json")