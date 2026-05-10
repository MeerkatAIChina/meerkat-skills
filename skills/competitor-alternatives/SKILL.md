---
name: competitor-alternatives
description: "Create SEO-optimized competitor comparison and alternative pages. Covers 4 formats: singular alternative, plural alternatives, you-vs-competitor, and competitor-vs-competitor. Supports both SaaS/digital products and FMCG/consumer goods. Use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'battle card,' or 'competitor teardown.' For sales-specific internal collateral, see sales-enablement."
metadata:
  hermes:
    version: "2.0.0"
    author: "Hermes Agent Skill Pipeline"
    license: "MIT"
    category: "content-marketing"
    tags:
      - competitor-analysis
      - seo-content
      - comparison-pages
      - alternative-pages
      - sales-enablement
      - fmcg
      - consumer-goods
    related_skills:
      - programmatic-seo
      - copywriting
      - seo-audit
      - schema-markup-generator
      - sales-enablement
      - competitor-ads-analyst
    supported_industries:
      - saas
      - fmcg
      - consumer-goods
      - ecommerce
  version: 2.0.0
---

# Competitor & Alternative Pages

You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively.

---

## End-to-End Workflow

Follow this SOP for every competitor page project:

### Phase 1: Discovery & Research (Input)
1. **Receive trigger**: User requests a competitor/alternative page (mentioning competitor name, target format, or search term)
2. **Load product context**: Read `.agents/product-marketing-context.md` if available
3. **Determine industry**: SaaS/digital or FMCG/consumer goods → select appropriate comparison dimensions
4. **Gather competitor intel**: Follow the Research Process (product testing, pricing, review mining, customer interviews)
5. **Fill competitor data template**: Use centralized YAML format (see Content Architecture)

### Phase 2: Strategy & Planning
6. **Select page format(s)**: Based on search intent — singular alternative, plural alternatives, you-vs-competitor, or competitor-vs-competitor
7. **Keyword research**: Identify primary and secondary target keywords per format
8. **Prioritize pages**: Create a Page Set Plan ordered by search volume and business impact
9. **Define URL structure**: Align with site architecture (`/alternatives/`, `/vs/`, `/compare/`)

### Phase 3: Content Production
10. **Draft each page**: Follow the page structure for the selected format
11. **Apply Core Principles**: Honesty, depth, decision-helpfulness, modular data sourcing
12. **Write comparison tables**: Go beyond checkmarks — use descriptive comparisons (see Essential Sections)
13. **Add migration section**: If applicable, detail switching process and support
14. **Include social proof**: Quotes from switchers, aggregate reviews, case studies

### Phase 4: Optimization & Delivery (Output)
15. **SEO polish**: Meta title/description, H1-H3 hierarchy, internal links, FAQ schema
16. **CRO review**: Clear CTAs, trust signals, friction reduction
17. **Legal check**: Confirm trademark usage is nominative fair use; avoid defamatory claims
18. **Deliver final output**: Page copy, meta tags, comparison tables, internal linking map

---

## Output Specifications

### Deliverable 1: Page Content (per page)

```markdown
## Page: [Title]
**URL**: /alternatives/notion
**Format**: Singular Alternative
**Target Keywords**: "notion alternative", "alternative to notion", "switch from notion"

### Meta Tags
- Title: "[Your Product] vs Notion: Which Is Right for You? [Year]"
- Description: "[X]-word comparison of [Your Product] and Notion. Compare features, pricing, and more..."
- H1: "[Your Product] vs Notion: An Honest Comparison"

### Body Copy
[Full page content organized by the format's structure, including:
- TL;DR summary
- Feature comparison paragraphs
- Pricing comparison table
- Who each is best for
- Migration guidance
- Customer testimonials
- CTA]

### Internal Links
- Link to: /alternatives (hub page)
- Link to: /vs/notion-airtable (related comparison)
- Link from: /features/collaboration (relevant feature page)
```

