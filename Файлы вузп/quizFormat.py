from docx import Document
import string

def reformat_question_docx_to_docx(input_file, output_file):
    document = Document(input_file)
    new_document = Document()
    question_counter = 1  # Стартовый номер вопроса
    answer_index = 0  # Индекс для нумерации ответов
    
    for para in document.paragraphs:
        line = para.text.strip()
        if line.startswith(('V1', 'V2')):
            if question_counter > 1:
                new_document.add_paragraph()

            question_title = line.split('\t')[1].strip()
            question_number = f"{question_counter}."  # Нумеруем вопросы
            new_document.add_paragraph(f"{question_number} {question_title}")
            question_counter += 1
            answer_index = 0  
        elif line.startswith(('0', '1')):
            answer = line[2:].strip()
            letter = string.ascii_uppercase[answer_index]
            new_document.add_paragraph(f"{letter}\t{answer}")
            answer_index += 1  
    

    new_document.save(output_file)


reformat_question_docx_to_docx('текст.docx', 'output.docx')
