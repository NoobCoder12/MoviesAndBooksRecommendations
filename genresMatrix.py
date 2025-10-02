# subject_to_keywords.py
# Keys: suggested Open Library subject slugs (lowercase, underscores)
# Values: extensive keyword lists (single words + multiword tokens)
#
# IMPORTANT:
# - Verify each slug exists in Open Library with:
#     GET https://openlibrary.org/subjects/{slug}.json
#   (see Subjects API docs). :contentReference[oaicite:2]{index=2}
# - You can add aliases (e.g. 'sci-fi' -> 'science_fiction') if needed.

subject_to_keywords = {
    # Fiction / Fantasy family (merged strong "fantasy" signal)
    "fantasy": [
        "fantasy", "magic", "wizard", "sorcery", "spell", "wand", "potion",
        "dragon", "elf", "dwarf", "orc", "hobbit", "troll", "giant", "fairy",
        "myth", "legend", "mythology", "fellowship", "ring", "quest",
        "prophecy", "dark_lord", "kingdom", "castle", "realm", "enchanted",
        "school_of_magic", "hogwarts", "quidditch", "muggle", "gryffindor",
        "slytherin", "ravenclaw", "hufflepuff", "wandmaking", "horcrux",
        "patronus", "spellbook", "magical_creature", "portal", "otherworld",
        "high_fantasy", "epic_fantasy", "urban_fantasy", "dark_fantasy"
    ],

    # Science fiction / sci-fi
    "science_fiction": [
        "science fiction", "science_fiction", "sci-fi", "space", "spaceship",
        "galaxy", "planet", "alien", "extraterrestrial", "robot", "android",
        "cyborg", "artificial_intelligence", "ai", "time_travel", "wormhole",
        "future", "dystopia", "postapocalyptic", "utopia", "colonization",
        "terraforming", "quantum", "nanotechnology", "cyberpunk", "space_opera"
    ],

    # Mystery / Detective (Open Library commonly uses these long slugs)
    "mystery_and_detective_stories": [
        "mystery", "detective", "whodunit", "investigation", "clues", "murder",
        "crime", "sleuth", "private_investigator", "case", "evidence",
        "suspense", "police_procedural", "locked_room", "forensic", "conspiracy"
    ],

    # Historical fiction / history
    "historical_fiction": [
        "historical fiction", "historical", "period", "era", "medieval",
        "renaissance", "victorian", "war", "battle", "revolution", "dynasty",
        "chronicle", "historical_setting", "ancient", "empire", "kingdoms",
        "historical_characters", "costume_drama"
    ],
    "history": [
        "history", "historical", "ancient_history", "world_history",
        "military_history", "social_history", "chronicle", "historical_study",
        "archaeology", "civilization", "empire", "revolution", "war"
    ],

    # Children's & Young Adult
    "children": [
        "children", "children's", "kids", "picture_book", "bedtime_story",
        "early_reader", "young_children", "talking_animals", "friendship",
        "imagination", "school", "family", "playful", "moral_story"
    ],
    "young_adult": [
        "young adult", "ya", "teen", "coming_of_age", "school", "friendship",
        "first_love", "identity", "dystopian_ya", "adolescent", "high_school"
    ],

    # Romance
    "romance": [
        "romance", "love", "relationship", "courtship", "marriage", "affair",
        "romantic", "passion", "heart", "romantic_comedy", "historical_romance",
        "contemporary_romance", "paranormal_romance"
    ],

    # Horror
    "horror": [
        "horror", "ghost", "haunted", "possession", "demon", "curse", "monster",
        "vampire", "werewolf", "zombie", "psychological_horror", "gothic",
        "nightmare", "terror", "creepy", "body_horror"
    ],

    # Adventure / Action
    "adventure": [
        "adventure", "journey", "voyage", "expedition", "treasure", "island",
        "pirates", "ship", "survival", "explorer", "mountain", "wilderness",
        "rescue", "escape", "pursuit"
    ],

    # Biography / Memoir / Nonfiction family
    "biography": [
        "biography", "memoir", "autobiography", "life_story", "personal_account",
        "diary", "letters", "profile", "portrait", "legacy"
    ],
    "nonfiction": [
        "nonfiction", "non-fiction", "fact", "essay", "reportage", "journalism",
        "study", "analysis", "guide", "manual", "reference", "how_to", "guidebook"
    ],

    # Poetry, Plays, Short stories
    "poetry": [
        "poetry", "poems", "verse", "sonnet", "ballad", "free_verse", "lyric",
        "epic_poem", "poet"
    ],
    "plays": [
        "play", "drama", "theatre", "stage", "act", "scene", "tragicomedy",
        "farce", "Shakespeare", "monologue"
    ],
    "short_stories": [
        "short_story", "short_stories", "collection", "anthology", "flash_fiction"
    ],

    # Thriller / Suspense
    "thriller": [
        "thriller", "suspense", "espionage", "spy", "conspiracy", "kidnap",
        "assassination", "high_stakes", "chase", "intense"
    ],

    # Science / Popular science / Reference
    "science": [
        "science", "physics", "chemistry", "biology", "astronomy", "mathematics",
        "research", "experiment", "theory", "popular_science", "scientific_study"
    ],
    "reference": [
        "reference", "dictionary", "encyclopedia", "atlas", "handbook", "glossary",
        "index", "guide", "manual", "compendium"
    ]
}

# End of file