### Deliverable 2: Competitor Data File (YAML)

```yaml
# Saved to competitor_data/notion.md
name: Notion
# ... full competitor profile per Content Architecture template
```

### Deliverable 3: Page Set Plan

```markdown
## Recommended Comparison Pages for [Your Product]
Priority order based on search volume × conversion potential:

1. **[Your Product] vs Notion** — SV: 8,100/mo — Format: You vs Competitor
2. **Notion Alternative** — SV: 4,400/mo — Format: Singular Alternative
3. **Notion Alternatives** — SV: 2,900/mo — Format: Plural Alternatives
4. **Notion vs Airtable** — SV: 1,600/mo — Format: Competitor vs Competitor
... (continue for all priority competitors)
```

---

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

**Identify the industry context** — the comparison framework differs significantly between SaaS/digital products and FMCG/consumer goods:

### For SaaS/Digital Products
Before creating competitor pages, understand:

1. **Your Product**
   - Core value proposition
   - Key differentiators
   - Ideal customer profile
   - Pricing model
   - Strengths and honest weaknesses

2. **Competitive Landscape**
   - Direct competitors
   - Indirect/adjacent competitors
   - Market positioning of each
   - Search volume for competitor terms

3. **Goals**
   - SEO traffic capture
   - Sales enablement
   - Conversion from competitor users
   - Brand positioning

### For FMCG / Consumer Goods
Additional dimensions to assess:

1. **Product Attributes**
   - Ingredients / materials / formulation
   - Packaging formats (size, SKU variants)
   - Sensory attributes (taste, scent, texture)
   - Certifications (organic, halal, vegan, etc.)

2. **Commercial Factors**
   - Price per unit / per serving
   - Retail price bands (mass, premium, luxury)
   - Promotion frequency and mechanics
   - Distribution channels (modern trade, e-commerce, DTC, convenience)
   - Shelf placement and in-store visibility

3. **Consumer Decision Drivers**
   - Brand loyalty vs. price sensitivity in the category
   - Trial-to-repeat conversion patterns
   - Influencer/KOL impact on switching
   - Seasonality and occasion-based purchasing

---

## Core Principles

### 1. Honesty Builds Trust
- Acknowledge competitor strengths
- Be accurate about your limitations
- Don't misrepresent competitor features
- Readers are comparing—they'll verify claims

### 2. Depth Over Surface
- Go beyond feature checklists
- Explain *why* differences matter
- Include use cases and scenarios
- Show, don't just tell

### 3. Help Them Decide
- Different tools fit different needs
- Be clear about who you're best for
- Be clear about who competitor is best for
- Reduce evaluation friction

### 4. Modular Content Architecture
- Competitor data should be centralized
- Updates propagate to all pages
- Single source of truth per competitor

---

## Page Formats

### Format 1: [Competitor] Alternative (Singular)

**Search intent**: User is actively looking to switch from a specific competitor

**URL pattern**: `/alternatives/[competitor]` or `/[competitor]-alternative`

**Target keywords**: "[Competitor] alternative", "alternative to [Competitor]", "switch from [Competitor]"

