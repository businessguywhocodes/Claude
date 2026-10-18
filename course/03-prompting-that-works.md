# Module 3: Prompting That Works

**Track A · Foundations · ~35 minutes**

This is the most important module in the course. Prompting is not about magic words. **It is about briefing well.** If you can brief a smart colleague, you can prompt Claude.

## The briefing mindset

Imagine handing a task to a sharp new hire who has never been to your office. What would they need to know to do it well on the first try? Usually:

1. **Context.** Who you are, what's going on, and why this matters.
2. **Task.** Exactly what you want done.
3. **Audience and goal.** Who it's for and what a good result achieves.
4. **Constraints.** Length, tone, format, things to avoid, deadlines.
5. **Examples or materials.** Samples of what good looks like, or the source documents.

You don't need all five every time. A quick question needs none. But the more a task matters, the more of these you should include.

## Before and after

**Weak prompt**

> Write a reply to a guest complaint.

**Strong prompt**

> I manage guest relations for a 40-room boutique hotel in Goa. A guest emailed (pasted below) complaining that their sea-view room had construction noise from 8am and the front desk was dismissive when they raised it.
>
> Write a reply that:
> - apologises sincerely without making excuses,
> - acknowledges both the noise and the poor response from our team,
> - offers a complimentary night on a future stay or a 30% refund for the affected nights (their choice),
> - is under 150 words, warm but professional, and signed "Priya, Guest Relations".
>
> Don't promise the construction will stop; we don't control it.
>
> Guest email:
> """
> [paste]
> """

The second prompt takes 60 seconds more to write and saves three rounds of edits.

## Ten techniques that work

### 1. Be specific about the output
"Summarise this" gives a random summary. "Summarise this in 5 bullets for a CEO who has 30 seconds, leading with the decision needed" gives a useful one.

### 2. Give examples
If you want a particular style, show it. Paste two past emails you liked and say "match this tone". Examples beat adjectives.

### 3. Explain *why*
"Keep it short **because** it'll be read on a phone in the lobby" works better than "keep it short". When Claude knows the reason, it makes better judgment calls on everything you didn't specify.

### 4. Separate instructions from material
When you paste documents, put them inside clear markers such as triple quotes or tags like `<email>...</email>`. This stops Claude confusing your instructions with the content.

### 5. Ask for options
"Give me 5 subject lines, from safe to bold" beats asking for one and hoping. Then pick and refine.

### 6. Let Claude ask questions first
For anything substantial, end with:
> Before you start, ask me any questions you need answered to do this well.

This is the single best habit for complex tasks.

### 7. Assign a perspective
"Review this pitch as a sceptical hotel owner who has been burned by tech vendors before" gives a sharper critique than "review this pitch".

### 8. Break big tasks into steps
Don't ask for a whole business plan in one message. Ask for an outline, agree on it, then do each section. You keep control and the quality stays high.

### 9. Tell it what to do, not only what to avoid
"Write in plain, conversational English" works better than "don't be formal". Positive instructions are clearer.

### 10. Iterate in the conversation
The first answer is a draft. Reply with specific feedback:
- "Good. Cut the second paragraph, and make the ending a clear ask."
- "Too salesy. Rewrite as if you're a helpful colleague, not a vendor."
- "Keep the structure, but change the examples to be about resorts, not city hotels."

## Formats you can ask for

Claude can give you almost any shape of output. Ask explicitly:

- bullet points, numbered steps, or a table
- a checklist
- an email, WhatsApp message, LinkedIn post, or memo
- a pros/cons comparison or a decision matrix with scores
- a script for a call or a difficult conversation
- a spreadsheet, document, or slide deck as a downloadable file (Module 4)
- a one-page summary followed by details

## A reusable template

Copy this into your notes and fill it in for any important task:

```
Context: [who I am, the situation, why this matters]
Task: [what I want you to do]
Audience: [who will read/use this]
Good looks like: [the goal, success criteria]
Constraints: [length, tone, format, must-include, must-avoid]
Materials: [paste or attach]
Before you start, ask me anything you need to know.
```

## Common mistakes

| Mistake | Fix |
|---|---|
| One-line prompts for important work | Add context and constraints |
| Starting a new chat after a bad answer | Give feedback in the same chat instead |
| Accepting the first answer | Ask for options or a critique: "What's weak about this?" |
| Asking for everything at once | Break it into steps |
| Pasting sensitive data without thinking | See Module 5 |
| Treating facts as verified | Check names, numbers, and claims |

## Try it

1. **Rewrite a weak prompt.** Take this: *"Make a social post about our monsoon offer."* Rewrite it using the template, then compare outputs.
2. **Use the question trick.** Ask Claude to help you plan something real, such as a team offsite or a family trip, and end with "ask me any questions first".
3. **Practice steering.** Get a draft of anything, then give three rounds of specific feedback. Notice how quickly it converges.
4. **Get a critique.** Paste something you wrote recently and ask: *"Critique this as [specific reader]. Be direct. What's unclear, weak, or missing?"*

## Key takeaways

- Prompting is briefing. Context, task, audience, constraints, examples.
- Explain *why*, show examples, and let Claude ask questions.
- The first answer is a draft. Steer it with specific feedback.
- Keep a personal template for important tasks.
