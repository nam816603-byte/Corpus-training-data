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
    seen=set()
    result=[]
    for text in texts:
        if text not in seen:
            seen.add(text)
            result.append(text)
    return result


def save_dataset(text):
    output=Path(OUTPUT_DIR)
    output.mkdir(parents=True, exist_ok=True)
    path=output/OUTPUT_FILE
    path.write_text(text,encoding=ENCODING)
    print(f"Saved: {path}")


def main():
    print("CorpusBuilder")
    texts = load_files()
    print(f"Loaded {len(texts)} file(s).")
    texts = [clean_text(t) for t in texts]
    texts = remove_duplicates(texts)
    save_dataset("\n".join(texts))
    print(f"Saved {len(texts)} document(s).")
    print("Done.")

if __name__=="__main__":
    main()