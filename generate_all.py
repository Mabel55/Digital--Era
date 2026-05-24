def generate_all_courses():
    print("const courseManifest = {")
    for i in range(1, 21):
        key = f"Course {i}"
        # Determine if we need a comma at the end
        comma = "," if i < 20 else ""
        
        block = f'''    "{key}": {{
        "instructions": "### Coming Soon\\nThis lesson is currently under development. Check back soon!",
        "starterCode": "# Course {i} content coming soon...",
        "aiRubric": "Placeholder course."
    }}{comma}'''
        print(block)
    print("};")

if __name__ == "__main__":
    generate_all_courses()