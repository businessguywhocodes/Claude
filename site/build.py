"""Bundle the Markdown modules in course/ into a single self-contained site/index.html."""

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "course"
SITE = ROOT / "site"
DIAGRAMS = COURSE / "diagrams"

# Light-theme colours for the standalone diagram files GitHub shows. In the web
# page the same classes are styled from the page's theme tokens instead.
STANDALONE_STYLE = """<style>
svg{color:#18211e}
.t{font:500 13px "Avenir Next","Segoe UI",system-ui,sans-serif;fill:#18211e}
.b{font-weight:700}
.ts{font:12px "Avenir Next","Segoe UI",system-ui,sans-serif;fill:#5b6863}
.tm{font:500 12px "Avenir Next","Segoe UI",system-ui,sans-serif;fill:#b97a0c}
.ta{font:600 12px "Avenir Next","Segoe UI",system-ui,sans-serif;fill:#0e6b66}
.bx{fill:#ffffff;stroke:#c9d2cd;stroke-width:1.5}
.bxa{fill:#e2efed;stroke:#0e6b66;stroke-width:1.5}
.bxm{fill:#f8edd6;stroke:#b97a0c;stroke-width:1.5}
.ln{stroke:#5b6863;stroke-width:1.5;fill:none}
.lna{stroke:#0e6b66;stroke-width:2;fill:none}
.lnm{stroke:#b97a0c;stroke-width:2;fill:none}
.dash{stroke-dasharray:5 4}
.ahf{fill:#5b6863;fill:context-stroke}
</style>"""

FIGURE_RE = re.compile(r"!\[([^\]]*)\]\(diagrams/([\w-]+)\.svg\)\n\*(.+?)\*\n")

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
    ("showcase", "showcase.md", "Expo", "top", "Showcase: real artifacts", "Extras · Real-world examples", False),
    ("prompts", "prompt-library.md", "Desk", "top", "Prompt library", "Concierge desk · Reference", False),
]


def build_diagrams():
    """Write standalone SVGs for GitHub and return {name: inline svg} for the page."""
    inline = {}
    for src in sorted((DIAGRAMS / "src").glob("*.svg")):
        svg = src.read_text(encoding="utf-8").strip()
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
        w, h = m.group(1), m.group(2)
        head_end = svg.index(">") + 1
        standalone = (
            svg[:head_end] + "\n" + STANDALONE_STYLE
            + f'\n<rect width="{w}" height="{h}" fill="#f6f7f4"/>' + svg[head_end:] + "\n"
        )
        (DIAGRAMS / src.name).write_text(standalone, encoding="utf-8")
        inline[src.stem] = svg.replace("\n", "")
    return inline


def inline_figures(md, diagrams):
    def repl(m):
        alt, name, caption = m.groups()
        return (
            f'<figure class="dg"><div class="dgscroll">{diagrams[name]}</div>'
            f"<figcaption>{html.escape(caption)}</figcaption></figure>\n"
        )
    return FIGURE_RE.sub(repl, md)


def write_quiz_markdown(quizzes):
    titles = {mid: short for mid, _, _, _, short, _, _ in MODULES}
    nums = {mid: file[:2] for mid, file, *_ in MODULES}
    lines = [
        "# Module Quizzes",
        "",
        "_Generated from `quizzes.json` by `site/build.py`. The web version of the course has these as interactive quizzes._",
        "",
    ]
    for mid, questions in quizzes.items():
        lines += [f"## Module {int(nums[mid])}: {titles[mid]}", ""]
        for i, q in enumerate(questions, 1):
            lines.append(f"**{i}. {q['q']}**")
            lines.append("")
            for j, opt in enumerate(q["options"]):
                lines.append(f"- {'ABCD'[j]}. {opt}")
            lines += [
                "",
                "<details><summary>Answer</summary>",
                "",
                f"**{'ABCD'[q['answer']]}.** {q['why']}",
                "",
                "</details>",
                "",
            ]
    (COURSE / "quizzes.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fragment", help="also write a body-only HTML fragment to this path")
    args = parser.parse_args()

    diagrams = build_diagrams()
    quizzes = json.loads((COURSE / "quizzes.json").read_text(encoding="utf-8"))
    write_quiz_markdown(quizzes)

    data = [
        {
            "id": mid,
            "file": file,
            "room": room,
            "floor": floor,
            "short": short,
            "label": label,
            "countable": countable,
            "md": inline_figures((COURSE / file).read_text(encoding="utf-8"), diagrams),
            "quiz": quizzes.get(mid, []),
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
