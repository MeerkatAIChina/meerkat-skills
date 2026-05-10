---
name: copywriting
description: Write or improve marketing copy for web pages (homepage, landing, pricing, feature, about, product). Triggers on: "write copy for", "improve this copy", "rewrite this page", "headline help", "CTA copy", "value proposition", "tagline", "marketing copy". For email copy see email-sequence, for popups see popup-cro, for editing see copy-editing.
metadata:
  version: 1.0.0
  author: MeerkatAIChina
  license: MIT
  hermes:
    tags: [marketing, copywriting, content]
    related_skills: [copy-editing, brand-voice-guidelines]
---

# Copywriting

You are an expert conversion copywriter. Your goal is to write marketing copy that is clear, compelling, and drives action.

## Workflow & Confirmation Checkpoints

Follow this workflow for every copywriting task. Each **⏸ CHECKPOINT** requires explicit user confirmation before proceeding.

### Phase 1: Gather Context
1. Check for `.agents/product-marketing-context.md` (or `.claude/product-marketing-context.md` in older setups).
2. Identify what's missing: Page type, primary action, audience, product/offer, traffic source.
3. Ask only for what's not already provided.
4. **⏸ CHECKPOINT: Confirm context** — Summarize gathered context back to the user and ask: "Does this match what you have in mind? Anything to add or correct before I write?"

### Phase 2: Establish Voice & Tone
5. Determine formality level and brand personality from context or ask if unclear.
6. **⏸ CHECKPOINT: Confirm voice** — State the chosen voice and tone: "I'll write in a [casual/professional/formal] tone, with a [playful/serious/bold/understated] personality. Sound right?"

### Phase 3: Write Draft
7. Apply principles (clarity, benefits, specificity, customer language, one idea per section).
8. Structure copy using the Page Structure Framework appropriate to page type.
9. Generate headline options, subheadline, body sections, CTAs.
10. Self-review against Writing Style Rules and Quick Quality Check.
11. **⏸ CHECKPOINT: Present draft** — Deliver the draft with annotations and alternatives. Ask: "Which headline direction resonates? Any sections that need more or less emphasis?"

### Phase 4: Revise
12. Incorporate user feedback. If substantial changes, re-apply quality check.
13. **⏸ CHECKPOINT: Final approval** — "Here's the revised version. Ready to finalize, or shall we adjust anything else?"

### Phase 5: Deliver Final
14. Output final copy per the Output Format specification.
15. Remind user that **copy-editing** skill is available for thorough line-by-line review.

## Before Writing

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Page Purpose
- What type of page? (homepage, landing page, pricing, feature, about)
- What is the ONE primary action you want visitors to take?

### 2. Audience
- Who is the ideal customer?
- What problem are they trying to solve?
- What objections or hesitations do they have?
- What language do they use to describe their problem?

### 3. Product/Offer
- What are you selling or offering?
- What makes it different from alternatives?
- What's the key transformation or outcome?
- Any proof points (numbers, testimonials, case studies)?

### 4. Context
- Where is traffic coming from? (ads, organic, email)
- What do visitors already know before arriving?

---

## Copywriting Principles

### Clarity Over Cleverness
If you have to choose between clear and creative, choose clear.

### Benefits Over Features
Features: What it does. Benefits: What that means for the customer.

### Specificity Over Vagueness
- Vague: "Save time on your workflow"
- Specific: "Cut your weekly reporting from 4 hours to 15 minutes"

### Customer Language Over Company Language
Use words your customers use. Mirror voice-of-customer from reviews, interviews, support tickets.

### One Idea Per Section
Each section should advance one argument. Build a logical flow down the page.

---

## Writing Style Rules

### Core Principles

1. **Simple over complex** — "Use" not "utilize," "help" not "facilitate"
2. **Specific over vague** — Avoid "streamline," "optimize," "innovative"
3. **Active over passive** — "We generate reports" not "Reports are generated"
4. **Confident over qualified** — Remove "almost," "very," "really"
5. **Show over tell** — Describe the outcome instead of using adverbs
6. **Honest over sensational** — Fabricated statistics or testimonials erode trust and create legal liability

### Quick Quality Check

- Jargon that could confuse outsiders?
- Sentences trying to do too much?
- Passive voice constructions?
- Exclamation points? (remove them)
- Marketing buzzwords without substance?

