import pdfplumber
from docx import Document
import re

def extract_text_from_pdf(filepath):
    """Extrai texto de arquivo PDF"""
    text = ''
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return ''

def extract_text_from_docx(filepath):
    """Extrai texto de arquivo DOCX"""
    try:
        doc = Document(filepath)
        text = '\n'.join([p.text for p in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Erro ao extrair texto do DOCX: {e}")
        return ''

def extract_experiences(text):
    """Extrai experiências profissionais do texto"""
    pattern = r'(\b\d{2}/\d{4}\b|\b\d{4}\b).*?\n(.*?)(?=\n\d{2}/\d{4}|\n\d{4}|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    experiences = []
    for match in matches:
        date, desc = match
        experiences.append({'data': date.strip(), 'descricao': desc.strip()})
    return experiences

def extract_skills(text):
    """Extrai habilidades do texto"""
    skills = []
    skill_sections = re.findall(r'(Habilidades|Skills|Competências)[:\n](.*?)(\n\w|$)', text, re.IGNORECASE | re.DOTALL)
    for section in skill_sections:
        items = re.split(r'[\n,;•\-]', section[1])
        skills.extend([i.strip() for i in items if len(i.strip()) > 1])
    return list(set(skills)) 