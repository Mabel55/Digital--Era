"""
Batch 56: Deep Dive into Mobile Development (Flutter Framework Masterclass)
"""
import json, os

NEW_COURSES_BATCH56 = {
    "Flutter Framework Masterclass": {
        "tier": "Intermediate",
        "aiRubric": "Assess deep understanding of Flutter and Dart",
        "lessons": [
            {"title": "Everything is a Widget", "theory": "## The Widget Tree\\nIn Flutter, everything you see on the screen is a Widget. A `StatelessWidget` never changes its appearance after it's built, while a `StatefulWidget` can dynamically update its UI based on internal state changes.", "instructions": "## Task: Base Class\\nIf you want to create a UI component that maintains an internal counter, which class should it inherit from?", "starterCode": "# Options: StatelessWidget, StatefulWidget, InheritedWidget\\nbase_class = '___'", "solution": "# Options: StatelessWidget, StatefulWidget, InheritedWidget\\nbase_class = 'StatefulWidget'", "hint": "It needs state, so it's a StatefulWidget", "rubric": "Identifies StatefulWidget."},
            {"title": "Dart Language Basics", "theory": "## Sound Null Safety\\nFlutter uses the Dart programming language. Modern Dart features 'Sound Null Safety', meaning variables cannot contain `null` by default unless you explicitly allow it using a question mark `?`.", "instructions": "## Task: Nullable Types\\nDeclare a String variable named `username` that is allowed to be null.", "starterCode": "String___ username = null;", "solution": "String? username = null;", "hint": "Use a question mark ?", "rubric": "Uses String?."},
            {"title": "Layouts in Flutter", "theory": "## Flex Layouts\\nTo arrange widgets horizontally, you use a `Row`. To arrange them vertically, you use a `Column`. These behave very similarly to CSS Flexbox.", "instructions": "## Task: Vertical Alignment\\nCreate a layout widget that stacks its children vertically.", "starterCode": "___(\\n  children: <Widget>[\\n    Text('Top'),\\n    Text('Bottom'),\\n  ],\\n)", "solution": "Column(\\n  children: <Widget>[\\n    Text('Top'),\\n    Text('Bottom'),\\n  ],\\n)", "hint": "Use Column", "rubric": "Uses Column."},
            {"title": "State Management with Provider", "theory": "## Global State\\nPassing state down through multiple widgets (prop drilling) is painful. `Provider` is the officially recommended package to inject global state into the widget tree so any widget can listen to it.", "instructions": "## Task: State Architecture\\nWhat is the name of the popular pattern used with Provider where a model class notifies listeners of changes?", "starterCode": "# Options: ChangeNotifier, Redux, BLoC\\npattern = '___'", "solution": "# Options: ChangeNotifier, Redux, BLoC\\npattern = 'ChangeNotifier'", "hint": "ChangeNotifier", "rubric": "Identifies ChangeNotifier."},
            {"title": "Routing and Navigation", "theory": "## Managing Screens\\nIn Flutter, screens are called 'Routes'. You move between screens using the `Navigator` widget, pushing new routes onto a stack.", "instructions": "## Task: Push a Route\\nWrite the command used to push a new screen onto the navigation stack.", "starterCode": "Navigator.___(context, MaterialPageRoute(builder: (context) => SecondScreen()));", "solution": "Navigator.push(context, MaterialPageRoute(builder: (context) => SecondScreen()));", "hint": "Use push", "rubric": "Uses push."},
            {"title": "API Integration", "theory": "## Fetching Data\\nTo fetch data from a REST API, you typically use the `http` package and dart's built-in `dart:convert` library to decode the JSON response into a Dart Map.", "instructions": "## Task: Decode JSON\\nDecode the raw JSON string response into a dynamic map.", "starterCode": "import 'dart:convert';\\n\\nvar data = ___.decode(response.body);", "solution": "import 'dart:convert';\\n\\nvar data = json.decode(response.body);", "hint": "Use json.decode", "rubric": "Uses json.decode."},
            {"title": "Animations in Flutter", "theory": "## Implicit Animations\\nFlutter makes animation incredibly easy with 'Implicitly Animated Widgets'. For example, if you change the properties of an `AnimatedContainer`, it will automatically transition smoothly without you writing an animation controller.", "instructions": "## Task: Animated Widget\\nChange the standard `Container` to one that automatically animates changes to its size or color.", "starterCode": "___(\\n  duration: Duration(seconds: 1),\\n  color: isBlue ? Colors.blue : Colors.red,\\n)", "solution": "AnimatedContainer(\\n  duration: Duration(seconds: 1),\\n  color: isBlue ? Colors.blue : Colors.red,\\n)", "hint": "Use AnimatedContainer", "rubric": "Uses AnimatedContainer."},
            {"title": "Publishing to App Stores", "theory": "## The Final Build\\nBefore you can upload your Flutter app to the Google Play Store or Apple App Store, you must digitally sign the app and compile it into a release bundle.", "instructions": "## Task: Build Command\\nWhat terminal command creates an optimized release bundle for Android?", "starterCode": "flutter build ___", "solution": "flutter build appbundle", "hint": "Build an appbundle", "rubric": "Uses appbundle."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'mobile_development.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH56.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH56.items():
            tier = course_info["tier"]
            if "Mobile Development" in index_data and tier in index_data["Mobile Development"]:
                if new_course_name not in index_data["Mobile Development"][tier]:
                    index_data["Mobile Development"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 56: Added {total} lessons to Mobile Development track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
