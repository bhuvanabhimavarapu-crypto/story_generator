import random

def generate_story(character, genre, setting):

    openings = [
        f"One day, {character} arrived at {setting}.",
        f"{character} had always dreamed of visiting {setting}.",
        f"Everything changed when {character} entered {setting}."
    ]

    conflicts = [
        "A mysterious challenge suddenly appeared.",
        "A hidden secret was discovered.",
        "An unexpected adventure began."
    ]

    endings = [
        "In the end, everything worked out perfectly.",
        "The experience changed their life forever.",
        "It became a story remembered for years."
    ]

    story = (
        random.choice(openings) + " " +
        random.choice(conflicts) + " " +
        random.choice(endings)
    )

    return story

print(
    generate_story(
        "Bhuvana",
        "Adventure",
        "a hidden island"
    )
)
