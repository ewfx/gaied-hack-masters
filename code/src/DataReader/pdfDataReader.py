import PyPDF2

def read_text_from_pdf(pdf_path):
    """
    Reads text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF, or None if an error occurs.
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)  # Updated for PyPDF2 v3+
            text = ""
            for page in pdf_reader.pages: # Updated for PyPDF2 v3+
                text += page.extract_text() or "" # Added or "" to prevent errors if extract_text() returns None.
            return text

    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
        return None
    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read PDF file at {pdf_path}. It might be corrupted or encrypted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
pdf_file_path = ".\..\test\attachments\email_3.pdf" # Replace with your PDF's path.
extracted_text = read_text_from_pdf(pdf_file_path)

if extracted_text:
    print(extracted_text)
else:
    print("Failed to extract text from the PDF.")