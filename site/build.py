"""Bundle the Markdown modules in course/ into a single self-contained site/index.html."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "course"
SITE = ROOT / "site"

# (id, file, room number, floor, short title, label, counts toward progress)
MODULES = [
    ("welcome", "00-welcome.md", "Lobby", "lobby", "Welcome", "Start here", False),
    ("m01", "01-how-claude-works.md", "101", "A", "How Claude works", "Foundations · Module 1", True),
    ("m02", "02-getting-set-up.md", "102", "A", "Getting set up", "Foundations · Module 2", True),
    ("m03", "03-prompting-that-works.md", "103", "A", "Prompting that works", "Foundations · Module 3", True),
    ("m04", "04-files-and-making-things.md", "104", "A", "Files and making things", "Foundations · Module 4", True),
    ("m05", "05-accuracy-privacy-judgment.md", "105", "A", "Accuracy, privacy, judgment", "Foundations · Module 5", True),
    ("m06", "06-projects-memory-styles.md", "201", "B", "Projects, memory, styles", "Everyday leverage · Module 6", True),
    ("m07", "07-research-and-web-search.md", "202", "B", "Research and web search", "Everyday leverage · Module 7", True),
    ("m08", "08-claude-in-personal-life.md", "203", "B", "Claude in personal life", "Everyday leverage · Module 8", True),
    ("m09", "09-claude-at-work.md", "204", "B", "Claude at work", "Everyday leverage · Module 9", True),
    ("m10", "10-advanced-prompting.md", "301", "C", "Advanced prompting", "Advanced · Module 10", True),
    ("m11", "11-connectors-and-skills.md", "302", "C", "Connectors and skills", "Advanced · Module 11", True),
    ("m12", "12-agents.md", "303", "C", "Agents", "Advanced · Module 12", True),
    ("m13", "13-building-with-the-api.md", "304", "C", "Building with the API", "Advanced · Module 13 (optional)", True),
    ("capstone", "14-capstone.md", "Roof", "top", "Capstone and cheat sheet", "Capstone · Module 14", True),
    ("prompts", "prompt-library.md", "Desk", "top", "Prompt library", "Concierge desk · Reference", False),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fragment", help="also write a body-only HTML fragment to this path")
    args = parser.parse_args()

    data = [
        {
            "id": mid,
            "file": file,
            "room": room,
            "floor": floor,
            "short": short,
            "label": label,
            "countable": countable,
            "md": (COURSE / file).read_text(encoding="utf-8"),
        }
        for mid, file, room, floor, short, label, countable in MODULES
    ]
    # Escape "</" so module text can never close the surrounding <script> tag.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = (SITE / "template.html").read_text(encoding="utf-8")
    body = template.replace("/*__MODULES__*/[]", payload)

    # Standalone page for opening straight from the repo in a browser.
    page = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
        "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    )
    (SITE / "index.html").write_text(page, encoding="utf-8")
    print(f"Wrote {SITE / 'index.html'} with {len(data)} modules")

    # Body-only fragment, for hosts that supply their own document skeleton.
    if args.fragment:
        Path(args.fragment).write_text(body, encoding="utf-8")
        print(f"Wrote fragment {args.fragment}")


if __name__ == "__main__":
    main()
