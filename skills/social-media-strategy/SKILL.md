---
name: social-media-strategy
description: Platform-specific organic social media strategy, content calendars, engagement tactics, community building, and performance measurement. Use when the user asks about social media strategy, organic social, content calendars, community management, or social media metrics.
version: 1.0.0
author: MeerkatAIChina
license: MIT
metadata:
  hermes:
    tags: [marketing, social-media, strategy]
    related_skills: []
  category: content
  domain: social-media
  updated: 2026-03-18
  tested: 2026-03-18
  tested_with: "Claude Code v2.1"
---

# Social Media Strategy

Platform-specific organic social strategy, calendars, and community building.

## Install

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git && cp -r claude-marketing/skills/social-media-strategy ~/.claude/skills/
```

## Workflow

Follow these steps when the user requests social media strategy assistance. Each step includes a **Checkpoint** where you must confirm with the user before proceeding.

### Step 1: Gather Requirements

Ask the user to provide the following. If they cannot provide all details, use the defaults listed and explicitly state your assumptions:

| Required Info | Default if Missing |
|---------------|-------------------|
| **Platform(s)** of interest | LinkedIn + Instagram (B2B), Instagram + TikTok (B2C), LinkedIn + Twitter/X (tech/SaaS) |
| **Goal** | Brand awareness (default for new accounts), engagement (default for existing accounts) |
| **Industry/niche** | General business — note this limits specificity |
| **Current posting frequency** | Assume starting from scratch (0 posts/week) |
| **Team capacity** (hours/week) | 3 hours/week (solopreneur default) |
| **Budget** (organic-only or paid) | Organic-only unless stated otherwise |

**Error handling**: If the user provides fewer than 2 data points, default to LinkedIn-only strategy for B2B contexts and Instagram-only for B2C. State: *"I'm making the following assumptions based on limited input. Please correct any that are wrong before I proceed."*

> **🛑 Checkpoint 1**: Summarize gathered requirements in bullet form and ask: *"Does this look correct? Would you like to adjust anything before I build the strategy?"*

### Step 2: Platform Selection and Strategy

Using the Platform Strategy Matrix below, recommend 2-3 primary platforms. For each platform, specify:
- Recommended post frequency (adjusted to user's capacity)
- Primary content style
- Initial KPI target based on the Metrics section

**Error handling**: If the user's industry doesn't clearly map to any platform, default to LinkedIn (professional audiences) + Instagram (visual/content versatility) and explain: *"I've selected these platforms as the safest starting point. As we gather data, we can adjust."*

> **🛑 Checkpoint 2**: Present the platform recommendations table and ask: *"Do these platforms feel right for your audience? Any you'd like to add or remove?"*

### Step 3: Content Pillar Allocation

Apply the 40/25/25/10 rule from the Content Pillar Framework. For each pillar, propose 2-3 specific topic ideas tied to the user's industry/niche.

**Error handling**: If the user doesn't have enough content history for all pillars (e.g., no case studies yet), adjust the ratio temporarily — increase Educational to 50% and reduce Social Proof to 15% until materials exist.

> **🛑 Checkpoint 3**: Share the pillar plan with topic examples and ask: *"Do these content themes align with your brand? Any pillars you'd prioritize differently?"*

### Step 4: Build Content Calendar

Using the Content Calendar Template below, create a 2-week sample calendar with:
- Platform-specific post topics for each day
- Format notes (carousel, thread, reel, story, etc.)
- The repurposing flow linking content across platforms

**Error handling**: If the user has limited capacity (<5 hours/week), reduce calendar to 3 posts/week across all platforms and prioritize the highest-ROI platform only.

> **🛑 Checkpoint 4**: Present the calendar draft and ask: *"Here's a sample 2-week calendar. Would you like me to adjust the frequency, platforms, or topics before we finalize?"*

### Step 5: Engagement Tactics Plan

Outline a daily/weekly engagement routine using the Engagement Tactics section below. Scale to the user's capacity:

| Capacity | Pre-Post Engagement | Reply Window | DM Outreach |
|----------|-------------------|--------------|-------------|
| <3 hrs/week | 3-5 comments, 3x/week | Within 4 hours | 2 DMs/week |
| 3-10 hrs/week | 10-15 comments, daily | Within 2 hours | 5 DMs/week |
| 10+ hrs/week | 15+ comments, daily | Within 1 hour | 10+ DMs/week |

**Error handling**: If the user cannot commit to any engagement routine, recommend a minimum viable tactic: reply to every comment within 24 hours, and comment on 3 posts before each publishing session.

### Step 6: Measurement Framework

Define a tracking cadence and provide a simple tracking template:

- **Weekly** (Mondays): Record engagement rate, reach, follower count, top-performing post
- **Monthly** (1st of month): Full KPI review against benchmarks from the Metrics section

**Error handling**: If the user has no analytics tools, provide a manual Google Sheets template with columns: Date | Platform | Post Type | Impressions | Engagements | Comments | Shares | Notes.

> **🛑 Checkpoint 5**: Confirm the user has analytics access (platform native or third-party). Ask: *"How will you track these metrics? I can provide a manual tracking template if needed."*

### Step 7: Deliver Final Strategy Document

Compile all confirmed sections into a single strategy document with:
1. Platform Strategy Summary
2. Content Pillar Plan
3. 2-Week Content Calendar
4. Engagement Routine
5. KPI Dashboard Template
6. 30/60/90 Day Review Milestones

> **🛑 Final Checkpoint**: *"Here's your complete social media strategy. Would you like me to export this as a downloadable document, or make any final adjustments?"*

---

## Agent Output Templates

Use these exact templates when generating deliverables. Replace `[bracketed]` placeholders with user-specific content.

### Template: Platform Strategy Recommendation

```
## Recommended Platform Strategy for [Client/Company]

