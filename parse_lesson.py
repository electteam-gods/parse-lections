from docx import Document
import json
import sys

if len(sys.argv) < 2:
    print("Missing required argument: filename")
    exit(1)

filename = sys.argv[1]

document = Document(filename)

sections = []

skip_next_paragraph = False

excluded_titles = ["дополнительные материалы", "контрольные вопросы"]

for para in document.paragraphs:

    if (
        para.style.name.startswith("Heading")
        and para.text.lower().strip() in excluded_titles
    ):
        skip_next_paragraph = True
        continue

    if (
        para.style.name.startswith("Heading")
        and not para.text.lower().strip() in excluded_titles
    ):
        skip_next_paragraph = False

    if para.style.name.startswith("Heading") and len(para.text) > 0:
        sections.append({"title": para.text, "content": []})
        continue
    if len(sections) > 0 and len(para.text) > 0:
        sections[-1]["content"].append(para.text)

f = open("results/" + filename + ".json", "w", encoding="utf-8")
f.write(json.dumps(sections))
