from docx import Document
import io

from mosreg.models import Payment


def generate_document(item_name: Payment) -> io.BytesIO:
    document = Document()
    document.add_heading(f"Document for {item_name.counterparty}", level=1)
    content = f"This is the content of the document for {item_name}."
    document.add_paragraph(content)

    buffer = io.BytesIO()
    document.save(buffer)
    buffer.seek(0)
    return buffer