| Platform | Role | Post Frequency | Content Style | Primary KPI | Why This Platform |
|----------|------|---------------|---------------|-------------|-------------------|
| [Platform 1] | Primary | [X posts/week] | [Style] | [Metric] | [1-sentence justification tied to audience/goal] |
| [Platform 2] | Secondary | [X posts/week] | [Style] | [Metric] | [1-sentence justification] |
| [Platform 3] | Experimental | [X posts/week] | [Style] | [Metric] | [1-sentence justification] |

**Estimated weekly time commitment:** [X hours]
**90-day growth target:** [X followers / X% engagement rate]
```

### Template: Content Calendar (2-Week Sample)

```
## [Month] Content Calendar — [Client/Company]
**Theme:** [Monthly content theme]
**Goal:** [Metric target]

| Date | Day | Platform | Topic / Hook | Format | Pillar | Repurposed From |
|------|-----|----------|-------------|--------|--------|----------------|
| [Date] | Mon | LinkedIn | [Specific post topic/hook] | Carousel | Educational | Blog post |
| [Date] | Tue | Twitter/X | [Thread topic] | Thread (5 tweets) | Thought Leadership | LinkedIn carousel |
| [Date] | Wed | Instagram | [Visual topic] | Reel | Social Proof | — |
| ... | ... | ... | ... | ... | ... | ... |

**Repurposing Flow:**
[Source content] → [Platform A format] → [Platform B format] → [Platform C format]
```

### Template: Engagement Routine

```
## Daily Engagement Routine for [Client/Company]

**Before Posting (15 min):**
- Comment on [3-15] posts from accounts: [list 3-5 target accounts/hashtags]
- Reply to all pending comments from yesterday

**After Posting — First 2 Hours:**
- Reply to every new comment within 2 hours
- Engage with anyone who shared/quote-tweeted your post
- Send [1-3] thoughtful DMs to new followers/engagers

**End of Day (5 min):**
- Log impressions, engagements, and follower count
- Note top-performing post and why it worked
```

### Template: KPI Tracking Dashboard

```
## Weekly KPI Tracker — [Month] [Year]

| Week | Platform | Posts | Impressions | Engagements | Engagement Rate | New Followers | Top Post | Notes |
|------|----------|-------|-------------|-------------|-----------------|---------------|----------|-------|
| W1 | LinkedIn | [N] | [N] | [N] | [X%] | [+N] | [Topic] | — |
| W1 | Instagram | [N] | [N] | [N] | [X%] | [+N] | [Topic] | — |
| W2 | ... | ... | ... | ... | ... | ... | ... | ... |

**Monthly Summary:**
- Total reach: [N] | Growth: [%]
- Top platform: [Platform]
- Top content pillar: [Pillar]
- Key insight: [1-2 sentence takeaway]
```

### Template: Strategy Document Outline

When delivering the final strategy, compile into this structure:

```markdown
# Social Media Strategy: [Client/Company]
**Date:** [Date] | **Review cadence:** 30/60/90 days

## 1. Executive Summary
[3-4 sentences: which platforms, why, expected outcomes]

## 2. Platform Strategy
[Platform Strategy Recommendation template]

## 3. Content Pillar Plan
[40/25/25/10 breakdown with 2-3 topic examples per pillar]

## 4. Content Calendar
[2-week sample using Content Calendar template]

## 5. Engagement Routine
[Engagement Routine template scaled to capacity]

