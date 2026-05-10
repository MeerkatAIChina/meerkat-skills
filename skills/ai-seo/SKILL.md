---
name: ai-seo
description: Optimize content to get cited by AI search engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini). Triggers on: "AI SEO", "AEO", "GEO", "LLM optimization", "get cited by AI", "appear in AI answers", "AI visibility", "optimize for ChatGPT/Perplexity". For traditional SEO see seo-audit, for structured data see schema-markup.
metadata:
  version: 2.0.0
  author: Hermes Agent Skill Pipeline
  license: MIT
  hermes:
    skill_type: strategic
    category: marketing
    tags: [ai-seo, aeo, geo, llm-optimization, content-strategy, citations]
    requires: []
    complements: [seo-audit, schema-markup, content-strategy, competitor-alternatives, copywriting]
---

# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot. Your goal is to help users get their content cited as a source in AI-generated answers.

## Quick Start

New to AI SEO? Here's the 80/20 path:

| Step | Action | Time | Impact |
|:-----|:-------|:-----|:------:|
| 1 | **Audit** — Check if you're cited in AI answers for your top 20 queries (see [AI Visibility Audit](#ai-visibility-audit)) | 1-2 hours | Baseline |
| 2 | **Fix robots.txt** — Ensure GPTBot, PerplexityBot, ClaudeBot are allowed | 10 minutes | Unblock citation |
| 3 | **Add schema markup** — FAQ, Article, HowTo schemas on key pages | 1-2 days | +30-40% visibility |
| 4 | **Add statistics + citations** — Back claims with specific numbers and sources | 1-3 hours per page | +40% citation boost |
| 5 | **Add `/pricing.md`** — Machine-readable pricing for AI agents | 30 minutes | AI agent discoverability |
| 6 | **Monitor monthly** — Track AI visibility with tools or manual checks | 1 hour/month | Continuous improvement |

> 💡 **First win:** Allow AI bots in robots.txt and add schema markup. These are fast, high-impact changes that unblock everything else.

### ⏸ Checkpoints

This skill uses explicit confirmation checkpoints. **Do not skip them.**

| # | Checkpoint | When | What to Confirm |
|---|-----------|------|-----------------|
| ⏸1 | **Audit Complete** | After Phase 2 | Review audit findings: which queries trigger AI answers, who's getting cited, which pages need fixes. Confirm priorities before optimizing. |
| ⏸2 | **Strategy Aligned** | After Phase 3 planning | Before implementing: confirm the chosen tactics match business goals and resource constraints. |
| ⏸3 | **Implementation Review** | After key changes | After implementing schema, content changes, or robots.txt updates: verify the changes are live and correct. |
| ⏸4 | **First Results** | After Month 1 | Review initial monitoring data: are citations appearing? Adjust strategy if needed. |

---

## Phase 1: Background — How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources, check the platform-specific documentation for each AI provider.

> **Key takeaway:** Traditional SEO gets you ranked. AI SEO gets you **cited**. A well-structured page on page 2-3 can out-cite a higher-ranking page if it's more extractable and authoritative.

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

### Terminology

| Term | Meaning |
|------|---------|
| **AEO** (Answer Engine Optimization) | Optimizing for AI-generated answers |
| **GEO** (Generative Engine Optimization) | Academic term from Princeton research |
| **LLMO** (LLM Optimization) | Optimizing for large language model outputs |
| **Citation** | When an AI names and links to your brand/page as a source |
| **Extractability** | How easily AI can pull standalone facts from your content |
| **SGE/AI Overviews** | Google's AI-generated answer boxes above search results |

All these terms converge on the same goal: making your content the one AI chooses to reference.

---

## Phase 2: Assess — AI Visibility Audit

### Before Starting: Gather Context

**Check for product context first:** If `.agents/product-marketing-context.md` exists, read it before asking questions. Only ask for information not already covered there.

Gather this context (ask if not provided):

#### 1. Current AI Visibility
- Does your brand appear in AI answers today? (Check ChatGPT, Perplexity, Google AI Overviews)
- What are your top 10-20 most important queries?

