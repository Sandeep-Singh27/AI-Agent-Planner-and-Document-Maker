from docx import Document
from src.schema import ExecutionResult

def generate_docx(
        result: ExecutionResult,
        filename: str
):
    doc = Document()

    for section in result.document:
        doc.add_heading(section.heading)

        for paragraph in section.paragraphs:
            if paragraph.strip():
                doc.add_paragraph(paragraph)

    doc.save(filename)