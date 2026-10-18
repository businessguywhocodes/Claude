# Claude 101 and Beyond

A practical course on understanding Claude, using it well, and getting the most out of it in personal and professional life. Written for friends at HotelBFF, so work examples lean toward hotels, travel, and startups.

## Read the course

- **On GitHub:** start with [course/00-welcome.md](course/00-welcome.md) and follow the modules in order.
- **As a web page:** open [site/index.html](site/index.html) in a browser. It's a single file with every module, diagrams, an interactive quiz at the end of each module, a sidebar, progress tracking, and light/dark themes.

## Contents

| # | Module | Track |
|---|---|---|
| 0 | [Welcome](course/00-welcome.md) | |
| 1 | [How Claude Actually Works](course/01-how-claude-works.md) | A. Foundations |
| 2 | [Getting Set Up](course/02-getting-set-up.md) | A. Foundations |
| 3 | [Prompting That Works](course/03-prompting-that-works.md) | A. Foundations |
| 4 | [Files, Images, and Making Things](course/04-files-and-making-things.md) | A. Foundations |
| 5 | [Accuracy, Privacy, and Judgment](course/05-accuracy-privacy-judgment.md) | A. Foundations |
| 6 | [Projects, Memory, and Styles](course/06-projects-memory-styles.md) | B. Everyday leverage |
| 7 | [Research and Web Search](course/07-research-and-web-search.md) | B. Everyday leverage |
| 8 | [Claude in Your Personal Life](course/08-claude-in-personal-life.md) | B. Everyday leverage |
| 9 | [Claude at Work](course/09-claude-at-work.md) | B. Everyday leverage |
| 10 | [Advanced Prompting](course/10-advanced-prompting.md) | C. Advanced |
| 11 | [Connectors and Skills](course/11-connectors-and-skills.md) | C. Advanced |
| 12 | [Agents: Claude Code, Cowork, and Claude in Chrome](course/12-agents.md) | C. Advanced |
| 13 | [Building with the Claude API](course/13-building-with-the-api.md) | C. Advanced (optional) |
| 14 | [Capstone, 30-Day Plan, and Cheat Sheet](course/14-capstone.md) | |
| | [Showcase: Real Artifacts People Have Built](course/showcase.md) | Extras |
| | [Prompt Library](course/prompt-library.md) | Reference |
| | [Module Quizzes](course/quizzes.md) | Practice |

Total time: about 6 hours of reading and exercises, plus a 30-day practice plan.

## Editing the course

The Markdown files in `course/` are the source. After editing them, rebuild the web page:

```bash
python3 site/build.py
```

This writes `site/index.html` with the modules embedded, and regenerates `course/quizzes.md` (from `course/quizzes.json`) and the standalone diagrams in `course/diagrams/` (from `course/diagrams/src/`).

- **Quizzes:** edit `course/quizzes.json`. `answer` is the 0-based index of the correct option.
- **Diagrams:** edit the SVGs in `course/diagrams/src/`. They use shared class names (`bx`, `bxa`, `ln`, `t`, ...) that the web page colours from its theme. Reference one in a module as an image followed by an italic caption line:

  ```markdown
  ![Short alt text](diagrams/agent-loop.svg)
  *Caption that says what the diagram shows.*
  ```

_Written October 2026. Claude's features change often; the ideas last longer than the menus._