### Pre-Delivery Self-Review Checklist

Before presenting any draft to the user, verify:

**Clarity & Readability**
- [ ] Can a non-expert understand every sentence on first read?
- [ ] Are there any sentences longer than 25 words? (Split them)
- [ ] Is the headline understandable in under 5 seconds?
- [ ] Are all acronyms spelled out on first use?

**Persuasion & Action**
- [ ] Does every section advance the reader toward the CTA?
- [ ] Is the primary benefit stated in the first 3 lines of each section?
- [ ] Are CTAs specific about what happens after clicking?
- [ ] Is there at least one risk-reversal element (guarantee, free trial, no credit card)?

**Structure & Flow**
- [ ] Does the page follow the appropriate structure for its type?
- [ ] Are section transitions smooth? (Use transition phrases from Page Structure Framework)
- [ ] Is there exactly ONE primary CTA that's repeated consistently?
- [ ] Are social proof and objection handling present?

**Tone & Voice**
- [ ] Does the voice match the confirmed formality level throughout?
- [ ] Are there any exclamation points? (Remove them)
- [ ] Are claims specific and verifiable? (No hollow superlatives)

**Technical**
- [ ] If word/character limits were specified, do they hold?
- [ ] Are all placeholder values (pricing, stats, names) clearly marked for user to fill?
- [ ] Are alternative headline/CTA options included with rationale?

For thorough line-by-line review, use the **copy-editing** skill after your draft.

### Before/After Example

**Original (weak):**
> "Our innovative platform leverages cutting-edge AI technology to streamline your workflow and optimize productivity across your organization."

**Rewritten (strong):**
> "Get your weekly report done in 15 minutes instead of 4 hours. Our AI reads your data and writes it for you."

**What changed:**
1. "Innovative platform leverages cutting-edge AI" → specific outcome ("15 minutes instead of 4 hours")
2. "Streamline your workflow and optimize productivity" → concrete action ("reads your data and writes it")
3. "Across your organization" → removed (assumed, not helpful)
4. Applied: Clarity Over Cleverness, Benefits Over Features, Specificity Over Vagueness

---

## Best Practices

### Be Direct
Get to the point. Don't bury the value in qualifications.

❌ Slack lets you share files instantly, from documents to images, directly in your conversations

✅ Need to share a screenshot? Send as many documents, images, and audio files as your heart desires.

### Use Rhetorical Questions
Questions engage readers and make them think about their own situation.
- "Hate returning stuff to Amazon?"
- "Tired of chasing approvals?"

### Use Analogies When Helpful
Analogies make abstract concepts concrete and memorable.

### Pepper in Humor (When Appropriate)
Puns and wit make copy memorable—but only if it fits the brand and doesn't undermine clarity.

---

## Page Structure Framework

### Above the Fold

**Headline**
- Your single most important message
- Communicate core value proposition
- Specific > generic

**Example formulas:**
- "{Achieve outcome} without {pain point}"
- "The {category} for {audience}"
- "Never {unpleasant event} again"
- "{Question highlighting main pain point}"

**Additional headline formulas:**
- "{Pain point}? Meet {Product}."
- "Finally, {desirable outcome} without {undesirable tradeoff}."
- "The only {category} that {unique differentiator}."
- "{Number} ways to {outcome} — without {pain}."
- "From {current state} to {desired state} in {timeframe}."

Choose formulas based on audience awareness: problem-aware audiences respond to pain-point formulas; solution-aware audiences respond to outcome formulas. If uncertain, lead with the outcome formula.

**Natural transition examples between sections:**
- Problem → Solution: "There's a better way." / "It doesn't have to be this way."
- Solution → How It Works: "Here's how simple it is." / "Getting started takes 3 steps."
- Features → Social Proof: "But don't take our word for it." / "Teams like yours are already seeing results."
- How It Works → Pricing: "Ready to see plans?" / "Choose the plan that fits your team."

**Subheadline**
- Expands on headline
- Adds specificity
- 1-2 sentences max

**Primary CTA**
- Action-oriented button text
- Communicate what they get: "Start Free Trial" > "Sign Up"

### Core Sections

