import json
import os

STATE_FILE = "series_state.json"

DEFAULT_STATE = {
    "series_title": "The Hollow Protocol",
    "genre": "Psychological Horror / Dark Mystery",
    "current_episode": 1,
    "main_character": {
        "name": "Detective Elias Thorne",
        "description": "A weary, 40-year-old male detective with dark circles under his eyes, a scruffy beard, wearing a rumpled grey trench coat and a loose tie. Cinematic moody lighting."
    },
    "plot_summary": "Elias has just arrived in the perpetually overcast town of Oakhaven, where the sun hasn't been seen in 5 years. He is looking for his missing partner.",
    "previous_events": []
}

def load_state():
    """Loads the current state of the series."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading state file: {e}. Returning default state.")
    return DEFAULT_STATE.copy()

def save_state(state):
    """Saves the current state of the series."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=4)

def update_state_after_episode(state, next_plot_summary):
    """Updates the state for the next episode."""
    state["previous_events"].append(f"Episode {state['current_episode']}: {state['plot_summary']}")
    # Keep only the last 5 events so context doesn't blow up
    if len(state["previous_events"]) > 5:
        state["previous_events"] = state["previous_events"][-5:]
        
    state["current_episode"] += 1
    state["plot_summary"] = next_plot_summary
    save_state(state)
    return state
