import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_chars = []
    inside_tag = False

    for ch in html:
        if ch == '<':
            inside_tag = True
            continue
        if ch == '>':
            inside_tag = False
            continue
        if not inside_tag:
            cleaned_chars.append(ch)

    cleaned_text = ''.join(cleaned_chars)

    # убрать пустые строки
    lines = cleaned_text.splitlines()
    good_lines = []
    for line in lines:
        if line.strip() != "":
            good_lines.append(line)
    cleaned_text = "\n".join(good_lines)

    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write(cleaned_text)

# запуск
delete_html_tags("draft.html")