#### 2. Content & Domain
- What content types do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing schema markup?

#### 3. Goals
- Get cited as a source in AI answers? Appear in Google AI Overviews?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

#### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Where are they cited that you're not?
- Do you have Wikipedia or review site presence?

### Run the Audit

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test:**
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI bots allowed in robots.txt? | |

### Step 4: AI Bot Access Check

Verify your robots.txt allows AI crawlers. Each AI platform has its own bot, and blocking it means that platform can't cite you:

- **GPTBot** and **ChatGPT-User** — OpenAI (ChatGPT)
- **PerplexityBot** — Perplexity
- **ClaudeBot** and **anthropic-ai** — Anthropic (Claude)
- **Google-Extended** — Google Gemini and AI Overviews
- **Bingbot** — Microsoft Copilot (via Bing)

Check your robots.txt for `Disallow` rules targeting any of these. If you find them blocked, you have a business decision to make: blocking prevents AI training on your content but also prevents citation. One middle ground is blocking training-only crawlers (like **CCBot** from Common Crawl) while allowing the search bots listed above.

See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for the full robots.txt configuration.

> **After the audit:** You should have a clear picture of (1) which queries trigger AI answers, (2) who's getting cited vs. you, and (3) which pages need structural fixes. Use these findings to prioritize the optimization work below.

---

## Phase 3: Optimize — Implementation Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each content block type, adapt the structural rules below to your specific content needs.

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems don't just cite your website — they cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Create YouTube content for key how-to queries
- Answer relevant Quora questions with depth

### Machine-Readable Files for AI Agents

AI agents aren't just answering questions — they're becoming buyers. When an AI agent evaluates tools on behalf of a user, it needs structured, parseable information. If your pricing is locked in a JavaScript-rendered page or a "contact sales" wall, agents will skip you and recommend competitors whose information they can actually read.

Add these machine-readable files to your site root:

**`/pricing.md` or `/pricing.txt`** — Structured pricing data for AI agents

```markdown
# Pricing — [Your Product Name]

## Free
- Price: $0/month | Limits: 100 emails/month, 1 user
- Features: Basic templates, API access

## Pro
- Price: $29/month (annual) | $35/month (monthly)
- Limits: 10,000 emails/month, 5 users
- Features: Custom domains, analytics, priority support

## Enterprise
- Price: Custom — contact sales@example.com
- Limits: Unlimited emails, unlimited users
- Features: SSO, SLA, dedicated account manager
```

**Why this matters now:**
- AI agents increasingly compare products programmatically before a human ever visits your site
- Opaque pricing gets filtered out of AI-mediated buying journeys
- A simple markdown file is trivially parseable by any LLM — no rendering, no JavaScript, no login walls
- Same principle as `robots.txt` (for crawlers), `llms.txt` (for AI context), and `AGENTS.md` (for agent capabilities)

**Best practices:**
- Use consistent units (monthly vs. annual, per-seat vs. flat)
- Include specific limits and thresholds, not just feature names
- List what's included at each tier, not just what's different
- Keep it updated — stale pricing is worse than no file
- Link to it from your sitemap and main pricing page