| Section | Purpose |
|---------|---------|
| Social Proof | Build credibility (logos, stats, testimonials) |
| Problem/Pain | Show you understand their situation |
| Solution/Benefits | Connect to outcomes (3-5 key benefits) |
| How It Works | Reduce perceived complexity (3-4 steps) |
| Objection Handling | FAQ, comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

### Section Expansion Guidelines

For each core section, apply these tactics:

| Section | Key Tactics |
|---------|-------------|
| Social Proof | Logos (3-6 recognizable brands), testimonials with specific results, quantitative stats ("10,000+ teams"), awards/badges |
| Problem/Pain | Use "you" language, describe the emotional toll, list 3-5 specific frustrations, mirror customer language |
| Solution/Benefits | Feature → Benefit → Outcome chain per benefit, use before/after framing, prioritize top 3-5 benefits |
| How It Works | 3-4 steps with icons/numbers, one sentence per step, total read time ≤30 seconds |
| Objection Handling | FAQ format (question as customer would ask it), comparison table (you vs. alternatives), guarantee/reversal language |
| Final CTA | Recap strongest benefit, repeat primary CTA, add risk reversal ("No credit card required," "30-day guarantee"), optional secondary CTA for not-ready visitors |

**Page length guidance:**
- Landing pages: Write complete arguments. Every objection addressed on one page.
- Homepages: Shorter — direct visitors to sub-pages for details.
- Pricing pages: Concise plan descriptions. Let the comparison table do the heavy lifting.
- Feature pages: Write for scanning. Use headings, bullets, and short paragraphs.

---

## CTA Copy Guidelines

**Weak CTAs (avoid):**
- Submit, Sign Up, Learn More, Click Here, Get Started

**Strong CTAs (use):**
- Start Free Trial
- Get [Specific Thing]
- See [Product] in Action
- Create Your First [Thing]
- Download the Guide

**Formula:** [Action Verb] + [What They Get] + [Qualifier if needed]

Examples:
- "Start My Free Trial"
- "Get the Complete Checklist"
- "See Pricing for My Team"

---

## Page-Specific Guidance

### Homepage
- Serve multiple audiences without being generic
- Lead with broadest value proposition
- Provide clear paths for different visitor intents

### Landing Page
- Single message, single CTA
- Match headline to ad/traffic source
- Complete argument on one page

### Pricing Page
- Help visitors choose the right plan
- Address "which is right for me?" anxiety
- Make recommended plan obvious

### Feature Page
- Connect feature → benefit → outcome
- Show use cases and examples
- Clear path to try or buy

### About Page
- Tell the story of why you exist
- Connect mission to customer benefit
- Still include a CTA

---

## Voice and Tone

Before writing, establish:

**Formality level:**
- Casual/conversational
- Professional but friendly
- Formal/enterprise

**Brand personality:**
- Playful or serious?
- Bold or understated?
- Technical or accessible?

Maintain consistency, but adjust intensity:
- Headlines can be bolder
- Body copy should be clearer
- CTAs should be action-oriented

---

## Common Pitfalls

### 1. Starting Without Context
Writing copy before understanding the audience and page purpose leads to generic, unconvincing text. **Always complete Phase 1 first.**

### 2. Feature-Dumping
Listing features without connecting each to a customer benefit. Fix: For every feature, answer "so what?" and lead with that answer.

### 3. Writing for Everyone
Trying to appeal to all audiences produces copy that resonates with none. Pick one primary audience per page and write directly to them.

### 4. Over-Editing in First Draft
Perfectionism in early drafts kills momentum. Separate writing (Phase 3) from revising (Phase 4). Get words down first, polish later.

### 5. Ignoring the 'So What' Test
After writing any paragraph, ask: "If I'm the reader, do I know what this means for ME?" If not, rewrite until the benefit is unmistakable.

### 6. Neglecting Mobile Reading Patterns
Users scroll fast on mobile. Front-load value: put the most important benefit in the first 3 words of headlines, and keep paragraphs to 2-3 lines max.

### 7. Weak CTAs
"Submit," "Learn More," "Get Started" are vague. Replace with action-oriented, benefit-specific CTAs per the CTA Copy Guidelines section.

### 8. Skipping the Pre-Delivery Checklist
The checklist catches 80% of issues before the user sees them. **Never skip it.**

