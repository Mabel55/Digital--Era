import os
import json
import dotenv
dotenv.load_dotenv()
from database import SessionLocal, engine
import models

def seed_from_json():
    # Ensure tables exist
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    tracks_dir = os.path.join("curriculum", "tracks")
    
    if not os.path.exists(tracks_dir):
        print(f"Error: {tracks_dir} not found.")
        return

    print("🌱 Starting database seeding from JSON tracks...")
    
    total_courses = 0
    total_lessons = 0

    try:
        for filename in os.listdir(tracks_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(tracks_dir, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    track_data = json.load(f)
                    
                    for course_name, course_data in track_data.items():
                        # Check if course already exists to avoid duplicates
                        existing_course = db.query(models.Course).filter(models.Course.name == course_name).first()
                        if existing_course:
                            print(f"⏩ Skipping existing course: {course_name}")
                            continue
                            
                        # Create Course
                        new_course = models.Course(
                            name=course_name, 
                            description=f"Course module for {course_name}"
                        )
                        db.add(new_course)
                        db.commit()
                        db.refresh(new_course)
                        total_courses += 1
                        print(f"✅ Created Course: {new_course.name}")

                        # Check if course_data has a 'lessons' array
                        if "lessons" in course_data and isinstance(course_data["lessons"], list):
                            for lesson_data in course_data["lessons"]:
                                title = lesson_data.get("title", "Untitled Lesson")
                                content = lesson_data.get("theory", "") + "\n\n" + lesson_data.get("instructions", "")
                                expected_output = lesson_data.get("solution", "No exact solution provided")
                                
                                new_lesson = models.Lesson(
                                    title=title,
                                    content=content,
                                    expected_output=expected_output,
                                    course_id=new_course.id
                                )
                                db.add(new_lesson)
                                total_lessons += 1
                        else:
                            # If it's a single lesson module
                            title = course_name
                            content = course_data.get("instructions", "No instructions")
                            expected_output = course_data.get("solution", "No solution")
                            
                            new_lesson = models.Lesson(
                                title=title,
                                content=content,
                                expected_output=expected_output,
                                course_id=new_course.id
                            )
                            db.add(new_lesson)
                            total_lessons += 1

                        db.commit()
        
        print(f"🎉 Successfully seeded {total_courses} courses and {total_lessons} lessons!")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_from_json()
