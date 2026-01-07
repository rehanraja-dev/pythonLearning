import fitz, pymupdf4llm

path = "sample.pdf"

def validate_document(path):
    doc = fitz.open(path)
    if len(doc) == 0:
        raise ValueError("Empty PDF")

    if not str(doc[0].get_text()).strip():
        raise ValueError("Scanned or non-text PDF")

    return True

# print(validate_document(path))

md_text = pymupdf4llm.to_markdown(
    "sample.pdf",
    page_chunks=False
)

print(md_text)

def normalize_markdown(md):
    lines = []
    for line in md.split("\n"):
        if "ACT NO." in line:
            continue
        lines.append(line.strip())
        aa = "\n".join(lines)
    return aa

# print(normalize_markdown(md_text))
import re

def recover_structure(md_text):
    lines = md_text.split("\n")
    recovered = []

    for line in lines:
        line = line.strip()

        if line.startswith("**Subject:"):
            recovered.append("# Subject")
            recovered.append(line)

        elif line.startswith("**And whereas"):
            recovered.append("## Background & Legal Basis")
            recovered.append(line)

        elif re.match(r"\*\*\(\w+\)\*\*", line):
            recovered.append("## Direction")
            recovered.append(line)

        elif line.startswith("**Annexure"):
            recovered.append("# " + line.replace("**", ""))

        else:
            recovered.append(line)

    return "\n".join(recovered)



def semantic_chunks(md_text):
    chunks = []
    current = {"heading": None, "content": ""}

    for line in str(md_text).split("\n"):
        if line.startswith("*"):
            if current["content"]:
                chunks.append(current)
            current = {
                "heading": line.strip("# ").strip(),
                "content": ""
            }
        else:
            current["content"] += line + "\n"

    if current["content"]:
        chunks.append(current)

    return chunks

print(semantic_chunks(recover_structure))