## 6. Measurement Framework
[KPI Tracking Dashboard template with benchmarks]

## 7. Milestones
- **30 days:** Establish baseline metrics, test 3 content formats
- **60 days:** Double down on top format, grow engagement rate by 0.5%
- **90 days:** Full strategy review, platform expansion/reduction decision
```

---

## Platform Strategy Matrix

| Platform | Best Audience | Content Style | Post Frequency | Key Metric |
|----------|--------------|--------------|----------------|------------|
| **LinkedIn** | B2B, professionals, recruiters | Thought leadership, case studies, industry insights | 3-5x/week | Engagement rate |
| **Twitter/X** | Tech, media, real-time conversations | Hot takes, threads, commentary, launches | 1-3x/day | Impressions, replies |
| **Instagram** | DTC, lifestyle, visual brands | Reels, carousels, Stories, aesthetic | 3-5x/week + daily Stories | Reach, saves |
| **TikTok** | Gen Z/Millennial, entertainment-first | Short-form video, trends, behind-scenes | 1-3x/day | Views, shares |
| **YouTube** | Long-form education, tutorials | Tutorials, vlogs, podcasts, reviews | 1-2x/week | Watch time, subscribers |
| **Threads** | Text-first, early adopter | Conversational, casual, community | 3-5x/week | Engagement |

## Content Pillar Framework

### 40/25/25/10 Rule

| Pillar | % of Content | Examples |
|--------|-------------|---------|
| **Educational** | 40% | How-tos, tutorials, tips, frameworks, guides |
| **Thought Leadership** | 25% | Opinions, predictions, industry analysis, hot takes |
| **Social Proof** | 25% | Case studies, testimonials, results, behind-the-scenes |
| **Promotional** | 10% | Product launches, offers, CTAs, announcements |

## Platform-Specific Best Practices

### LinkedIn
- Personal profiles outperform company pages 5-10x
- First 2 lines are the hook (before "see more")
- Carousels (PDF documents) get highest reach
- Comment on 10-15 posts before/after publishing for algorithm boost
- Polls get reach but low quality engagement
- Best times: Tue-Thu 8-10am

### Twitter/X
- Threads outperform single tweets for depth
- First tweet must stand alone as a hook
- Quote tweets with added value > plain retweets
- Engage in replies to build visibility
- Trending hashtags only if genuinely relevant
- Best times: Mon-Fri 9am-12pm

### Instagram
- Reels get 2-3x the reach of static posts
- Carousels get highest saves and shares
- Stories for daily engagement and polls
- Use 3-5 hashtags (down from the old 30)
- Collab posts for cross-audience growth
- Best times: Tue-Fri 11am-1pm

## Content Calendar Template

```markdown
# [Month] Content Calendar

## Monthly Theme: [Theme]
## Goals: [Metric targets]

| Week | Mon | Tue | Wed | Thu | Fri |
|------|-----|-----|-----|-----|-----|
| W1 | LI: [Topic] | TW: [Topic] | IG: [Topic] | LI: [Topic] | — |
| W2 | LI: [Topic] | TW: [Topic] | IG: [Topic] | LI: [Topic] | TW: [Topic] |

## Repurposing Flow
Blog post (Mon) → LinkedIn carousel (Tue) → Twitter thread (Wed) → IG Reel (Thu)
```

## Engagement Tactics

1. **Comment-first strategy** — engage with 10-15 accounts in your niche before posting
2. **Reply to every comment** within first 2 hours (algorithm signal)
3. **Ask questions** — posts ending with questions get 2x comments
4. **Tag and mention** — give credit, tag people you reference
5. **DM engagement** — thoughtful DMs to new followers builds community
6. **User-generated content** — reshare and credit customer/community content

## Metrics and KPIs

| Metric | What It Measures | Good Benchmark |
|--------|-----------------|----------------|
| Engagement rate | Interactions / reach | >3% (LinkedIn), >1% (Instagram) |
| Reach | Unique viewers | Growing month-over-month |
| Impressions | Total views | 5-10x follower count |
| Follower growth | Net new followers | 2-5% monthly growth |
| Click-through rate | Link clicks / impressions | >1% |
| Saves/bookmarks | Content value signal | Growing trend |
| Share rate | Shares / reach | >1% = viral potential |
| Reply rate | Comments / impressions | >0.5% |

## Integration with Other Skills

- **content-creator** — Brand voice and content frameworks for social
- **content-pipeline** — Social distribution as the final pipeline stage
- **copywriting-frameworks** — Apply PAS/AIDA to social copy
- **content-workflow** — Plan and schedule social content
