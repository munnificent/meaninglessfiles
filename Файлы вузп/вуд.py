from docx import Document

def remove_lines_starting_with_zero(doc_path):
    # Открываем документ
    doc = Document(doc_path)
    
    # Проходим по каждому параграфу в документе
    for paragraph in list(doc.paragraphs):  # Создаем копию списка, чтобы можно было изменять оригинальный
        if paragraph.text.startswith('0'):
            # Удаляем параграф, если он начинается на '0'
            p = paragraph._element
            p.getparent().remove(p)
            p._p = p._element = None
    
    # Сохраняем измененный документ
    doc.save('modified_document.docx')

# Замените 'path_to_your_document.docx' на путь к вашему документу
remove_lines_starting_with_zero('текст.docx')
