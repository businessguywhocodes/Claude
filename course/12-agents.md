# Module 12: Agents: Claude Code, Cowork, and Claude in Chrome

**Track C · Advanced · ~30 minutes**

In a chat, Claude answers and you act. As an **agent**, Claude takes a goal, plans the steps, uses tools (files, a terminal, a browser, your apps), checks its own work, and keeps going until the job is done. You move from *asking* to *delegating*.

## The mental model: a capable assistant with hands

An agent works in a loop:

1. **Understand** the goal
2. **Plan** the steps
3. **Act** with a tool (read a file, run a command, click a button, search)
4. **Observe** the result
5. **Repeat** until done, then **report** back

Good delegation to an agent looks like good delegation to a person: a clear goal, the context it needs, what "done" means, and what it must not touch.

## Claude Code: agents for software

**Claude Code** is Claude working directly in a codebase. It runs in your terminal, in IDEs like VS Code and JetBrains, in the desktop app, and on the web, where it runs in a cloud environment. It can:

- read and understand an entire repository
- write and edit code across many files
- run tests, fix failures, and iterate
- use git, open pull requests, and respond to review comments
- connect to other tools through MCP (issue trackers, databases, docs)

**For the engineers:** start with a well-scoped task ("add input validation to the booking form and tests for it"). Add a `CLAUDE.md` file to your repo describing how to build, test, and the conventions to follow, and review the diff like you would a colleague's.

**For non-engineers:** Claude Code isn't only for developers. People use it to build internal tools, scripts that clean up spreadsheets, small websites, and data analyses, describing what they want in plain English. With the web version you can start a task from your browser or phone and come back to a finished result.

## Cowork: agents for knowledge work

**Cowork** brings the same agentic approach to everyday knowledge work in the Claude desktop app. You give Claude access to a folder and your connected apps, describe the outcome, and it works through the steps, such as:

- *"Go through the 40 vendor invoices in this folder, extract the amounts and due dates into a spreadsheet, and flag duplicates."*
- *"Read last month's guest feedback files and draft a summary deck with the top themes and recommended fixes."*
- *"Organise my Downloads folder into sensible subfolders and rename files consistently."*
- *"Using my calendar and inbox, prepare a briefing doc for each of tomorrow's meetings."*

Cowork can also run tasks on a schedule, such as a morning briefing every weekday, and use plugins that bundle skills and connectors for particular roles like marketing, operations, or sales.

## Claude in Chrome: agents for the web

**Claude in Chrome** is a browser extension that lets Claude see and act on web pages: navigate, click, fill forms, and pull information across tabs. Use it for:

- comparing options across several websites (hotels, flights, software vendors)
- filling repetitive web forms from a spreadsheet
- pulling data from a web dashboard that has no export button
- testing your own website's booking flow end to end

It asks for permission before acting on sites, and you can watch what it's doing.

## Delegating well

Use this checklist when handing a task to any agent:

- **Goal:** what outcome do you want?
- **Context:** where are the files or tools, and what background matters?
- **Definition of done:** how will you, and the agent, know it's finished and correct?
- **Boundaries:** what must it *not* do? (Don't send emails, don't delete files, don't spend money, ask before X.)
- **Checkpoints:** when should it stop and check with you?

Example:
> Goal: build a competitor rate comparison for our 3 Goa properties for the next 4 weekends.
> Context: competitors are listed in `competitors.xlsx`. Use public booking sites.
> Done: a spreadsheet with one row per property × competitor × date, the lowest available double-room rate, and the source link.
> Boundaries: read-only. Don't log in anywhere or start any booking.
> Checkpoint: show me the first property's results before doing the rest.

## Safety with agents

Agents are powerful because they act, so mistakes act too.

- **Start supervised.** Approve actions step by step until you trust a workflow, then loosen up.
- **Limit access.** Give the agent only the folders, accounts, and permissions the task needs.
- **Keep backups and use version control.** For files and code, make sure you can undo.
- **Watch for prompt injection.** Web pages, emails, and documents can contain hidden instructions. Be especially careful when an agent reads untrusted content *and* can take actions like sending or paying.
- **Review the output.** "Done" from an agent means "ready for your review", not "ready to ship".
- **Keep sensitive actions human.** Payments, sending to customers, deleting data, and changing permissions should need your explicit approval.

## Try it

1. **Cowork (or Claude Code) on a folder.** Pick a messy folder of files you own and ask Claude to organise it and produce an index, with a checkpoint before it moves anything.
2. **Multi-step research task.** Delegate a task that needs several steps, such as gathering prices from 5 vendor websites into a table, using the delegation checklist.
3. **For engineers.** Run Claude Code on a real but small ticket. Write a `CLAUDE.md` for the repo first.

## Key takeaways

- Agents plan, act with tools, check their work, and keep going until the goal is met.
- Claude Code handles software, Cowork handles knowledge work, and Claude in Chrome handles the web.
- Delegate like a manager: goal, context, definition of done, boundaries, checkpoints.
- Start supervised, limit access, and keep a human on sensitive actions.