**`/llms.txt`** — Context file for AI systems (see [llmstxt.org](https://llmstxt.org))

If you don't have one yet, add an `llms.txt` that gives AI systems a quick overview of what your product does, who it's for, and links to key pages (including your pricing).

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility. For implementation, use the **schema-markup** skill.

### Priority Action Matrix

Not sure where to start? Prioritize by impact and effort:

| Priority | Action | Effort | AI Visibility Impact |
|:--------:|:-------|:------:|:--------------------:|
| 🔴 P0 | Allow AI bots in robots.txt | Minutes | Unblocks all citation |
| 🔴 P0 | Add FAQ/Article/HowTo schema | Hours-Days | +30-40% |
| 🟠 P1 | Add statistics with cited sources | Hours | +37-40% |
| 🟠 P1 | Add expert quotes and author bios | Hours | +25-30% |
| 🟡 P2 | Build comparison tables for key queries | Days | +33% citation share |
| 🟡 P2 | Create `/pricing.md` and `llms.txt` | Minutes-Hours | Agent discoverability |
| 🟢 P3 | Build third-party presence (Wikipedia, Reddit, reviews) | Weeks-Months | Long-term authority |
| 🟢 P3 | Monthly AI visibility monitoring | 1 hr/month | Sustained improvement |

---

### Content Types That Get Cited Most

Not all content is equally citable. Prioritize these formats:

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |
| **Opinion/analysis** | ~10% | Expert perspective, quotable |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)

---

## Phase 4: Monitor — Tracking AI Visibility

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (see below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Source attribution | Which of your pages get cited | Track referral traffic from AI sources |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month

---

### AI SEO for Different Content Types

#### SaaS Product Pages

**Goal:** Get cited in "What is [category]?" and "Best [category]" queries.

**Optimize:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables (you vs. category, not just competitors)
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing) — add a `/pricing.md` file so AI agents can parse your plans without rendering your page (see "Machine-Readable Files" above)
- FAQ section addressing common buyer questions

#### Blog Content

**Goal:** Get cited as an authoritative source on topics in your space.

**Optimize:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

#### Comparison/Alternative Pages

**Goal:** Get cited in "[X] vs [Y]" and "Best [X] alternatives" queries.

**Optimize:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data
- Cite the competitor-alternatives skill for building these pages

#### Documentation / Help Content

**Goal:** Get cited in "How to [X] with [your product]" queries.

**Optimize:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes

---

## Chinese AI Search Ecosystem (中国 AI 搜索生态)

For brands targeting the Chinese market, optimize for China's distinct AI search platforms:

| Platform | Ecosystem | Bot User-Agent | Notes |
|----------|-----------|---------------|-------|
| **百度 AI** | Baidu index | `Baiduspider` | Dominant in China; integrates with ERNIE Bot |
| **豆包 (Doubao)** | ByteDance | `Bytespider` | Fast-growing; cites from Toutiao, Douyin content |
| **文心一言 (ERNIE Bot)** | Baidu | `Baiduspider` | Baidu's LLM; pulls from Baidu index + Baike |
| **Kimi** | Moonshot AI | Check robots.txt | Strong at long-form content extraction |
| **通义千问 (Tongyi)** | Alibaba | Check robots.txt | Integrates with Alibaba ecosystem |
| **360 AI** | 360 Search | `360Spider` | Integrated with 360 Search results |
| **秘塔 (MetaSo)** | Independent | Check robots.txt | Legal/professional focus; values authoritative sources |

**Key differences from Western AI SEO:**
- **百度百科 presence matters more than Wikipedia** — Baidu's AI heavily weights Baidu Baike (百度百科) entries
- **微信生态** — WeChat Official Accounts content is indexed by some Chinese AI platforms
- **备案/ICP requirement** — Sites without ICP registration may be deprioritized
- **Content hosting** — Content on domestic Chinese platforms (知乎, 小红书, CSDN) often outranks independent sites
- **Regulatory compliance** — AI platforms in China must comply with content regulations; avoid sensitive topics

**Action items for Chinese market:**
- [ ] Create/maintain 百度百科 entry for your brand
- [ ] Ensure ICP registration is current and valid
- [ ] Host content on 知乎, 小红书, and 微信公众号 in addition to your own site
- [ ] Use simplified Chinese throughout; traditional Chinese has lower AI extractability
- [ ] Allow `Baiduspider` and `Bytespider` in robots.txt

---

### Access & Discovery
- **Ignoring AI search** — ~45% of Google searches now show AI Overviews. AI SEO is no longer optional.
- **Gating or blocking content** — AI can't access gated/PDF-only content; blocking GPTBot/PerplexityBot/ClaudeBot in robots.txt prevents citation entirely. Keep authoritative content open and allow AI search crawlers.
- **Weak third-party presence** — AI often cites Wikipedia, Reddit, review sites more than your own domain. Build presence where AI looks.

### Content Quality
- **Writing for AI, not humans** — Content that reads like algorithm-gaming won't get cited or convert.
- **Generic content without data** — "We're the best" won't get cited. "Customers see 3x improvement in [metric]" will. Include specific statistics with sources.
- **Keyword stuffing** — Actively reduces AI visibility by 10% (Princeton GEO study), unlike traditional SEO where it's merely ineffective.

### Technical
- **No freshness signals** — Undated content loses to dated content. Show "Last updated" prominently and refresh quarterly.
- **No structured data** — Schema markup (FAQ, HowTo, Article, Product) gives AI structured context. Missing it drops visibility 30-40%.
- **Opaque pricing** — Hiding pricing behind "contact sales" or JS-rendered pages makes AI agents skip you. Add a `/pricing.md` file.

### Process
- **Not monitoring** — You can't improve what you don't measure. Check AI visibility monthly at minimum.

---

## Measuring Success & ROI

### What Success Looks Like (Realistic Timeline)

| Timeframe | Milestone | Signal |
|:----------|:----------|:-------|
| Week 1-2 | Technical foundation | AI bots allowed, schema deployed, `/pricing.md` live |
| Month 1-2 | Content optimized | Key pages have statistics, citations, expert quotes |
| Month 3-4 | First citations | Brand appears in AI answers for 2-5 niche queries |
| Month 6 | Competitive parity | Cited for 30-50% of target queries where competitors appear |
| Month 12 | AI visibility leadership | Cited more often than competitors for core queries |

### Measuring ROI

AI SEO ROI can be measured through:

| Metric | How to Measure | Tools |
|--------|---------------|-------|
| **AI referral traffic** | Track UTM-tagged links from AI platforms | GA4, referral reports |
| **Brand citation rate** | % of target queries where brand is cited | Otterly, Peec, ZipTie, manual checks |
| **Share of AI voice** | Your citations ÷ total citations in space | Otterly, Peec |
| **Citation-to-conversion** | Track conversions from AI-referred visitors | GA4 + UTM parameters |
| **Competitive displacement** | Queries where you replaced a competitor as cited source | Manual tracking spreadsheet |

> 💡 **Realistic ROI expectation:** Companies investing in AI SEO typically see 15-40% increase in AI-driven referral traffic within 6 months. For B2B SaaS, AI-mediated buying journeys are growing 3x year-over-year — being invisible to AI agents means losing deals before a human ever visits your site.

### Example Scenario: B2B SaaS

A project management SaaS company ($10M ARR) implemented AI SEO:

- **Before:** Zero AI citations for "best project management software." Competitors cited in 8/20 target queries.
- **Actions:** Added schema markup, created 5 comparison pages with data, published original research, added `/pricing.md` and `llms.txt`.
- **After (6 months):** Cited in 14/20 target queries. AI referral traffic up 28%. Two enterprise deals attributed to AI agent evaluations.

---

## Tool Integrations

| Tool | Use For |
|------|---------|
| `semrush` | AI Overview tracking, keyword research, content gap analysis |
| `ahrefs` | Backlink analysis, content explorer, AI Overview data |
| `gsc` | Search Console performance data, query tracking |
| `ga4` | Referral traffic from AI sources |
| `otterly` | Multi-platform AI visibility tracking |
| `peec` | Multi-platform citation monitoring |

---

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO audits
- **schema-markup**: For implementing structured data that helps AI understand your content
- **content-strategy**: For planning what content to create
- **competitor-alternatives**: For building comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable

---

## Verification Checklist

After completing an AI SEO task, verify:

- [ ] Description in frontmatter is ≤ 1024 characters
- [ ] All 4 ⏸ CHECKPOINT confirmations were completed
- [ ] AI bot access audit completed (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot)
- [ ] Schema markup recommendations provided for priority pages
- [ ] At least 3 content optimization recommendations given (statistics, citations, structure)
- [ ] Chinese market: 百度百科/ICP/知乎/小红书 considerations addressed if relevant
- [ ] `/pricing.md` and `llms.txt` creation recommended where applicable
- [ ] Monitoring plan (tools + DIY method) provided
- [ ] Priority Action Matrix reviewed with user
- [ ] All file references in this SKILL.md point to existing resources
