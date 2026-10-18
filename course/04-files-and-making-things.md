# Module 4: Files, Images, and Making Things

**Track A · Foundations · ~25 minutes**

Claude can read what you give it and make things you can use, not just text in a chat window.

## Giving Claude things to read

You can attach:

- **Documents**: PDFs, Word files, text, contracts, reports, menus, policies
- **Spreadsheets and data**: CSV and Excel files
- **Images**: screenshots, photos of receipts or whiteboards, charts, product photos
- **Content from connected apps**: files from Google Drive and similar tools

### What to do with documents

- **Summarise:** "Summarise this 40-page vendor contract. List the termination terms, auto-renewal clauses, liability caps, and anything unusual. Quote the exact clause numbers."
- **Compare:** "Here are three hotel PMS proposals. Compare them in a table: price, contract length, integrations, support terms, and red flags."
- **Extract:** "Pull every date and deadline from this document into a table."
- **Question:** "Based only on this policy document, can a guest get a refund if they cancel 24 hours before check-in?"

> **Tip:** Ask Claude to **quote** the parts of the document it relied on. This makes checking its work fast and reduces made-up details.

### What to do with images

- Screenshot an error message: "What does this mean and how do I fix it?"
- Photograph a whiteboard after a meeting: "Turn this into structured notes with action items."
- Upload a competitor's landing page: "What's this page doing well? What would you change?"
- Photograph a printed bill: "Put these line items in a table and check the total."

### What to do with data

Claude can run analysis on spreadsheets and CSVs, including calculations and charts. For example:

> Here's our booking export for last quarter (CSV). Show me:
> 1. bookings and revenue by month,
> 2. average length of stay by channel,
> 3. cancellation rate by lead time bucket (0–7, 8–30, 31+ days),
> and a chart for each. Then tell me the three most interesting patterns.

Always sanity-check numbers against something you know, such as last month's total. If a figure looks off, ask Claude to show how it calculated it.

## Making things

### Artifacts

When Claude creates something substantial, such as a document, a piece of code, a diagram, or a small interactive app, it can appear as an **Artifact** in a panel next to the chat. You can keep editing it through conversation, copy it, download it, and publish it to share with others.

Things people build with Artifacts:

- a **checklist app** for a housekeeping inspection
- an **ROI calculator** for a sales conversation
- a **trip itinerary** page to share with family
- a **training quiz** for new front-desk staff
- a **flowchart** of a guest complaint escalation process
- a simple **dashboard** from a spreadsheet you uploaded

Want to see what real people have built? Browse the **[Showcase](showcase.md)** of public artifacts.

You don't need to know how to code. Describe what you want, try it, then ask for changes: *"Add a button to reset the form"*, *"Make it work on mobile"*, *"Use our brand colours: navy and coral."*

### Real files

Claude can also create proper files you download and open in other apps:

- **Word documents** (proposals, SOPs, letters)
- **Excel spreadsheets** with working formulas (budgets, trackers, models)
- **PowerPoint decks** (pitches, training, monthly reviews)
- **PDFs**

Example:

> Create an Excel budget for a 3-day team offsite for 25 people in Udaipur. Tabs for travel, stay, food, activities, and a summary tab with totals and per-person cost. Use formulas so I can change headcount and everything updates.

## Try it

1. **Document Q&A.** Upload a long PDF you've been meaning to read, like a policy, report, or contract. Ask for a 5-bullet summary, then three specific questions. Ask it to quote its sources in the document.
2. **Image to structure.** Photograph a page of handwritten notes or a whiteboard and turn it into a clean action list.
3. **Build a mini-app.** Ask: *"Build me an interactive checklist for a hotel room inspection, with sections for bathroom, bed, minibar, and amenities, a pass/fail toggle for each item, and a score at the bottom."* Then ask for two improvements.
4. **Make a real file.** Ask for a spreadsheet you'd actually use, such as a monthly personal budget or a trip cost splitter.

## Key takeaways

- Upload the real material instead of describing it. Claude reads documents, images, and data.
- Ask Claude to quote or show its working so you can verify quickly.
- Artifacts turn ideas into usable tools and documents in minutes, without code.
- Claude can produce real Word, Excel, PowerPoint, and PDF files.
