# -*- coding: utf-8 -*-
"""
patcher.py - Universal theory patcher
Loads theory from JSON data files and patches the curriculum tracks.
Run: python patcher.py [track_name]
Or:  python patcher.py   (patches all available)
"""
import json, os, sys

TRACKS_DIR = os.path.join("curriculum", "tracks")
DATA_DIR   = "theory_data"

def patch(track_filename, theory_dict):
    track_path = os.path.join(TRACKS_DIR, track_filename)
    print(f"\n{'='*55}")
    print(f"Patching {track_filename}...")

    with open(track_path, encoding="utf-8") as f:
        data = json.load(f)

    patched = 0; still_short = 0
    for topic_data in data.values():
        for lesson in topic_data.get("lessons", []):
            title = lesson.get("title", "")
            if title in theory_dict:
                lesson["theory"] = theory_dict[title]
                patched += 1
            elif lesson.get("type") != "quiz" and len(lesson.get("theory","")) <= 800:
                still_short += 1
                print(f"  [??] No theory for: {title!r}")

    print(f"Patched: {patched} | Still short: {still_short}")
    with open(track_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved.")
    return patched


def load_and_patch(data_json_path, track_filename):
    with open(data_json_path, encoding="utf-8") as f:
        data = json.load(f)
    # Data can be {track_name: {lesson_title: theory}} or {lesson_title: theory}
    if track_filename.replace(".json","") in data:
        theory_dict = data[track_filename.replace(".json","")]
    else:
        theory_dict = data
    patch(track_filename, theory_dict)


if __name__ == "__main__":
    # Patch all JSON files in theory_data/ that match a track
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    for data_file in sorted(files):
        track_file = data_file  # Same name as track file
        track_path = os.path.join(TRACKS_DIR, track_file)
        if os.path.exists(track_path):
            load_and_patch(os.path.join(DATA_DIR, data_file), track_file)
        else:
            print(f"No matching track for {data_file}")
    print("\n\nAll done!")
