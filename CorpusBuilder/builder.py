from pathlib import Path
import re

from config import RAW_DIR, OUTPUT_DIR, OUTPUT_FILE, ENCODING


def load_files():
    texts=[]
    raw=Path(RAW_DIR)
    if not raw.exists():
        return texts
    for file in sorted(raw.rglob("*.txt")):
        try:
            texts.append(file.read_text(encoding=ENCODING))
        except Exception as e:
            print(f"Skip {file}: {e}")
    return texts


def clean_text(text):
    text=text.replace("\r\n","\n").replace("\r","\n")
    text=re.sub(r"[ \t]+"," ",text)
    text=re.sub(r"\n{3,}","\n\n",text)
    return text.strip()


def remove_duplicates(texts):
    pass


def save_dataset(text):
    pass


def main():
    print("CorpusBuilder")
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    texts=[clean_text(t) for t in load_files()]
    texts=remove_duplicates(texts)
    save_dataset("\n".join(texts))
    print("Done.")

if __name__=="__main__":
    main()