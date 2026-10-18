# Module 10: Advanced Prompting

**Track C · Advanced · ~30 minutes**

Module 3 covered the basics of briefing. These techniques help with complex, long, or high-stakes work, and they are the foundation for building workflows and agents.

## 1. Structure long prompts with tags

When a prompt has several parts (instructions, documents, examples), label them with XML-style tags. Claude is trained to pay attention to this structure.

```
<context>
We're a hotel-tech startup preparing for a partner summit.
</context>

<documents>
  <document name="last_year_feedback.csv">...</document>
  <document name="agenda_draft.md">...</document>
</documents>

<task>
Propose 3 changes to the agenda based on last year's feedback.
</task>

<output_format>
For each change: the change, the feedback that supports it (quote), and the expected impact.
</output_format>
```

You can also ask Claude to put parts of its output in tags, which makes it easy to pull out pieces later:
> Put your reasoning in `<analysis>` tags and your final recommendation in `<recommendation>` tags.

## 2. Put long documents first, the question last

With very long inputs (several reports or a big contract), paste the documents at the **top** and put your instructions and question at the **end**. This tends to produce better answers on long material.

For better accuracy, ask Claude to **extract relevant quotes first**, then answer based on those quotes:
> First, find the quotes from the contract that are relevant to termination and put them in `<quotes>` tags. Then answer my question using only those quotes.

## 3. Ask for reasoning before the answer

For analysis and decisions, ask Claude to think through the problem before concluding:
> Think through this step by step: list the factors, weigh them, consider what could go wrong, and then give your recommendation.

Or turn on **extended thinking**, which does this automatically. Don't over-specify *how* it should think. A high-level instruction to think carefully often works better than a rigid script.

## 4. Few-shot examples

Show 2–5 examples of input → output, and Claude will follow the pattern closely. This is powerful for classification and consistent formatting.

```
Classify each guest message as BOOKING, COMPLAINT, REQUEST, or OTHER.

Message: "Can I get an extra pillow in 304?" → REQUEST
Message: "The AC has been broken since we arrived." → COMPLAINT
Message: "Do you have rooms on the 14th for 2 nights?" → BOOKING

Now classify:
[messages]
```

Make examples varied so Claude learns the underlying pattern, not one surface detail.

## 5. Prompt chaining

Split a big job into a pipeline where each step's output feeds the next. For example, a competitor analysis:

1. **Research** → "Gather facts on these 5 competitors." (web search)
2. **Structure** → "Put the facts into this comparison table."
3. **Analyse** → "Identify gaps and opportunities for us."
4. **Write** → "Draft a 1-page memo for leadership."
5. **Review** → "Critique the memo as a sceptical CFO, then revise."

Each step is easier to check and fix than one giant prompt.

## 6. Self-critique and revision

Ask Claude to grade its own work against explicit criteria:
> Here are the criteria: clear ask in the first line, under 120 words, no jargon, mentions the customer's specific situation. Score your draft against each one, then rewrite to fix any misses.

## 7. Write a prompt with Claude

When you need a reusable prompt (for a Project, a Skill, or the API), ask Claude to help write it:
> I want a reusable prompt that turns raw guest reviews into a weekly summary for hotel GMs. Interview me about what the GMs need, then write the prompt. Include an example output.

Then test it on 5–10 real inputs and refine. **Prompting is iterative engineering**: write, test, look at failures, adjust.

## 8. Be explicit about effort and scope

Modern Claude models follow instructions precisely. If you want more, ask for it:
- "Be thorough. Cover edge cases, not just the happy path."
- "Go beyond the basics. Include advanced options."

If you want less:
- "Just the answer, no explanation."
- "Only change what I asked for; leave everything else as is."

## 9. Control format positively

To get prose instead of bullets, say "write in flowing paragraphs" rather than "don't use bullet points". Matching your own prompt's style to the output you want also helps: a prompt written in paragraphs tends to produce paragraphs.

## 10. Build a test set for anything you reuse

If a prompt will run many times (on every guest review, every lead, every invoice), collect 10–20 real examples, including tricky ones. Check the outputs whenever you change the prompt. This simple habit is what separates a reliable workflow from a demo.

## Try it

1. **Tags.** Rewrite a complex prompt you've used, with `<context>`, `<documents>`, `<task>`, and `<output_format>` tags. Compare results.
2. **Quotes first.** Take a long document and use the "extract quotes, then answer" pattern.
3. **Chain.** Run a 4-step chain on a real topic: research → structure → analyse → write.
4. **Meta-prompt.** Have Claude interview you and write a reusable prompt for a task you do weekly. Test it on 5 real inputs.

## Key takeaways

- Use tags to structure complex prompts, with documents first and questions last.
- Ask for reasoning (or use extended thinking) on hard problems.
- Few-shot examples and prompt chains give consistency and control.
- For reusable prompts, test on real examples and iterate.
