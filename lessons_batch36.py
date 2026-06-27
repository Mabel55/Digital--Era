"""
Batch 36: Expanding Mobile Development Curriculum (Flutter, State, Push Notifications, Offline, CI/CD)
"""
import json, os

NEW_COURSES_BATCH36 = {
    "Flutter Intro": {
        "tier": "Beginner",
        "aiRubric": "Assess Flutter basics",
        "lessons": [
            {"title": "Widgets are Everything", "theory": "## The Flutter Paradigm\\nIn Flutter, everything is a widget. A layout is a tree of widgets, and even structural elements like padding or alignment are themselves widgets.", "instructions": "## Task: Create a Text Widget\\nReturn a simple Text widget with the string 'Hello Flutter' centered on the screen.", "starterCode": "import 'package:flutter/material.dart';\\n\\nWidget buildHello() {\\n  return Center(\\n    child: ___('___'),\\n  );\\n}", "solution": "import 'package:flutter/material.dart';\\n\\nWidget buildHello() {\\n  return Center(\\n    child: Text('Hello Flutter'),\\n  );\\n}", "hint": "Use Text('Hello Flutter')", "rubric": "Correctly instantiates the Text widget with the string."},
            {"title": "Stateful vs Stateless", "theory": "## Managing State\\n`StatelessWidget` is for static UI, while `StatefulWidget` is for UI that changes over time (like a counter or a form).", "instructions": "## Task: SetState\\nUpdate the counter variable inside the `setState` method to trigger a UI rebuild.", "starterCode": "void incrementCounter() {\\n  setState(() {\\n    _counter ___ 1;\\n  });\\n}", "solution": "void incrementCounter() {\\n  setState(() {\\n    _counter += 1;\\n  });\\n}", "hint": "Use += 1", "rubric": "Correctly increments the counter inside setState."}
        ]
    },
    "State Management in React Native": {
        "tier": "Intermediate",
        "aiRubric": "Assess state management",
        "lessons": [
            {"title": "Zustand Setup", "theory": "## Lightweight Global State\\nZustand is a fast, scalable state-management solution for React Native. It uses hooks and avoids boilerplate.", "instructions": "## Task: Create a Store\\nCreate a Zustand store with a `bears` count of 0 and an `increasePopulation` function.", "starterCode": "import { create } from 'zustand'\\n\\nconst useStore = ___((set) => ({\\n  bears: 0,\\n  increasePopulation: () => set((state) => ({ bears: state.bears + ___ })),\\n}))", "solution": "import { create } from 'zustand'\\n\\nconst useStore = create((set) => ({\\n  bears: 0,\\n  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),\\n}))", "hint": "Use create and add 1", "rubric": "Correctly uses create and increments by 1."},
            {"title": "Redux Toolkit", "theory": "## Robust State Architecture\\nFor larger apps, Redux Toolkit provides a standardized way to write Redux logic, including 'slices' that bundle reducers and actions.", "instructions": "## Task: Create a Slice\\nDefine a slice named 'counter' with an initial state of 0.", "starterCode": "import { createSlice } from '@reduxjs/toolkit'\\n\\nconst counterSlice = ___({\\n  name: '___',\\n  initialState: { value: 0 },\\n  reducers: {\\n    increment: (state) => { state.value += 1 }\\n  }\\n})", "solution": "import { createSlice } from '@reduxjs/toolkit'\\n\\nconst counterSlice = createSlice({\\n  name: 'counter',\\n  initialState: { value: 0 },\\n  reducers: {\\n    increment: (state) => { state.value += 1 }\\n  }\\n})", "hint": "Use createSlice and name it 'counter'", "rubric": "Correctly invokes createSlice and names it."}
        ]
    },
    "Push Notifications": {
        "tier": "Intermediate",
        "aiRubric": "Assess push notification handling",
        "lessons": [
            {"title": "Requesting Permissions", "theory": "## User Consent\\nBefore sending push notifications on iOS and Android (13+), you must explicitly request permission from the user.", "instructions": "## Task: Expo Notifications\\nWrite the code to request permission using Expo's notification module.", "starterCode": "import * as Notifications from 'expo-notifications';\\n\\nasync function requestPermissions() {\\n  const { status } = await Notifications.___();\\n  return status === '___';\\n}", "solution": "import * as Notifications from 'expo-notifications';\\n\\nasync function requestPermissions() {\\n  const { status } = await Notifications.requestPermissionsAsync();\\n  return status === 'granted';\\n}", "hint": "Use requestPermissionsAsync and 'granted'", "rubric": "Requests permissions and checks for 'granted' status."},
            {"title": "Handling Foreground Messages", "theory": "## In-App Notifications\\nWhen the app is open (foreground), notifications don't show up in the system tray by default. You need an event listener to handle them.", "instructions": "## Task: Notification Listener\\nSet up a listener to console log the notification when received in the foreground.", "starterCode": "import * as Notifications from 'expo-notifications';\\n\\nNotifications.___(\\n  notification => {\\n    console.log('Received:', notification);\\n  }\\n);", "solution": "import * as Notifications from 'expo-notifications';\\n\\nNotifications.addNotificationReceivedListener(\\n  notification => {\\n    console.log('Received:', notification);\\n  }\\n);", "hint": "Use addNotificationReceivedListener", "rubric": "Correctly attaches the notification listener."}
        ]
    },
    "Offline-First Apps": {
        "tier": "Advanced",
        "aiRubric": "Assess offline-first strategies",
        "lessons": [
            {"title": "AsyncStorage / SQLite", "theory": "## Local Persistence\\nOffline-first apps save data locally first, then sync to the cloud. React Native uses AsyncStorage for small data or SQLite for complex relational data.", "instructions": "## Task: Save to AsyncStorage\\nWrite the function to save a string value to AsyncStorage.", "starterCode": "import AsyncStorage from '@react-native-async-storage/async-storage';\\n\\nasync function storeData(value) {\\n  try {\\n    await AsyncStorage.___('@my_key', ___);\\n  } catch (e) {\\n    console.error(e);\\n  }\\n}", "solution": "import AsyncStorage from '@react-native-async-storage/async-storage';\\n\\nasync function storeData(value) {\\n  try {\\n    await AsyncStorage.setItem('@my_key', value);\\n  } catch (e) {\\n    console.error(e);\\n  }\\n}", "hint": "Use setItem and the value", "rubric": "Correctly calls setItem with the key and value."},
            {"title": "Sync Queues", "theory": "## Conflict Resolution\\nWhen offline, user actions are saved to a local 'Queue'. When the network returns, the app processes the queue and handles server conflicts.", "instructions": "## Task: NetInfo Check\\nUse the NetInfo library to check if the device is connected before attempting a sync.", "starterCode": "import NetInfo from '@react-native-community/netinfo';\\n\\nNetInfo.fetch().then(state => {\\n  if (state.___) {\\n    syncQueueToServer();\\n  }\\n});", "solution": "import NetInfo from '@react-native-community/netinfo';\\n\\nNetInfo.fetch().then(state => {\\n  if (state.isConnected) {\\n    syncQueueToServer();\\n  }\\n});", "hint": "Check the isConnected property", "rubric": "Checks if the state isConnected."}
        ]
    },
    "Mobile CI/CD": {
        "tier": "Advanced",
        "aiRubric": "Assess mobile CI/CD pipelines",
        "lessons": [
            {"title": "Fastlane Basics", "theory": "## Automating Deployments\\nFastlane automates tedious mobile development tasks like generating screenshots, managing provisioning profiles, and releasing to app stores.", "instructions": "## Task: Fastfile Lane\\nDefine a fastlane 'lane' named 'beta' that builds the iOS app and uploads it to TestFlight.", "starterCode": "lane :___ do\\n  build_app(workspace: \"MyApp.xcworkspace\", scheme: \"MyApp\")\\n  upload_to____\\nend", "solution": "lane :beta do\\n  build_app(workspace: \"MyApp.xcworkspace\", scheme: \"MyApp\")\\n  upload_to_testflight\\nend", "hint": "beta and testflight", "rubric": "Defines the beta lane and uploads to testflight."},
            {"title": "EAS Build (Expo)", "theory": "## Cloud Builds\\nExpo Application Services (EAS) Build allows you to compile native iOS and Android apps in the cloud without needing a Mac or Android Studio.", "instructions": "## Task: EAS Config\\nDefine the eas.json build profile for production to auto-increment the build number.", "starterCode": "{\\n  \"build\": {\\n    \"production\": {\\n      \"autoIncrement\": ___\\n    }\\n  }\\n}", "solution": "{\\n  \"build\": {\\n    \"production\": {\\n      \"autoIncrement\": true\\n    }\\n  }\\n}", "hint": "Set autoIncrement to true", "rubric": "Sets autoIncrement to boolean true."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'mobile_development.json')
    
    # 1. Update mobile_development.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH36.items():
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
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH36.items():
            tier = course_info["tier"]
            if "Mobile Development" in index_data and tier in index_data["Mobile Development"]:
                if new_course_name not in index_data["Mobile Development"][tier]:
                    index_data["Mobile Development"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 36: Added {total} lessons to Mobile Development track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