**Page structure**:
1. Why people look for alternatives (validate their pain)
2. Summary: You as the alternative (quick positioning)
3. Detailed comparison (features, service, pricing)
4. Who should switch (and who shouldn't)
5. Migration path
6. Social proof from switchers
7. CTA

---

### Format 2: [Competitor] Alternatives (Plural)

**Search intent**: User is researching options, earlier in journey

**URL pattern**: `/alternatives/[competitor]-alternatives`

**Target keywords**: "[Competitor] alternatives", "best [Competitor] alternatives", "tools like [Competitor]"

**Page structure**:
1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (criteria framework)
3. List of alternatives (you first, but include real options)
4. Comparison table (summary)
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

**Important**: Include 4-7 real alternatives. Being genuinely helpful builds trust and ranks better.

---

### Format 3: You vs [Competitor]

**Search intent**: User is directly comparing you to a specific competitor

**URL pattern**: `/vs/[competitor]` or `/compare/[you]-vs-[competitor]`

**Target keywords**: "[You] vs [Competitor]", "[Competitor] vs [You]"

**Page structure**:
1. TL;DR summary (key differences in 2-3 sentences)
2. At-a-glance comparison table
3. Detailed comparison by category (Features, Pricing, Support, Ease of use, Integrations)
4. Who [You] is best for
5. Who [Competitor] is best for (be honest)
6. What customers say (testimonials from switchers)
7. Migration support
8. CTA

---

### Format 4: [Competitor A] vs [Competitor B]

**Search intent**: User comparing two competitors (not you directly)

**URL pattern**: `/compare/[competitor-a]-vs-[competitor-b]`

**Page structure**:
1. Overview of both products
2. Comparison by category
3. Who each is best for
4. The third option (introduce yourself)
5. Comparison table (all three)
6. CTA

**Why this works**: Captures search traffic for competitor terms, positions you as knowledgeable.

---

## Industry Adaptations

### SaaS vs. FMCG Comparison Dimensions

The comparison dimensions shift significantly between digital products and physical consumer goods. Adapt your page structure accordingly:

| Dimension | SaaS Focus | FMCG / CPG Focus |
|-----------|-----------|-------------------|
| **Features** | Functionality, integrations, API | Ingredients, formulation, efficacy |
| **Pricing** | Per-seat, tiered, usage-based | Per unit, per serving, bundle deals |
| **User Experience** | UI/UX, onboarding, learning curve | Taste, scent, texture, convenience |
| **Availability** | Global (digital) | Regional distribution, channel coverage |
| **Social Proof** | G2/Capterra reviews, case studies | E-commerce ratings, KOL reviews, blind tests |
| **Switching Cost** | Data migration, retraining | Price difference, habit change, availability |
| **Comparable Metrics** | Uptime, response time, API limits | Nutritional values, efficacy %, price/g or ml |

### FMCG-Specific Page Elements

When building comparison pages for consumer goods, include:

1. **Side-by-Side Product Photos**: Visual comparison of packaging, serving size, product appearance
2. **Price Breakdown Table**: Price per unit (per 100g, per serving, per ml) for fair comparison
3. **Ingredient/Formula Comparison**: Highlight differences in active ingredients, preservatives, allergens
4. **Taste/Experience Comparison**: Descriptive, sensory language backed by blind test data if available
5. **Availability Map**: Where each product can be purchased (online platforms, retail chains, regions)
6. **Promotion Calendar Context**: How discount frequency affects effective price
7. **Sustainability Comparison**: Packaging materials, carbon footprint, ethical sourcing

### FMCG Comparison Page Structure (Adapted Format 3: You vs Competitor)

1. **At-a-Glance Summary**: Price per unit, key ingredient difference, best for scenario
2. **Product Photo Comparison**: Side-by-side packaging shots with callouts
3. **Ingredient Deep Dive**: What's inside each product — what's different, why it matters
4. **Taste / Sensory Comparison**: Descriptive comparison (be honest about competitor strengths)
5. **Price & Value Analysis**: Unit economics, bulk savings, promotion-adjusted cost
6. **Where to Buy**: Channel availability comparison table
7. **Consumer Reviews at a Glance**: Aggregate ratings from major e-commerce platforms
8. **Who Each Is Best For**: Usage occasion, dietary preference, budget segment
9. **Try Our Product**: Sampling offer, money-back guarantee, trial-size purchase link
10. **CTA**

### FMCG Competitor Data Template (Extension)

Extend the centralized competitor data with FMCG-specific fields:

```yaml
# FMCG-specific fields (add to competitor data)
fmcg:
  category: "instant noodles"
  subcategory: "spicy chicken flavor"
  pack_sizes: ["60g cup", "120g bowl", "5-pack bundle"]
  price_per_unit: 1.50  # USD per serving
  retail_channels: ["Walmart", "Amazon", "7-Eleven", "Costco"]
  ecommerce_platforms: ["Amazon", "Shopee", "Lazada"]
  certifications: ["Halal", "ISO 22000"]
  key_ingredients: ["wheat flour", "palm oil", "MSG"]
  allergens: ["wheat", "soy"]
  nutritional_per_serving:
    calories: 420
    sodium_mg: 1800
    protein_g: 8
  sensory_profile:
    spiciness: 7/10
    richness: 6/10
    texture: "chewy noodles"
  avg_rating:
    amazon: 4.2
    shopee: 4.5
    lazada: 4.3
  promotion_cadence: "monthly flash sales, quarterly bundle deals"
```

---

## Essential Sections

### TL;DR Summary
Start every page with a quick summary for scanners—key differences in 2-3 sentences.

### Paragraph Comparisons
Go beyond tables. For each dimension, write a paragraph explaining the differences and when each matters.

### Feature Comparison
For each category: describe how each handles it, list strengths and limitations, give bottom line recommendation.

### Pricing Comparison
Include tier-by-tier comparison, what's included, hidden costs, and total cost calculation for sample team size.

### Who It's For
Be explicit about ideal customer for each option. Honest recommendations build trust.

### Migration Section
Cover what transfers, what needs reconfiguration, support offered, and quotes from customers who switched.

**For detailed templates**: See [references/templates.md](references/templates.md)

> **Inline quick reference**: The reference file provides copy-paste Markdown templates for: TL;DR Summary, Paragraph Comparison, Feature Comparison, Pricing Comparison, Service & Support, Who It's For, Migration, Social Proof, and Comparison Table Best Practices (beyond checkmarks, organize by category, include ratings where useful).

---

## Content Architecture

### Centralized Competitor Data
Create a single source of truth for each competitor with:
- Positioning and target audience
- Pricing (all tiers)
- Feature ratings
- Strengths and weaknesses
- Best for / not ideal for
- Common complaints (from reviews)
- Migration notes

**For data structure and examples**: See [references/content-architecture.md](references/content-architecture.md)

> **Inline quick reference**: Use the YAML template below as a starting point. Core fields: `name`, `tagline`, `pricing.*`, `strengths[]`, `weaknesses[]`, `best_for[]`, `not_ideal_for[]`, `common_complaints[]`, `migration_from.*`. For FMCG products, add the `fmcg.*` extension block from the Industry Adaptations section.

---

## Research Process

### Deep Competitor Research

For each competitor, gather:

1. **Product research**: Sign up, use it, document features/UX/limitations
2. **Pricing research**: Current pricing, what's included, hidden costs
3. **Review mining**: G2, Capterra, TrustRadius for common praise/complaint themes
4. **Customer feedback**: Talk to customers who switched (both directions)
5. **Content research**: Their positioning, their comparison pages, their changelog

### Ongoing Updates

- **Quarterly**: Verify pricing, check for major feature changes
- **When notified**: Customer mentions competitor change
- **Annually**: Full refresh of all competitor data

### Maintenance Checklist

Use this checklist to keep competitor pages accurate and high-performing:

- [ ] **Pricing audit** (quarterly): Verify all competitor pricing tiers, hidden fees, and bundling
- [ ] **Feature parity check** (quarterly): Confirm feature claims still accurate; note new competitor launches
- [ ] **Review mining refresh** (quarterly): Scan G2/Capterra/Amazon reviews for new complaint themes
- [ ] **Screenshot update** (bi-annual): Refresh product/packaging photos to reflect current designs
- [ ] **SEO performance review** (monthly): Check rankings, CTR, and conversion rates for key comparison pages
- [ ] **Broken link check** (monthly): Verify all competitor website links and internal cross-links
- [ ] **Legal compliance review** (annual): Confirm trademark usage, comparative advertising compliance per jurisdiction
- [ ] **Full content refresh** (annual): Rewrite/update all comparison pages with latest data

---

## SEO Considerations

### Keyword Targeting

| Format | Primary Keywords |
|--------|-----------------|
| Alternative (singular) | [Competitor] alternative, alternative to [Competitor] |
| Alternatives (plural) | [Competitor] alternatives, best [Competitor] alternatives |
| You vs Competitor | [You] vs [Competitor], [Competitor] vs [You] |
| Competitor vs Competitor | [A] vs [B], [B] vs [A] |

### Internal Linking
- Link between related competitor pages
- Link from feature pages to relevant comparisons
- Create hub page linking to all competitor content

### Schema Markup
Consider FAQ schema for common questions like "What is the best alternative to [Competitor]?"

---

## Conversion Rate Optimization (CRO) for Comparison Pages

Comparison pages have unique CRO dynamics — visitors are in evaluation mode, not discovery mode. Optimize for this intent:

### CTA Strategy by Visitor Intent

| Visitor Intent | Best CTA | Placement |
|---------------|----------|-----------|
| **Researching options** | "See full feature list" / "Watch demo" | After feature comparison |
| **Price-sensitive** | "View pricing" / "Calculate your savings" | Next to pricing table |
| **Ready to switch** | "Start free trial" / "Switch now" | After migration section + testimonials |
| **Just browsing** | "Join [X]K+ teams" / Newsletter sign-up | Sticky bar or exit intent |

### Trust Signals to Include
- **Third-party ratings**: G2 badges, Capterra stars, Amazon ratings (FMCG)
- **Customer logos**: Recognizable brands that use your product
- **Switcher statistics**: "X companies switched from [Competitor] this year"
- **Money-back guarantee / trial**: Reduce perceived risk of switching
- **Data residency / security certifications**: For enterprise SaaS comparisons

### A/B Testing Priorities for Comparison Pages
1. **Headline framing**: "vs" vs "Alternative to" vs "Why switch from"
2. **CTA placement**: Above fold vs. after comparison vs. sticky
3. **Pricing display**: Monthly vs. annual vs. per-unit comparison
4. **Testimonial format**: Text quotes vs. video vs. case study summaries
5. **Comparison table style**: Checklist vs. descriptive vs. rating stars

---

## Legal & Compliance Guidelines

### Trademark Usage in Comparison Pages
- **Nominative fair use**: You may use competitor names to refer to their products, but do not imply endorsement or affiliation
- **Do NOT**: Use competitor logos without permission (text references are safer)
- **Do NOT**: Register domains containing competitor trademarks (e.g., `notionvsurproduct.com`)
- **DO**: Include a disclaimer: "[Competitor] is a trademark of [Company]. We are not affiliated with or endorsed by [Company]."

### Comparative Advertising Rules by Region

| Jurisdiction | Key Requirement |
|-------------|----------------|
| **USA (FTC)** | Claims must be truthful, substantiated, and not misleading. Puffery allowed within limits. |
| **EU (Directive 2006/114/EC)** | Comparative advertising permitted if: not misleading, compares goods for same needs, objective comparison of verifiable features, no denigration, no unfair advantage of reputation. |
| **UK (CAP Code)** | Comparisons must compare like with like, be objectively verifiable, and not unfairly discredit competitor. |
| **China (广告法)** | Comparative advertising generally restricted. Avoid direct competitor naming in most cases. Use generic "other leading brands" approach. |
| **SEA markets** | Varies significantly; Indonesia and Thailand are more permissive, Singapore follows UK-style rules. |

### Content Risk Mitigation
- **Substantiate all claims**: Store evidence for every factual claim (screenshots, dated pricing, test results)
- **Date-stamp comparisons**: Include "Last updated: [Date]" to show freshness and limit liability for outdated claims
- **Avoid superlatives without proof**: "Best" / "Fastest" / "Cheapest" require substantiation
- **Review legal with counsel**: For high-traffic pages in regulated industries (finance, health, alcohol)

---

## Conversion Tracking & Performance Measurement

### KPIs for Comparison Pages

| Metric | Target | Why It Matters |
|--------|--------|---------------|
| Organic traffic | Growing MoM | SEO effectiveness |
| Avg. time on page | >3 min | Content engagement depth |
| Bounce rate | <60% | Relevance to search intent |
| CTA click-through | >5% | Conversion effectiveness |
| Trial/demo sign-ups | Track per page | Direct revenue attribution |
| Rank for target keywords | Top 5 | Competitive SERP visibility |
| Exit rate at pricing section | <20% | Price objection identification |

### Revenue Attribution Model
1. **First-touch**: Comparison page was first interaction → SEO acquisition credit
2. **Last-touch**: Comparison page was last page before conversion → CRO credit
3. **Assisted**: Comparison page appeared in conversion path → influence credit

Set up UTM parameters for all CTAs on comparison pages: `utm_source=competitor-page&utm_medium=organic&utm_campaign=comparison&utm_content=[competitor-name]`

---

## Output Format

> **Note**: Detailed output specifications with templates are provided in [Output Specifications](#output-specifications) above. See Deliverable 1 (Page Content), Deliverable 2 (Competitor Data File), and Deliverable 3 (Page Set Plan) for full templates.

### Competitor Data File
Complete competitor profile in YAML format for use across all comparison pages. See Content Architecture section for the data template structure.

### Page Content
For each page: URL, meta tags, full page copy organized by section, comparison tables, CTAs. Follow the page structure defined in the Page Formats section for the selected format.

### Page Set Plan
Recommended pages to create with priority order based on search volume and conversion potential. Include target keywords, format type, and estimated monthly search volume.

---

## Discovery Questions

Ask these during the Initial Assessment phase to fill gaps not covered by the product marketing context file:

### Product & Positioning
1. What are the top 3 reasons customers switch from competitors to you?
2. What honest limitations should we acknowledge about your product?

### Customer Evidence
3. Do you have customer quotes or case studies specifically about switching?
4. What do your customers say they gained after switching (specific metrics)?

### Commercial & Migration
5. What's your pricing vs. the target competitor (tier-by-tier if possible)?
6. Do you offer migration support, data import tools, or onboarding assistance?
7. What's your trial or sampling policy (free trial, money-back guarantee, sample-size purchase)?

### FMCG-Specific
8. What are your key retail/e-commerce channels vs. the competitor?
9. Do you have blind test or sensory panel results vs. the competitor?
10. What's your promotion calendar vs. the competitor's typical discount pattern?

---

## Related Skills

- **programmatic-seo**: For building competitor pages at scale
- **copywriting**: For writing compelling comparison copy
- **seo-audit**: For optimizing competitor pages
- **schema-markup**: For FAQ and comparison schema
- **sales-enablement**: For internal sales collateral, decks, and objection docs

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **2.0.0** | 2026-05-10 | Major update: Added comprehensive FMCG/consumer goods adaptation (Industry Adaptations section, FMCG data template, FMCG page structure). Added end-to-end SOP workflow (4 phases). Added output specifications with 3 deliverable templates. Added CRO strategy for comparison pages (CTA by intent, trust signals, A/B testing priorities). Added legal & compliance guidelines with jurisdiction-specific rules (USA, EU, UK, China, SEA). Added conversion tracking KPIs and revenue attribution model. Restructured metadata with `hermes` block (category, tags, related_skills, supported_industries). Added maintenance checklist (8 items). Added inline quick-reference summaries for reference files. Expanded discovery questions (10 items covering product, customer, commercial, and FMCG). |
| **1.1.0** | 2025-09-15 | Added Schema Markup section, improved keyword targeting table, added footer navigation architecture from references. |
| **1.0.0** | 2025-06-01 | Initial release. Four page formats, research process, content architecture, essential sections. |