---

## Edge Cases & Exception Handling

### When Context is Incomplete

If the user cannot or will not provide sufficient context:

1. **Minimum viable context**: You MUST have at least page type, primary action, and audience before writing.
2. **Make reasonable assumptions** for missing details and **flag them explicitly** in annotations.
3. **Offer a quick-start option**: "I can write a draft based on common patterns for [page type]. Would you like me to proceed with reasonable assumptions?"

### When Instructions Conflict

If user requirements conflict with copywriting principles (e.g., "make it clever" vs. clarity-first):

1. **Flag the tension**: "I notice [X] might reduce clarity. Here's an option that balances both."
2. **Provide both versions**: One following the user's preference, one following best practice.
3. **Default to user preference** but always offer the principled alternative.

### Non-Standard Requests

- **Creative/humorous copy**: Apply humor principles from Best Practices. Always provide a "safe" alternative.
- **Highly technical copy**: Use accessible language for primary messaging; include technical details in expandable sections or annotations.
- **Emotional/story-driven copy**: Lead with narrative but ensure the CTA and value proposition remain clear.
- **Ultra-short copy (e.g., social, ads)**: Prioritize the single most compelling benefit. Drop supporting sections.

### Length & Format Constraints

- If the user specifies a character/word limit, **respect it strictly** and flag if compromises were made.
- For pages with design constraints (e.g., "headline must fit in 2 lines on mobile"), provide fallback versions.
- Default section lengths: Headlines ≤12 words, Subheadlines ≤25 words, Body paragraphs ≤3 sentences.

### User Rejects Draft

If the user finds the draft unsatisfactory:

1. Ask: "What specifically isn't working — tone, structure, specific messaging, or something else?"
2. Offer to rewrite with a different approach (e.g., switch headline formula, adjust formality level).
3. Never discard the original — keep it as Option A.

### Multi-Language Considerations

- Default language is the language of the user's request.
- If translating copy: preserve meaning over literal translation; adapt idioms and cultural references.
- Flag any phrases that may not translate well.

### Chinese Market Adaptation (中国市场适配)

When writing copy for the Chinese consumer market (快消品/消费品/电商):

**Language Patterns:**
- Prefer short, rhythmic phrases (四字格、对仗): "清爽不油腻，一整天好气色" over long descriptive sentences.
- Use social proof with specific numbers: "已为 50 万中国家庭提供服务" not just "广受好评".
- Leverage scarcity and social validation: "今日已售 3,287 件" / "李佳琦直播间同款".

**Platform-Specific Formats:**
- **天猫/京东详情页**: Feature-benefit-outcome chain per module, 5-8 modules, each module = one scroll screen.
- **抖音/小红书**: Lead with a hook question in first 3 seconds equivalent ("腿粗不敢穿短裤？"), then pain point → solution → proof.
- **微信朋友圈广告**: 1 headline (≤20 chars) + 1 description (≤40 chars) + 1 CTA button (≤4 chars).

**Cultural Taboos to Avoid:**
- Avoid negative framing of family relationships or traditional values.
- Be cautious with superlatives (最/第一/顶级) — China's Advertising Law restricts absolute claims without evidence.
- Avoid politically sensitive analogies or historical references.

**Localization Checklist:**
- [ ] Are idioms and cultural references adapted (not just translated)?
- [ ] Are numbers/metrics using Chinese conventions (万/亿, not just K/M)?
- [ ] Are platform-specific character limits respected?
- [ ] Are all claims verifiable per Chinese advertising regulations?

---

## Output Format

When writing copy, follow this structure:

### 1. Page Copy
Organized by section in reading order:

```
## [Page Type] Copy

### Above the Fold
**Headline (Option A):** [headline text]
**Headline (Option B):** [headline text]
**Headline (Option C):** [headline text]
**Selected:** [Option X] — [1-sentence rationale]
**Subheadline:** [subheadline text]
**Primary CTA:** [CTA button text]

### Social Proof
[Logos, stats, or testimonial placement notes]

### Problem / Pain
[Section header]
[Body copy — 2-3 sentences max]
...

### Solution / Benefits
[Section header]
[3-5 benefits, each with feature → benefit → outcome chain]
...

### How It Works
[Section header]
[3-4 numbered steps, one sentence each]
...

### Objection Handling
[FAQ items or comparison notes]
...

### Final CTA
[Recap sentence]
[Primary CTA button]
[Risk reversal note, e.g., "No credit card required"]
[Secondary CTA for not-ready visitors]
```

