# Prompt Library

Copy, paste, and fill in the `[brackets]`. Each prompt follows the briefing formula from Module 3. Adapt freely.

## Everyday

**Briefing template**
```
Context: [who I am, the situation, why it matters]
Task: [what I want]
Audience: [who it's for]
Good looks like: [goal and success criteria]
Constraints: [length, tone, format, must-include, must-avoid]
Materials: [paste or attach]
Before you start, ask me any questions you need answered to do this well.
```

**Rewrite for clarity**
```
Rewrite this so a busy [reader] understands it in 30 seconds. Lead with the main point or ask, keep every number and decision, and cut everything else.
"""
[text]
"""
```

**Get a tough critique**
```
Critique this [document/plan/email] as [specific reader, e.g. a sceptical CFO / a first-time guest / a hotel owner who distrusts tech]. Be direct. List what's unclear, weak, unsupported, or missing, in order of importance. Then suggest the 3 changes that would improve it most.
"""
[text]
"""
```

**Decide between options**
```
I'm deciding between [options]. Context: [details]. First ask me what matters most to me. Then build a weighted decision matrix, give a recommendation, and make the strongest case for the option you didn't recommend.
```

**Learn a topic**
```
Teach me [topic]. Start by asking what I already know. Explain one concept at a time with a real-world example, check my understanding with a question, and only move on when I get it right.
```

**Continue in a fresh chat**
```
Summarise everything we've decided and produced in this conversation so I can paste it into a new chat: goals, decisions, open questions, and the latest version of any drafts.
```

## Work: hospitality and startups

**Guest complaint reply**
```
I handle guest relations at [property, type, location]. A guest wrote the message below. Write a reply that apologises sincerely without excuses, acknowledges each specific issue, offers [compensation options], and invites them back. Under [N] words, warm and professional, signed "[name, role]". Don't promise [things we can't control].
Guest message:
"""
[paste, with personal details removed]
"""
```

**Review analysis**
```
Attached are [N] guest reviews from [period]. Identify the top 5 praise themes and top 5 complaint themes, with rough frequency and 2 representative quotes each. Then recommend the 3 fixes with the biggest likely impact on ratings, and how we'd know they worked.
```

**Review responses**
```
Draft responses to each review below. Thank them, reference something specific they said, address any complaint without being defensive, and invite them back. Under 80 words each, in our voice: [describe voice].
```

**SOP from a messy process**
```
Here's how we currently do [process], in rough notes. Turn it into a clear SOP: purpose, roles, step-by-step instructions, what to do when things go wrong, and a short checklist version for the wall.
"""
[notes]
"""
```

**Meeting notes to actions**
```
Here are notes or a transcript from [meeting]. Give me: (1) decisions made, (2) action items as a table with owner, task, and due date, (3) open questions, (4) a 5-line summary I can send to people who weren't there.
```

**Prospect research brief**
```
With web search, research [hotel/group/company]: size, locations, positioning, recent news, likely priorities and pain points, and who the decision-makers probably are. Then suggest the best angle for our outreach about [product], and 3 questions to ask on a first call. Cite sources.
```

**Outreach sequence**
```
Write a 3-email outreach sequence to [audience] about [offer]. Plain language, no hype, under 120 words each, one clear ask per email, spaced [timing]. Email 1 leads with their likely problem, email 2 with proof ([case study/data]), and email 3 is a short, friendly break-up note.
```

**Campaign ideas**
```
Give me 10 campaign ideas for [property/brand] for [season/occasion], ranging from safe to bold. For each: the target guest, the core message, the main channel, and one way to measure success.
```

**Data analysis**
```
Attached is [data export]. Show me [metrics] by [dimensions], with a chart for each. Then tell me the 3 most important patterns, what might explain them, and what you'd want to check before acting. Show your calculations so I can verify the key numbers.
```

**Monthly business review**
```
Turn these metrics and notes into a one-page monthly review for [audience]: headline (one sentence), 3 highlights, 3 concerns, a metrics table vs. last month and target, and recommended actions with owners.
```

**Feature spec**
```
Turn this idea into a one-page spec: problem, target users, goals and non-goals, user stories, success metrics, risks, and open questions. Ask me clarifying questions first.
Idea: [description]
```

**Job description and interview kit**
```
Write a job description for [role] at [company stage/context]. Be honest about the pace and ambiguity. Include what success looks like at 30, 60, and 90 days. Then create 8 structured interview questions with a 1–4 scoring rubric for each.
```

**Investor update**
```
Turn these notes and metrics into a monthly investor update: TL;DR (3 bullets), highlights, lowlights (honest), key metrics table, what we're focused on next month, and specific asks (intros, hires, advice).
```

## Personal

**Trip planner**
```
Plan a [N]-day trip to [place] in [month] for [who, with ages and constraints]. We like [interests] and dislike [dislikes]. Budget about [amount] excluding flights. Give a day-by-day plan, where to stay, what to book in advance, and a rainy-day backup. Ask me questions first.
```

**Budget review**
```
Here's my spending export for [period]. Categorise it, show where the money goes (a table and a chart), compare it with [budget/goal], and suggest 3 realistic changes. Be practical, not preachy.
```

**Doctor visit prep**
```
I have an appointment about [issue]. Help me prepare: a short summary of my symptoms and history to share (I'll fill in details), what to track before the visit, and the most useful questions to ask. Don't diagnose me.
```

**Hard conversation**
```
I need to talk to [person] about [issue]. My goal is [outcome] while keeping the relationship good. Help me plan what to say, anticipate their likely reactions, and suggest how to respond to each. Then role-play it with me, playing them realistically.
```

**Meal planning**
```
Plan [N] dinners for [household] this week. Constraints: [diet, time per meal, budget, dislikes]. Use overlapping ingredients to reduce waste, and give me one combined shopping list grouped by store section.
```

**Gift ideas**
```
Suggest 10 gift ideas for [person: age, relationship, interests, what they already have] with a budget of [amount]. Mix practical, experiential, and sentimental options, and say why each fits.
```

## Advanced

**Structured prompt with tags**
```
<context>[background]</context>
<documents>
  <document name="[name]">[content]</document>
</documents>
<task>[what to do]</task>
<output_format>[exact structure]</output_format>
```

**Quotes first, then answer**
```
First, find the quotes from the documents that are relevant to [question] and list them in <quotes> tags. Then answer the question using only those quotes. If the documents don't answer it, say so.
```

**Self-check and revise**
```
Here are the criteria: [list]. Score your draft against each criterion, explain any misses, then produce a revised version that meets all of them.
```

**Build a reusable prompt**
```
I want a reusable prompt for [task] that I'll run [frequency] on [inputs]. Interview me about the goal, audience, format, and edge cases. Then write the prompt with an example input and output. Finally, suggest 5 test cases, including tricky ones.
```

**Create a skill**
```
Help me create a skill for [task]. Interview me about the steps, standards, tone, examples of good output, and common mistakes. Then package it as a SKILL.md with a clear description of what it does and when to use it.
```

**Delegate to an agent**
```
Goal: [outcome]
Context: [where the files and tools are, background]
Done means: [specific deliverable and quality bar]
Boundaries: [what not to do: no sending, deleting, purchasing, logging in...]
Checkpoint: [when to stop and show me progress]
```
