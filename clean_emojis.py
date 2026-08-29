import json
import re
import glob

def remove_emojis(text):
    if not isinstance(text, str):
        return text
    # Regex to match emojis and other pictographic symbols
    # This range includes most common emojis and symbols like ✅, ❌, ⚠️, 🚀
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"       # emoticons
        u"(\ud83d[\ude80-\udeff])|"       # transport & map symbols
        u"(\ud83e[\udd00-\uddff])|"       # supplemental symbols
        u"([\u2600-\u27BF])|"             # miscellaneous symbols & dingbats
        u"(\ud83c[\udf00-\udfff])|"       # miscellaneous symbols and pictographs
        u"(\ud83d[\udc00-\uddff])|"       # miscellaneous symbols and pictographs
        u"([\u2B50])|"                    # ⭐
        u"([\u23F0])|"                    # ⏰
        u"([\u23F3])"                     # ⏳
        "+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [clean_dict(i) for i in d]
    elif isinstance(d, str):
        return remove_emojis(d)
    return d

def main():
    json_files = glob.glob('curriculum/tracks/*.json')
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cleaned_data = clean_dict(data)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, indent=2)
        print(f"Cleaned {file_path}")

if __name__ == '__main__':
    main()
