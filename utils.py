from typing import List

from spacy.language import Language
from spacy.tokens.doc import Doc


def chunked(lines: List[str], chunk_size=512) -> List[str]:
    chunks: List[str] = []
    next_chunk = ""
    for line in lines:
        if len(f"{line}\n{next_chunk}") < chunk_size:
            next_chunk = f"{line}\n{next_chunk}"
        if len(f"{line}\n{next_chunk}") > chunk_size:
            chunks.append(next_chunk)
            next_chunk = line
    chunks.append(next_chunk)
    return chunks


def nlp_chunked(nlp: Language, text: str, chunk_size=1024):
    """
    nlp model should be spacy.load("en_core_web_md") or similar
    """
    doc: Doc = nlp(text)
    chunks = []
    next_chunk = ""
    for sent in doc.sents:
        line = sent.text
        if len(f"{line}\n{next_chunk}") < chunk_size:
            next_chunk = next_chunk + line
        if len(f"{line}\n{next_chunk}") > chunk_size:
            chunks.append(next_chunk)
            next_chunk = line
    chunks.append(next_chunk)
    return chunks
