import json

# List all the course titles you have in your Menu (curriculum)
courses_to_initialize = [
    "Introduction to FastAPI Routing",
    "Connecting to PostgreSQL with SQLAlchemy",
    "Building a CRUD API for a Bookstore",
    "Course 4", "Course 5", "Course 6", "Course 7", 
    "Course 8", "Course 9", "Course 10", "Course 11", 
    "Course 12", "Course 13", "Course 14", "Course 15", 
    "Course 16", "Course 17", "Course 18", "Course 19", "Course 20"
]

def generate_placeholders():
    manifest_data = {}
    
    for title in courses_to_initialize:
        manifest_data[title] = {
            "instructions": f"### {title}\n\nThis lesson is currently under development by Mabel Academy. Check back soon for the full curriculum!",
            "starterCode": "# Course content coming soon...",
            "aiRubric": "No grading available for placeholder courses."
        }
    
    # Output this to the console so you can copy-paste it
    print(json.dumps(manifest_data, indent=4))

if __name__ == "__main__":
    generate_placeholders()