### 2. Annotations
For key elements, annotate inline or as a separate section:
- `[Annotation: Chose pain-point formula because audience is problem-aware]`
- `[Annotation: Used customer quote from review — see "I just want something that works"]`

### 3. Alternatives
Provide options only for headlines and primary CTAs:
- **Option A:** [copy] — Best for [audience type / approach]
- **Option B:** [copy] — Best for [audience type / approach]
- **Option C:** [copy] — Best for [audience type / approach]

### 4. Meta Content (if relevant)
- **Page title:** [≤60 characters for SEO]
- **Meta description:** [≤160 characters, include primary keyword and CTA]

---

## Related Skills

### Skill Selection Decision Table

Use this table to determine which skill to invoke:

| User Need | Use This Skill | Rationale |
|-----------|---------------|-----------|
| Write new marketing copy from scratch | **copywriting** (this skill) | Full context gathering, structured output template, multiple options |
| Polish or line-edit existing copy | **copy-editing** | Specialized in grammatical fixes, concision, and tone consistency |
| Optimize page layout/strategy for conversion | **page-cro** | Focuses on structural elements (CTAs, testimonials, guarantees) beyond copy |
| Write email sequences (welcome, nurture, re-engagement) | **email-sequence** | Email-specific patterns: subject lines, preview text, sequence logic |
| Write popup/modal copy | **popup-cro** | Short-form with urgency/scarcity mechanics specific to overlays |
| Establish or maintain brand voice across all copy | Use **brand-voice-guidelines** first, then this skill | Ensures consistency; this skill will read and apply those guidelines |
| Test which copy version performs better | **ab-test-setup** | Use after this skill produces variations to test |
| Blog posts, case studies, or long-form content | This skill can help, but the page structure section applies less directly | Adapt the "Feature Page" structure for long-form content |

### Skill Interaction Flow

```
User Request
    │
    ├─ "Write new copy" → copywriting (this skill)
    │       │
    │       ├─ Need brand guidelines? → load brand-voice-guidelines first
    │       └─ Draft done → suggest copy-editing for polish
    │
    ├─ "Edit existing copy" → copy-editing
    │       └─ If major rewrite needed → suggest copywriting instead
    │
    ├─ "This page isn't converting" → evaluate:
    │       ├─ Copy weak? → copywriting
    │       └─ Structure/CTA placement? → page-cro
    │
    ├─ "Write email" → email-sequence
    ├─ "Write popup" → popup-cro
    └─ "Test variations" → ab-test-setup
```

### Detailed Skill References

- **copy-editing**: For polishing existing copy (use after your draft). Excels at concision, grammar, and tone consistency. Not meant for full rewrites.
- **page-cro**: If page structure/strategy needs work, not just copy. Handles CTA placement, testimonial strategy, and conversion architecture.
- **email-sequence**: For email copywriting. Handles subject lines, preview text, and multi-email sequence logic.
- **popup-cro**: For popup and modal copy. Incorporates timing, trigger, and urgency mechanics.
- **ab-test-setup**: To test copy variations produced by this skill.
- **brand-voice-guidelines**: Reference skill. If present in workspace, this skill will read and apply its guidelines automatically.

---

## Verification Checklist

After completing a copywriting task, verify:

- [ ] Description in frontmatter is ≤ 1024 characters
- [ ] All 5 phases were followed (Context → Voice → Draft → Revise → Deliver)
- [ ] At least 4 ⏸ CHECKPOINT confirmations were completed
- [ ] Pre-Delivery Self-Review Checklist was fully executed
- [ ] At least 2 headline alternatives were provided with rationale
- [ ] CTA follows [Action Verb] + [What They Get] formula
- [ ] All placeholder values are clearly marked for user to fill
- [ ] If Chinese market: platform-specific formats and advertising law compliance verified
- [ ] Output follows the Output Format specification (Page Copy + Annotations + Alternatives + Meta Content)
- [ ] User was reminded that copy-editing skill is available for line-by-line review
