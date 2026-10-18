# Module 13: Building with the Claude API (for builders)

**Track C · Advanced · ~30 minutes · Optional: for engineers and technical PMs**

Everything so far uses Claude's apps. The **Claude API** lets you build Claude into your own products and internal workflows. Examples include auto-tagging guest messages, summarising reviews every night, powering a support assistant, or extracting data from invoices.

## When to use the API vs. the apps

| Use the apps (or Cowork / Claude Code) when... | Use the API when... |
|---|---|
| A person is in the loop for each task | The task runs automatically, at volume |
| The task varies each time | The task is the same shape every time |
| You're exploring or prototyping | You're building it into a product or pipeline |

**Start simple.** Most useful API features are a single call with a good prompt. Reach for agents only when a task genuinely needs open-ended, multi-step work.

## Your first call (Python)

Get an API key from the Claude Console, set it as the `ANTHROPIC_API_KEY` environment variable, then:

```bash
pip install anthropic
```

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    system=(
        "You classify hotel guest messages. "
        "Reply with exactly one label: BOOKING, COMPLAINT, REQUEST, or OTHER."
    ),
    messages=[
        {"role": "user", "content": "The AC in room 304 has been broken since we arrived."}
    ],
)

# The response can contain several content blocks; print the text ones.
print("".join(block.text for block in response.content if block.type == "text"))
```

Key ideas in that snippet:

- **`model`**: which Claude model to use.
- **`system`**: standing instructions, like project instructions in the app.
- **`messages`**: the conversation so far, alternating `user` and `assistant`.
- **`max_tokens`**: the upper limit on the length of the reply.

The official SDKs also cover TypeScript, Java, Go, Ruby, C#, and PHP.

## Choosing a model

As of this writing, the current models include:

| Model | ID | Use for |
|---|---|---|
| Claude Opus 5.5 | `claude-opus-5-5` | Strong default for complex reasoning, coding, and agents |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | Fast and capable everyday work at a lower price |
| Claude Haiku 5.5 | `claude-haiku-5-5` | High-volume, latency-sensitive, simple tasks |
| Claude Fable 5.1 | `claude-fable-5-1` | Anthropic's most capable widely released model, for the hardest long-horizon work |

Model IDs and prices change. Check the [models overview](https://docs.claude.com/en/docs/about-claude/models/overview) before you build. The practical approach: get it working with a capable model, build a small test set (Module 10), then see whether a faster, cheaper model holds up on that set.

Current models also take an **effort** setting (`output_config={"effort": "low" | "medium" | "high" | ...}`) that trades thoroughness for speed and cost. Low effort suits simple classification; high effort suits hard reasoning and agentic work.

## Concepts worth knowing

**Tool use (function calling).** You describe functions your system offers, such as `check_availability(date, room_type)` or `create_ticket(...)`. Claude decides when to call them, and your code runs them and returns the results. This is how you connect Claude to your own systems. The SDKs include a **tool runner** that handles the call-execute-repeat loop for you.

**Structured outputs.** Ask for JSON that matches a schema you define, so the output plugs straight into your code.

**Prompt caching.** If many requests share a long, unchanging prefix (a big system prompt, a policy document, a product catalogue), caching it cuts cost and latency considerably. Put stable content first and the variable parts last.

**Message Batches.** For large jobs that don't need an instant answer (like tagging 50,000 historical reviews), the Batches API processes requests asynchronously at a discount.

**Files, PDFs, and citations.** Send PDFs and documents directly and ask Claude to cite the exact passages it used.

**Server tools.** Anthropic-hosted tools like **web search**, **web fetch**, and **code execution** run on Anthropic's side, with no extra infrastructure for you.

**MCP.** The same Model Context Protocol behind connectors (Module 11) lets your API apps use MCP servers, and lets you expose your own systems to Claude.

**Skills.** The same Skills from Module 11 work through the API, for example to have Claude produce polished Excel or PowerPoint files.

## Building agents

There are several ways to build an agent, from most control to least code:

1. **Your own loop with tool use.** You call the API, run the tools Claude asks for, and repeat. Full control.
2. **The SDK tool runner.** You write the tool functions and the SDK runs the loop.
3. **Claude Agent SDK.** The same harness that powers Claude Code, as a library, with built-in file, shell, and web tools, subagents, and permissions. You host it.
4. **Claude Managed Agents.** Anthropic runs the agent loop *and* hosts a sandboxed workspace for each session. Good for long-running, scheduled, or stateful agents without managing infrastructure.

Before building an agent, ask: Is the task genuinely multi-step and hard to specify in advance? Is the outcome worth the extra cost and time? Can mistakes be caught and undone? If not, a single call or a fixed workflow is better.

## Production checklist

- **Evaluate:** keep a test set of real inputs (including edge cases) and check outputs every time you change a prompt or model.
- **Handle errors:** retries for rate limits and server errors (the SDK retries some of these automatically), and fallbacks when needed.
- **Check the stop reason:** responses report why they ended (finished, hit `max_tokens`, requested a tool, or declined). Handle each case.
- **Protect data:** send only what's needed, and follow your company's data policies.
- **Guard against prompt injection:** treat user-supplied and web content as untrusted, especially when Claude can take actions.
- **Monitor cost:** log token usage, use caching and batches, and right-size the model and effort.
- **Keep humans in the loop** for consequential actions.

## Resources

- Claude Docs: [docs.claude.com](https://docs.claude.com)
- The Claude Console (API keys, usage, and a prompt workbench)
- Anthropic's courses and cookbooks on GitHub ([github.com/anthropics](https://github.com/anthropics))
- In Claude Code, ask Claude itself: it knows the API well and can scaffold a working project for you.

## Try it

1. Make your first API call with the snippet above.
2. Turn a prompt you use repeatedly in the app into an API script that processes a CSV of inputs.
3. Add a tool: define a fake `check_availability` function and let Claude call it to answer "Do you have a deluxe room on the 14th?"

## Key takeaways

- Use the API when tasks run automatically, at volume, or inside your product.
- Start with a single well-prompted call. Add tools, then agents, only when needed.
- Caching, batches, and the right model and effort keep costs down.
- Evaluate with real examples before and after every change.
