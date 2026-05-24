import json
import re

def check_courses():
    with open('courses.js', 'r') as f:
        content = f.read()

    # Extracting the curriculum list using regex
    curriculum_match = re.search(r'const curriculum = \{(.*?)\};', content, re.DOTALL)
    # Extracting the manifest keys using regex
    manifest_match = re.findall(r'"(.*?)"\s*:', content[content.find('const courseManifest'):])
    
    # Simple list of all courses in the curriculum menu
    menu_courses = re.findall(r'"(.*?)"', curriculum_match.group(1))
    
    # Check for mismatches
    missing_in_manifest = [c for c in menu_courses if c not in manifest_match]
    
    if missing_in_manifest:
        print("❌ Mismatch Found! The following courses are in your menu but missing content:")
        for course in missing_in_manifest:
            print(f" -> {course}")
    else:
        print("✅ Success! Every course in your menu has matching content.")

check_courses()