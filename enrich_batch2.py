# -*- coding: utf-8 -*-
"""
enrich_batch2.py  
Rich theory for:
  - tech_entrepreneurship.json (8 lessons)
  - ui_ux.json (14 lessons)
  - generative_theory.json (9 lessons)
  - data_structures_algorithms.json (23 lessons)
"""
import json, os

def patch(track_file, theory_dict):
    path = os.path.join("curriculum", "tracks", track_file)
    print(f"\n{'='*55}\nLoading {track_file}...")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    patched = 0; short = 0
    for topic_data in data.values():
        for lesson in topic_data.get("lessons", []):
            t = lesson.get("title", "")
            if t in theory_dict:
                lesson["theory"] = theory_dict[t]
                patched += 1
            elif lesson.get("type") != "quiz" and len(lesson.get("theory","")) <= 800:
                short += 1; print(f"  [??] Still short: {t!r}")
    print(f"Patched: {patched} | Still short: {short}")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved.")


# ══════════════════════════════════════════════════
# TECH ENTREPRENEURSHIP (8 lessons)
# ══════════════════════════════════════════════════
TECH_THEORY = {

"The Agile Manifesto": """## The 4 Values That Changed Software Development

In 2001, seventeen software developers met in Utah and published the **Agile Manifesto**  -  a set of values and principles that revolutionized how software is built. Before Agile, most teams used "Waterfall": plan everything upfront, code for months, deliver once. Agile replaced this with short, iterative cycles and constant collaboration.

### The 4 Core Values

The manifesto declares that while items on the right have value, items on the left are valued more:

| We value... | Over... |
|---|---|
| **Individuals and interactions** | Processes and tools |
| **Working software** | Comprehensive documentation |
| **Customer collaboration** | Contract negotiation |
| **Responding to change** | Following a plan |

### What This Means in Practice

**Individuals and interactions over processes and tools:**
A direct conversation resolves misunderstandings in minutes. A formal change-request process takes days. Talk to your teammates. Tools should enable collaboration, not replace it.

**Working software over comprehensive documentation:**
A 200-page spec that nobody reads is worth less than a simple feature users can click. Ship early, ship often. Real software answers real questions that documents cannot.

**Customer collaboration over contract negotiation:**
Involve your users and stakeholders throughout the process. Don't disappear for 6 months and return with what YOU thought they wanted. They will have changed their minds  -  and that's okay.

**Responding to change over following a plan:**
Requirements change. Markets shift. Users discover they want something different once they see the first version. Agile teams embrace change instead of fighting it.

### The 12 Principles

Key principles behind the manifesto:
1. Deliver working software frequently (weeks, not months)
2. Welcome changing requirements, even late in development
3. Business people and developers work together daily
4. Build projects around motivated individuals  -  give them trust
5. Face-to-face conversation is the most efficient communication
6. Working software is the primary measure of progress
7. Agile processes promote sustainable development pace
8. Continuous attention to technical excellence enhances agility
9. Simplicity  -  the art of maximizing work NOT done
10. Self-organizing teams produce the best architectures and designs""",

# ────────────────────────────────────────────────
"Scrum Ceremonies": """## The 5 Scrum Events That Structure Your Sprint

Scrum is the most widely used Agile framework. It organizes work into time-boxed **Sprints** (usually 2 weeks), with five structured events that keep the team aligned and continuously improving.

### 1. Sprint Planning (Start of Sprint  -  ~4 hrs for 2-week sprint)

The team answers two questions:
- **What** will we deliver this sprint? (Sprint Goal)
- **How** will we build it? (Tasks breakdown)

```
Product Backlog → Sprint Backlog
(all desired features)   (what we commit to this sprint)

Team pulls items they can complete → estimates each task → creates Sprint Goal
```

### 2. Daily Standup / Daily Scrum (~15 minutes, every day)

Each team member answers three questions:
1. What did I complete **yesterday**?
2. What will I complete **today**?
3. What **blockers** do I have?

Key rules: Standing up keeps it short. No problem-solving during standup. Surface blockers, solve them separately.

### 3. Sprint Review (End of Sprint  -  ~2 hrs)

The team **demos working software** to stakeholders. Real users see real features. Feedback is gathered. The Product Backlog is updated based on what was learned.

> "Show don't tell"  -  working software only, no PowerPoint slides.

### 4. Sprint Retrospective (End of Sprint  -  ~1.5 hrs)

The team reflects on their **process** (not the product):
- What went **well**? (Keep doing)
- What went **poorly**? (Stop doing)
- What should we **try** next sprint? (Experiment)

This is continuous improvement in action  -  each sprint the team gets slightly better.

### 5. Backlog Refinement / Grooming (During Sprint  -  ~2 hrs/week)

The team and Product Owner review upcoming backlog items:
- Break large stories into smaller ones
- Estimate effort (story points or t-shirt sizes)
- Clarify requirements before sprint planning

### The Sprint Cycle

```
Sprint Planning → Daily Standups → Backlog Refinement → Sprint Review → Retrospective
                                                                              ↓
                                                                       Next Sprint Planning
```""",

# ────────────────────────────────────────────────
"Stages of a Product": """## From Idea to Scale  -  The Product Lifecycle

Every successful tech product passes through predictable stages. Understanding which stage your product is in determines your priorities, metrics, and strategy.

### Stage 1: Discovery / Problem-Solution Fit

**Goal:** Prove the problem is real and your solution makes sense.

Activities:
- Customer interviews (50+ conversations before writing code)
- Problem validation: "How do you currently solve this?"
- Hypothesis testing: "Would you pay for X?"
- Build nothing (or simple mockups)

**Key metric:** Interview quality, problem severity score

### Stage 2: MVP (Minimum Viable Product)

**Goal:** Build the smallest thing that delivers core value to early adopters.

Activities:
- Identify the ONE key value proposition
- Build in 4-8 weeks with minimal features
- Get 10-100 real users using it
- Measure: do they keep coming back?

**Key metric:** Activation rate, day-7 retention

> "If you're not embarrassed by v1, you launched too late."  -  Reid Hoffman

### Stage 3: Product-Market Fit

**Goal:** Find repeatable growth signal  -  users love it and tell others.

You've found PMF when:
- Retention curves flatten (users don't leave)
- Net Promoter Score (NPS) > 40
- "Very disappointed" if product disappeared: >40% of users

**Key metric:** Weekly Active Users (WAU), NPS, retention cohorts

### Stage 4: Growth / Scaling

**Goal:** Grow efficiently  -  lower CAC, increase LTV.

Activities:
- Optimize onboarding funnel
- Build referral loops
- Expand into new segments
- Hire sales and marketing

**Key metrics:** CAC, LTV, MRR growth rate, churn

### Stage 5: Maturity / Expansion

**Goal:** Maintain market position, expand revenue streams.

- New product lines
- International expansion
- Enterprise tier
- Acquisitions""",

# ────────────────────────────────────────────────
"What is a PRD?": """## Product Requirements Document  -  The Blueprint for Building

A **Product Requirements Document (PRD)** is a document that describes what you're building, who it's for, why it matters, and what success looks like. It aligns engineers, designers, and stakeholders before a single line of code is written.

### Why PRDs Matter

Without a PRD:
- Engineers build what they *think* is wanted
- Designers make decisions without business context
- Stakeholders have different expectations
- Teams argue about scope mid-development

### PRD Structure

```markdown
# Feature Name: [Student Progress Dashboard]

## Problem Statement
Students have no visibility into their learning progress across courses.
This leads to disengagement and 40% drop-off after lesson 3.

## User Story
As a student, I want to see my overall progress and daily streak
so that I feel motivated to continue learning.

## Goals
- Increase day-7 retention from 35% to 50%
- Reduce course drop-off at lesson 3 by 30%

## Non-Goals (What we are NOT building)
- Comparison with other students (privacy concerns)
- Detailed analytics (out of scope for v1)

## Requirements
### Must Have (P0)
- Overall course completion percentage
- Current streak (days of consecutive activity)
- Last 7 days activity heatmap

### Should Have (P1)
- Estimated time to completion
- Weekly goals

### Nice to Have (P2)
- Badges and achievements

## Success Metrics
- Primary: Day-7 retention rate
- Secondary: Average lessons completed per week

## Timeline
- Design: Week 1
- Engineering: Weeks 2-4
- QA: Week 5
- Launch: Week 6
```

### How to Write a Good PRD

1. **Start with the problem**, not the solution
2. **Include "Non-Goals"**  -  what you're explicitly NOT building prevents scope creep
3. **Prioritize ruthlessly**  -  use P0/P1/P2 or MoSCoW (Must/Should/Could/Won't)
4. **Define success metrics** before building
5. **Keep it short**  -  2 pages is better than 20""",

# ────────────────────────────────────────────────
"Launching to the World": """## Go-to-Market Strategy  -  Getting Your First Users

Building a great product is only half the battle. A **Go-to-Market (GTM) strategy** is your plan for reaching customers and driving adoption. Many great products fail not because of bad technology but because of poor GTM.

### The GTM Framework

**1. Define Your Target Customer**
```
Who is the primary buyer? → Student aged 18-30 in Nigeria
Job title / role?         → Undergraduate or recent graduate
Pain point?               → Can't afford coding bootcamps (₦2M+)
Where do they spend time? → Twitter, WhatsApp groups, YouTube
```

**2. Craft Your Value Proposition**
A single clear sentence: "We help [who] achieve [outcome] by [mechanism]."

Example: *"Digital Era helps Nigerian students become job-ready developers through bite-sized lessons and real project experience  -  at 1/20th the cost of a bootcamp."*

**3. Choose Your Channels**
| Channel | Best For | Cost |
|---|---|---|
| Content marketing (blog, YouTube) | Long-term organic | Low |
| Social media (Twitter, LinkedIn) | Community building | Low |
| WhatsApp/Telegram groups | Community targeting | Low |
| Google Ads | Intent-based demand | High |
| University partnerships | Large B2B deals | Medium |
| Influencer / KOL marketing | Rapid awareness | Medium |

**4. Acquisition → Activation → Retention**
- **Acquisition:** How users discover you (ads, referral, SEO)
- **Activation:** The "aha moment"  -  first real value delivered
- **Retention:** Why they come back (streaks, progress, community)

### Launch Types

- **Soft launch:** Release to a small group (beta users) for feedback before public
- **Hard launch:** Full public release with marketing push
- **Product Hunt launch:** Tech-savvy audience, good for developer tools
- **Press launch:** Reach mainstream audiences via news coverage""",

# ────────────────────────────────────────────────
"Funding Rounds": """## How Startups Raise Money

Most tech startups require external capital to grow faster than revenue alone allows. Venture Capital (VC) funding comes in stages, each aligned with the company's maturity and risk level.

### The Funding Stages

| Stage | Typical Amount | Who Invests | Milestone |
|---|---|---|---|
| **Pre-seed** | $50K-$500K | Friends, family, angels | Idea + team |
| **Seed** | $500K-$3M | Angel investors, seed VCs | MVP, early users |
| **Series A** | $3M-$15M | VC firms | Product-market fit |
| **Series B** | $15M-$60M | Growth VCs | Scaling proven model |
| **Series C+** | $60M+ | Late-stage VCs, PE | Expansion, pre-IPO |
| **IPO** | Varies | Public markets | Liquidity event |

### Key Terms to Know

**Valuation:** The company's worth at time of investment. A $10M post-money valuation after a $2M seed round means the company is worth $10M total (with $2M in the bank).

**Dilution:** Each funding round issues new shares, reducing existing shareholders' percentage. Founders typically retain 50-70% after seed, 20-40% at Series A.

**Term Sheet:** A non-binding document outlining the key terms of the investment (valuation, equity percentage, board seats, anti-dilution provisions).

**SAFE (Simple Agreement for Future Equity):** A popular instrument for early-stage raises  -  investors give money now in exchange for the right to receive equity at the next priced round.

**Cap Table:** Spreadsheet showing who owns what percentage of the company.

### African/Nigerian Startup Ecosystem

Key investors active in Nigeria:
- **Techstars** (accelerator)
- **Y Combinator** (global  -  has funded many Nigerian startups)
- **Ventures Platform**, **CcHUB**, **Founders Factory Africa**
- **Local angel networks:** Lagos Angel Network

Recent notable raises: Paystack ($200M+), Flutterwave ($3B valuation), Moniepoint, Kuda Bank""",

# ────────────────────────────────────────────────
"Product-Market Fit (PMF)": """## The Most Important Milestone for Any Startup

**Product-Market Fit (PMF)** means your product satisfies a strong market demand. It's the point where your product "fits" the market so well that users adopt it enthusiastically and growth becomes easier. Before PMF, everything is expensive and difficult. After PMF, growth compounds.

### How to Measure PMF

**The Sean Ellis Test:**
Survey your users: "How would you feel if you could no longer use [product]?"
- Very disappointed: **>40%** = strong PMF signal
- Somewhat disappointed: 15-40% = approaching PMF
- Not disappointed: <15% = no PMF yet

**Retention Curves:**
Plot the percentage of users still active N days after signup:
```
Without PMF:           With PMF:
100%                   100%
 ↘                      ↘ 
  ↘                      ↘___________  (flattens!)
   ↘___↘___→ 0%         35%→→→→→→
```
If the curve flattens and doesn't reach 0%, you have retained users  -  a strong PMF signal.

**NPS (Net Promoter Score):**
"On a scale of 0-10, how likely are you to recommend us?"
- Promoters (9-10) - Detractors (0-6) = NPS
- NPS > 40 is excellent

### Finding PMF

PMF is not found by building more features  -  it's found by:
1. Talking to users relentlessly
2. Narrowing your target audience (niche down)
3. Identifying which users love you most  -  serve THEM
4. Removing features that complicate the core value

### When You Have PMF

Signs you've found it:
- Users get upset when you make changes
- Word-of-mouth brings new users without spending
- Press reaches out to cover you without being asked
- You're struggling to keep up with demand
- Customer success is flooded with support requests (good problem!)""",

# ────────────────────────────────────────────────
"Key Metrics (KPIs)": """## Measuring What Matters  -  Product Analytics

A **KPI (Key Performance Indicator)** is a measurable value that shows how effectively you're achieving a business objective. Tracking the right metrics keeps teams focused and helps identify problems before they become critical.

### The Pirate Metrics Framework (AARRR)

```
Acquisition  → How do users find you?
Activation   → Do users have a great first experience?
Retention    → Do they come back?
Revenue      → Do they pay?
Referral     → Do they tell others?
```

### Key Metrics by Category

**Acquisition:**
- **CAC (Customer Acquisition Cost):** Total marketing spend ÷ new customers. If you spend ₦500K and get 100 signups, CAC = ₦5,000.
- **Traffic:** Unique visitors, sessions, bounce rate
- **Conversion rate:** Visitors who sign up

**Activation:**
- **Activation rate:** % of signups who complete key first action (first lesson, first code run)
- **Time to first value:** How long until user gets the "aha moment"

**Retention:**
- **DAU/MAU ratio (stickiness):** Daily Active Users ÷ Monthly Active Users. >20% is good.
- **Day-1, Day-7, Day-30 retention:** % of users still active after N days
- **Churn rate:** % of users who stop using the product per period

**Revenue:**
- **MRR (Monthly Recurring Revenue):** Total monthly subscription revenue
- **ARR (Annual Recurring Revenue):** MRR × 12
- **LTV (Lifetime Value):** Average revenue per user over their entire relationship with you
- **LTV:CAC ratio:** Should be >3:1 for a healthy business

**Engagement:**
- **Lessons completed per week**
- **Streak length**
- **NPS (Net Promoter Score)**

### The North Star Metric

Every product should have ONE north star metric that captures core value:
- Airbnb: nights booked
- Spotify: time listened
- Digital Era: lessons completed per week""",
}

# ══════════════════════════════════════════════════
# UI/UX (14 lessons)
# ══════════════════════════════════════════════════
UI_THEORY = {

"The Color Wheel": """## Understanding Color Relationships

The **color wheel** is the foundation of color theory  -  a circular diagram that shows the relationships between colors. Understanding it lets you combine colors that work harmoniously together.

### Primary, Secondary, and Tertiary Colors

```
PRIMARY COLORS (cannot be mixed from other colors):
  Red, Yellow, Blue (traditional)
  Red, Green, Blue (light/digital  -  RGB)

SECONDARY COLORS (mix two primaries):
  Red + Yellow = Orange
  Yellow + Blue = Green
  Red + Blue = Purple/Violet

TERTIARY COLORS (mix primary + adjacent secondary):
  Red-Orange, Yellow-Orange, Yellow-Green,
  Blue-Green, Blue-Violet, Red-Violet
```

### Color Properties

Every color has three properties:
- **Hue:** The pure color itself (red, blue, green)
- **Saturation:** Intensity/purity. 100% saturation = vivid. 0% = gray.
- **Value/Lightness:** How light or dark. Add white (tint) or black (shade).

```css
/* HSL  -  Hue, Saturation, Lightness (best for design): */
hsl(210, 80%, 50%)    /* A vivid blue */
hsl(210, 80%, 80%)    /* A light blue (tint) */
hsl(210, 80%, 20%)    /* A dark blue (shade) */
hsl(210, 20%, 50%)    /* A muted blue (desaturated) */
```

### Warm vs Cool Colors

**Warm colors** (red, orange, yellow): Energetic, exciting, urgent  -  used for CTAs, notifications, sale badges.

**Cool colors** (blue, green, purple): Calm, trustworthy, professional  -  used for tech products, finance, healthcare.

### Reading Color Codes

```css
/* Three ways to write the same color: */
color: #3B82F6;              /* Hex */
color: rgb(59, 130, 246);    /* RGB */
color: hsl(217, 91%, 60%);   /* HSL  -  most designer-friendly */
```

### Digital Color Spaces

- **RGB**  -  for screens (Red, Green, Blue light)
- **CMYK**  -  for print (Cyan, Magenta, Yellow, Black ink)
- **HSL/HSB**  -  for design tools (more intuitive than RGB)""",

# ────────────────────────────────────────────────
"Color Psychology": """## How Colors Make People Feel

Colors trigger psychological and emotional responses. These associations are partly cultural, partly universal. As a designer, you choose colors deliberately to evoke specific feelings in your users.

### Color Meanings in Western/Global Digital Contexts

**Red 🔴**
- Emotions: Urgency, danger, excitement, passion, energy
- Used for: Error messages, sale badges, CTAs, notifications, stop signs
- Brands: Netflix, YouTube, Coca-Cola, Pinterest

**Orange 🟠**
- Emotions: Enthusiasm, creativity, warmth, affordability
- Used for: Calls-to-action, youth brands, food delivery
- Brands: Amazon, Fanta, Duolingo, Etsy

**Yellow 🟡**
- Emotions: Optimism, happiness, caution, attention
- Used for: Warning messages, highlights, budget/value messaging
- Brands: McDonald's, IKEA, Snapchat, DHL

**Green 🟢**
- Emotions: Success, nature, health, safety, money (in US/Europe)
- Used for: Success states, confirmation, eco-brands, finance
- Brands: WhatsApp, Spotify, Whole Foods, Cash App

**Blue 🔵**
- Emotions: Trust, reliability, calm, professionalism, technology
- Used for: Tech products, finance, social media, healthcare
- Brands: Facebook, Twitter/X, PayPal, Samsung, LinkedIn

**Purple 🟣**
- Emotions: Creativity, luxury, wisdom, spirituality
- Used for: Premium brands, beauty, education, creative tools
- Brands: Twitch, Cadbury, Hallmark

**Black ⚫**
- Emotions: Sophistication, power, luxury, mystery
- Used for: Luxury brands, premium tiers, dark mode
- Brands: Apple (accessories), Chanel, Nike

**White ⚪**
- Emotions: Clean, simple, minimal, pure
- Used for: Backgrounds, minimalist design, healthcare, clarity

### Application for Digital Era

- **Primary action (enroll, start lesson):** Vibrant CTA color  -  orange or electric blue
- **Progress/success states:** Green
- **Errors:** Red
- **Trust (payment, account):** Deep blue
- **Background:** Dark navy or white (depending on mode)""",

# ────────────────────────────────────────────────
"Color Harmonies": """## Building Color Palettes That Work Together

A **color harmony** is a combination of colors that are pleasing to the eye. Using a systematic approach to picking colors prevents random, clashing combinations.

### 6 Classic Color Harmonies

**1. Monochromatic  -  One Hue, Multiple Shades**
```
Base: Blue (hsl(220, 80%, 50%))
Light: hsl(220, 80%, 80%)
Dark:  hsl(220, 80%, 20%)
Muted: hsl(220, 30%, 50%)
```
✅ Sophisticated, cohesive, professional. Easy to get right.

**2. Complementary  -  Opposite Colors on the Wheel**
```
Blue (#3B82F6) + Orange (#F97316)
Red (#EF4444) + Green (#22C55E)
Purple (#A855F7) + Yellow (#EAB308)
```
✅ High contrast, vibrant. Use one color for primary, complementary for accent only.

**3. Analogous  -  Adjacent Colors**
```
Blue, Blue-Green, Green  (tech, calm, nature)
Red, Red-Orange, Orange  (energetic, warm)
```
✅ Natural, harmonious. Common in nature-inspired designs.

**4. Triadic  -  Three Equally Spaced Colors**
```
Red, Yellow, Blue  (primary colors  -  classic but bold)
Orange, Green, Purple
```
Use one dominant, one secondary, one accent.

**5. Split-Complementary  -  Safer Version of Complementary**
```
Blue (#3B82F6) + Yellow-Orange + Red-Orange
```
Less tension than full complementary, still vibrant.

**6. Tetradic/Square  -  Four Colors**
Complex  -  rarely needed for most digital products.

### Building a Product Color Palette

```css
:root {
    /* Primary brand color: */
    --color-primary: hsl(220, 80%, 55%);
    --color-primary-light: hsl(220, 80%, 75%);
    --color-primary-dark: hsl(220, 80%, 35%);
    
    /* Accent (complementary or triadic): */
    --color-accent: hsl(40, 90%, 55%);
    
    /* Semantic: */
    --color-success: hsl(145, 65%, 42%);
    --color-error: hsl(0, 75%, 55%);
    --color-warning: hsl(38, 92%, 50%);
    
    /* Neutrals: */
    --color-gray-100: hsl(220, 20%, 97%);
    --color-gray-500: hsl(220, 10%, 55%);
    --color-gray-900: hsl(220, 20%, 10%);
}
```""",

# ────────────────────────────────────────────────
"Serif vs. Sans-Serif": """## Choosing the Right Typeface

Typography is one of the most powerful design decisions you make  -  it communicates personality, tone, and professionalism before a user reads a single word.

### Typeface Categories

**Serif fonts**  -  have small decorative strokes (serifs) at the end of letterforms:
```
Examples: Georgia, Times New Roman, Playfair Display, Merriweather, Garamond

The word "Typography" in a serif font feels:
→ Traditional, authoritative, classic, literary
→ Good for: editorial, luxury brands, law firms, print-heavy designs
```

**Sans-serif fonts**  -  clean, without those extra strokes:
```
Examples: Inter, Roboto, Open Sans, Helvetica, Poppins, DM Sans

The word "Typography" in sans-serif feels:
→ Modern, clean, minimal, tech-forward, accessible
→ Good for: tech products, startups, apps, digital-first designs
```

**Monospace fonts**  -  each character takes equal width:
```
Examples: Fira Code, JetBrains Mono, Courier New, Source Code Pro
→ Good for: code editors, terminal output, technical content
```

**Display/Decorative fonts**  -  high personality, low readability at small sizes:
```
→ Good for: logos, headlines, one-off branding moments
→ NEVER use as body text
```

### Pairing Fonts

Most designs use 2 fonts maximum: one for headings, one for body text.

**Classic pairings:**
- Playfair Display (heading) + Source Sans Pro (body)  -  editorial, premium
- Inter (heading) + Inter (body)  -  modern, minimal, tech
- Poppins (heading) + Open Sans (body)  -  friendly, approachable
- DM Serif Display (heading) + DM Sans (body)  -  contemporary editorial

**Rule of thumb:** Pair a serif with a sans-serif, or use one font family with different weights.

### Loading Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
```

```css
body { font-family: 'Inter', sans-serif; }
h1, h2 { font-family: 'Playfair Display', serif; }
```""",

# ────────────────────────────────────────────────
"Hierarchy and Scale": """## Typography Hierarchy  -  Guiding the Eye

**Typographic hierarchy** is the visual organization of text so readers instinctively know what to read first, second, and third. Without hierarchy, everything competes for attention. With it, the eye flows naturally through your content.

### Creating Hierarchy with Type

The four main tools:
1. **Size**  -  biggest = most important
2. **Weight**  -  bold = more important
3. **Color**  -  darker or accented = draws attention
4. **Spacing**  -  more whitespace around = more prominent

### A Type Scale System

Using a consistent scale (like a musical scale) creates visual harmony:

```css
/* Type Scale (based on 1.25 ratio  -  "Major Third"): */
:root {
    --text-xs:   0.75rem;   /* 12px  -  captions, labels */
    --text-sm:   0.875rem;  /* 14px  -  secondary text */
    --text-base: 1rem;      /* 16px  -  body text (BASE) */
    --text-lg:   1.125rem;  /* 18px  -  lead text */
    --text-xl:   1.25rem;   /* 20px  -  card titles */
    --text-2xl:  1.5rem;    /* 24px  -  section headings */
    --text-3xl:  1.875rem;  /* 30px  -  page headings */
    --text-4xl:  2.25rem;   /* 36px  -  hero headings */
    --text-5xl:  3rem;      /* 48px  -  display headings */
}

/* Application: */
h1 { font-size: var(--text-4xl); font-weight: 700; line-height: 1.1; }
h2 { font-size: var(--text-3xl); font-weight: 600; line-height: 1.2; }
h3 { font-size: var(--text-2xl); font-weight: 600; }
h4 { font-size: var(--text-xl);  font-weight: 500; }
p  { font-size: var(--text-base); line-height: 1.6; }
small { font-size: var(--text-sm); color: #6b7280; }
```

### Readability Rules

**Line length (measure):** 45-75 characters per line is optimal. Too wide = tiring. Too narrow = choppy.
```css
.content { max-width: 65ch; }  /* 65 characters wide */
```

**Line height (leading):** 
- Body text: 1.5-1.7 (relaxed)
- Headings: 1.0-1.3 (tight)

**Letter spacing (tracking):**
- Body: 0 or slightly negative for large sizes
- Caps/labels: 0.05-0.1em (more open)

### Visual Example

```
LARGE BOLD HEADING (H1  -  first thing read)
--------------------------------------------
Subtitle or lead paragraph in slightly      
larger or bolder body text. (H2 or lead-in)

Regular body text at base size with comfortable
line height. This is where the main content
lives and must be easy to read. (body)

Caption or metadata in smaller, lighter text.
```""",

# ────────────────────────────────────────────────
"What is a Wireframe?": """## Sketching the Structure Before Designing

A **wireframe** is a low-fidelity visual representation of a screen's structure and layout. It shows WHERE elements go and HOW they're organized  -  without color, typography, or imagery. Think of it as an architect's floor plan: it defines the structure before the aesthetic.

### Why Wireframe?

1. **Speed**  -  A wireframe takes 30 minutes; a full design takes 3 days. Validate the structure cheaply first.
2. **Focus**  -  No color or style debates. Everyone focuses on structure and flow.
3. **Communication**  -  Engineers, designers, and PMs can align on layout before building.
4. **Iteration**  -  Easy to change a box in a wireframe vs. rebuilding a coded component.

### Wireframe Elements

```
┌────────────────────────────────────────┐
│  LOGO        Nav Links        [Button] │  ← Header
├────────────────────────────────────────┤
│  ████████████████  Title               │
│  ░░░░░░░░░░░░░░░░  Body text           │  ← Hero Section
│  [Primary CTA]  [Secondary CTA]        │
├────────────────────────────────────────┤
│  [Card]  [Card]  [Card]  [Card]        │  ← Feature Grid
├────────────────────────────────────────┤
│  Copyright   Links   Social            │  ← Footer
└────────────────────────────────────────┘

Legend:
████ = Image placeholder
░░░░ = Text placeholder
[  ] = Button
```

### What to Show in a Wireframe

✅ DO show:
- Page/screen layout and regions
- Navigation structure
- Content hierarchy (what's bigger = more important)
- Key interactive elements (buttons, inputs, links)
- Content groupings

❌ DON'T show:
- Colors (use gray shades only)
- Real images (use boxes or crossed boxes)
- Actual content (use lorem ipsum or "placeholder text")
- Fonts or styling

### Tools for Wireframing

- **Figma**  -  the industry standard (free for individuals)
- **Excalidraw**  -  quick, hand-drawn style (free, web-based)
- **Balsamiq**  -  purposely lo-fi look
- **Pen and paper**  -  fastest for early exploration
- **FigJam**  -  collaborative whiteboard""",

# ────────────────────────────────────────────────
"Fidelity Levels": """## Low, Mid, and High Fidelity  -  When to Use Each

**Fidelity** refers to how closely a design resembles the final product. Using the right fidelity at the right stage of design saves enormous time and prevents wasted effort.

### Low-Fidelity (Lo-Fi)

**What:** Rough sketches, no color, placeholder boxes for images, lorem ipsum text.
**When:** Early exploration, concept validation, user flow discussions.
**How long:** 30 minutes to 2 hours.

```
┌─────────────────┐
│ ████  LOGO      │
│ □ nav □ nav □   │
├─────────────────┤
│  ████████████   │
│  ░░░░ Title ░░  │
│  [Button]       │
└─────────────────┘
```

**Benefits:** Fast, easy to change, doesn't anchor people to visual details.
**Tools:** Paper, whiteboard, Excalidraw, Balsamiq.

### Mid-Fidelity (Mid-Fi)

**What:** More precise layout, actual content, realistic proportions, minimal color (gray scale).
**When:** After lo-fi validated structure. Showing to stakeholders for feedback on layout.
**How long:** 2-8 hours per screen.

**Benefits:** Specific enough to discuss content, fast enough to iterate.
**Tools:** Figma, Adobe XD, Sketch.

### High-Fidelity (Hi-Fi)

**What:** Pixel-perfect, full color, real typography, real images, micro-interactions defined.
**When:** After the structure and content are validated. Ready for developer handoff.
**How long:** 1-2 days per screen.

**Benefits:** Developers can build directly from this. Client approves the actual look.
**Tools:** Figma (primary), Adobe XD.

### The Design Process Flow

```
Paper sketch (Lo-fi)
      ↓ Validate structure
Figma wireframe (Mid-fi)
      ↓ Validate layout + content
Figma visual design (Hi-fi)
      ↓ Validate look + feel + brand
Interactive prototype
      ↓ User testing
Developer handoff + spec
```

**Common mistake:** Jumping straight to hi-fi without validating the structure first.""",

# ────────────────────────────────────────────────
"Qualitative vs. Quantitative": """## Two Types of User Research

To design products people love, you need to understand your users deeply. Research methods fall into two categories: **qualitative** (the "why") and **quantitative** (the "what" and "how many").

### Qualitative Research  -  The "Why"

Qualitative research explores motivations, feelings, behaviors, and mental models. Small samples (5-20 people) yield rich insights.

**Methods:**

**User Interviews**  -  1-on-1 conversations (30-60 min):
```
"Tell me about the last time you tried to learn to code."
"What made you give up?"
"What does your current learning look like?"
→ Reveals real pain points, language users use, unexpected needs
```

**Contextual Inquiry**  -  Observe users in their natural environment:
```
"Can you show me how you currently use this feature?"
→ Reveals what people DO (vs. what they SAY they do)
```

**Usability Testing**  -  Watch users try to complete tasks with your product:
```
"Please try to enroll in a course  -  think aloud as you go."
→ Reveals confusion points, broken flows, wrong assumptions
```

**Card Sorting**  -  Users organize content into groups:
```
→ Reveals users' mental models for navigation/information architecture
```

### Quantitative Research  -  The "What" and "How Many"

Quantitative research measures behavior at scale. Large samples (hundreds to millions).

**Analytics:** How many users drop off at step 3? What's the average session length?

**Surveys:** NPS score, satisfaction ratings (valid when N > 100)

**A/B Testing:** Show 50% of users version A, 50% version B  -  which converts better?

**Heatmaps (Hotjar, Clarity):** Where do users click? What do they scroll past?

### When to Use Each

| Situation | Use |
|---|---|
| "WHY do users abandon checkout?" | Qualitative (interviews, session recordings) |
| "HOW MANY users abandon checkout?" | Quantitative (analytics) |
| "Which button color converts better?" | Quantitative (A/B test) |
| "Is our onboarding confusing?" | Qualitative (usability test) |

Best practice: Start with qualitative to understand the problem, use quantitative to measure the solution's effectiveness.""",

# ────────────────────────────────────────────────
"Interactive Mockups": """## Turning Static Designs into Clickable Prototypes

A **prototype** is an interactive simulation of your product  -  users can click, navigate, and interact with it  -  before a single line of code is written. This lets you test the user experience and validate design decisions cheaply.

### Types of Prototypes

**Paper Prototype:**
Physical cutouts of screens that a facilitator manually "advances" when a user clicks.
- Fastest, cheapest
- Great for early-stage flow testing

**Low-Fi Digital Prototype (Linked Wireframes):**
Wireframes connected with click targets so you can navigate between screens.
- Tools: Figma (connecting frames), InVision, Marvel
- Good for: Testing navigation and information architecture

**High-Fi Interactive Prototype:**
Full-color, pixel-perfect designs with animations and micro-interactions.
- Tools: Figma (primary), Principle, ProtoPie, Framer
- Good for: Usability testing, stakeholder demos, developer specs

### Building a Prototype in Figma

```
1. Design your screens as separate Frames
2. Select an element (button, link, nav item)
3. Switch to "Prototype" mode in right panel
4. Drag the blue connection handle to the destination frame
5. Choose interaction type:
   - On Click → Navigate to
   - On Hover → Show overlay
   - After delay → Navigate to
6. Press Play button (▶) to run the prototype
7. Share the link with users for testing
```

### What to Test with Prototypes

**Task-based testing:**
"Please try to [enroll in a Python course]  -  talk me through your thinking."

Watch for:
- Where do they hesitate or get confused?
- What do they expect to happen that doesn't?
- What do they say vs. what do they click?

**The 5-user rule (Jakob Nielsen):** Testing with just 5 users reveals ~85% of usability problems.

### Prototype Fidelity vs. Purpose

| Purpose | Fidelity Needed |
|---|---|
| Test navigation flow | Low  -  linked wireframes |
| Test copy and content | Low-Mid |
| Test visual design | High |
| Developer handoff | High + annotations |""",

# ────────────────────────────────────────────────
"Introduction to WCAG": """## Web Content Accessibility Guidelines

**WCAG (Web Content Accessibility Guidelines)** is the international standard for web accessibility, published by the W3C. It ensures that websites and apps are usable by people with disabilities  -  including visual, auditory, motor, and cognitive impairments.

### Why Accessibility Matters

1. **~15% of the world's population has some form of disability**
2. **Legal requirement** in many countries (ADA in US, EN 301 549 in Europe)
3. **Accessibility improves usability for everyone**  -  captions help in noisy environments; keyboard navigation helps power users
4. **SEO benefit**  -  semantic HTML and alt text improve search rankings

### WCAG Conformance Levels

- **Level A:** Minimum requirements (removing the most severe barriers)
- **Level AA:** Standard target for most websites (legally required in many jurisdictions)
- **Level AAA:** Highest level (not required for entire sites)

Most teams target **WCAG 2.1 AA**.

### The 4 WCAG Principles (POUR)

**1. Perceivable**  -  Information must be presentable to users in ways they can perceive.
- Alt text for all images
- Captions for video
- Sufficient color contrast
- Text resizable to 200% without breaking layout

**2. Operable**  -  Users must be able to navigate and use the interface.
- All functionality available via keyboard
- No content that flashes >3 times/second (seizure risk)
- Sufficient time to complete tasks

**3. Understandable**  -  Content and UI must be understandable.
- Clear, simple language
- Consistent navigation
- Error identification and suggestions

**4. Robust**  -  Content must be interpreted by a wide variety of assistive technologies.
- Valid semantic HTML
- ARIA labels where needed
- Tested with screen readers (NVDA, VoiceOver, JAWS)

### Quick Wins

```html
<!-- Alt text on all images: -->
<img src="course.jpg" alt="Student completing a Python coding exercise">

<!-- Descriptive link text (not "click here"): -->
<a href="/python">View Python courses</a>

<!-- Form labels linked to inputs: -->
<label for="email">Email address</label>
<input type="email" id="email" required>

<!-- Skip-to-main link: -->
<a href="#main-content" class="skip-link">Skip to main content</a>
```""",

# ────────────────────────────────────────────────
"Color Contrast": """## Making Text Readable for Everyone

**Color contrast** is the difference in luminance between foreground (text) and background colors. Insufficient contrast makes text unreadable for users with low vision, color blindness, or in bright sunlight.

### WCAG Contrast Requirements

| Content | Level AA | Level AAA |
|---|---|---|
| Normal text (< 18pt) | 4.5:1 | 7:1 |
| Large text (≥ 18pt or 14pt bold) | 3:1 | 4.5:1 |
| UI components, icons, charts | 3:1 |  -  |

The ratio is calculated from black (1:1 with itself) to white (21:1 with black). Higher ratio = more contrast.

### Examples

```
White text on dark blue #1e40af:  15.7:1 ✅ (Excellent)
Black text on white:              21:1   ✅ (Maximum)
Dark gray #374151 on white:       10.7:1 ✅ (Great)
Medium gray #6b7280 on white:     4.6:1  ✅ (Passes AA)
Light gray #9ca3af on white:      2.9:1  ❌ (Fails AA)
Yellow text on white:             1.1:1  ❌ (Unreadable)
```

### Common Accessibility Failures

```css
/* ❌ Fails  -  low contrast placeholder text: */
input::placeholder {
    color: #cccccc;   /* Too light on white background */
}

/* ✅ Fix: */
input::placeholder {
    color: #767676;   /* Minimum passing gray */
}

/* ❌ Fails  -  blue link on dark blue background: */
.nav-link { color: #60a5fa; background: #1d4ed8; } /* 1.7:1 */

/* ✅ Fix  -  white on dark blue: */
.nav-link { color: #ffffff; background: #1d4ed8; } /* 4.7:1 */
```

### Tools for Checking Contrast

- **WebAIM Contrast Checker**  -  webaim.org/resources/contrastchecker
- **Figma plugins**  -  "Contrast" by Stark, "A11y - Color Contrast Checker"
- **Chrome DevTools**  -  click any element, see contrast ratio in Styles panel
- **whocanuse.com**  -  see how your colors look to users with different vision types

### Don't Rely on Color Alone

Color alone cannot convey information  -  8% of men have some form of color vision deficiency (color blindness):

```html
<!-- ❌ Bad  -  only color distinguishes required fields: -->
<input style="border: 1px solid red">

<!-- ✅ Good  -  color + icon + text: -->
<input style="border: 2px solid red">
<span class="required-indicator" aria-label="required">*</span>
```""",

# ────────────────────────────────────────────────
"What is a Design System?": """## A Single Source of Truth for Design and Code

A **design system** is a collection of reusable components, guidelines, and principles that enables teams to build consistent, high-quality products faster. It's the bridge between design and engineering  -  both reference the same components and patterns.

### What a Design System Contains

```
Design System
├── Foundations
│   ├── Color Palette (primary, semantic, neutrals)
│   ├── Typography Scale (typefaces, sizes, weights)
│   ├── Spacing System (4px, 8px, 12px, 16px, 24px...)
│   ├── Border Radius, Shadows, Z-index scale
│   └── Motion/Animation principles
│
├── Components
│   ├── Button (primary, secondary, ghost, danger, sizes)
│   ├── Input, Textarea, Select, Checkbox, Radio
│   ├── Card, Modal, Tooltip, Toast/Alert
│   ├── Navigation (Navbar, Sidebar, Breadcrumb, Tabs)
│   └── Data display (Table, List, Badge, Progress)
│
├── Patterns
│   ├── Form validation patterns
│   ├── Empty states
│   ├── Loading states
│   └── Error states
│
└── Documentation
    ├── Usage guidelines for each component
    ├── Do's and Don'ts
    └── Accessibility notes
```

### Famous Design Systems

| Company | Design System | Public URL |
|---|---|---|
| Google | Material Design 3 | material.io |
| Apple | Human Interface Guidelines | developer.apple.com |
| IBM | Carbon Design System | carbondesignsystem.com |
| Shopify | Polaris | polaris.shopify.com |
| Atlassian | Design System | atlassian.design |
| Microsoft | Fluent UI | microsoft.com/design/fluent |

### Benefits

✅ **Consistency**  -  Every button, input, and modal looks the same across all screens  
✅ **Speed**  -  Engineers copy components instead of rebuilding from scratch  
✅ **Collaboration**  -  Designers and developers speak the same language  
✅ **Quality**  -  Accessibility, responsiveness built into components once, used everywhere  
✅ **Scalability**  -  Update one component, fix everywhere it's used""",

# ────────────────────────────────────────────────
"Data-Driven Design": """## A/B Testing  -  Making Design Decisions with Data

**A/B testing** (also called split testing) is a method of comparing two versions of a design to determine which performs better. Instead of debating opinions, you let real user behavior decide.

### How A/B Testing Works

```
Traffic → Route 50% to Version A → Measure conversions
        → Route 50% to Version B → Measure conversions

Compare: Which version had a higher conversion rate?
```

**Example:**
- Version A: Green "Enroll Now" button
- Version B: Orange "Start Learning" button
- 1,000 users see each version
- Version A: 8.2% clicked → 82 clicks
- Version B: 11.5% clicked → 115 clicks
- Winner: Version B  -  40% improvement!

### What Can You Test?

- **Headlines and copy**  -  "Learn Python" vs. "Become a Python Developer"
- **CTA buttons**  -  text, color, size, placement
- **Images**  -  hero image A vs. hero image B
- **Pricing display**  -  monthly vs. annual pricing shown first
- **Form length**  -  5-field form vs. 3-field form
- **Page layout**  -  single column vs. two columns
- **Onboarding flows**  -  wizard-style vs. all-at-once

### Statistical Significance

Not every difference is real  -  it might be random chance. You need **statistical significance** (typically 95% confidence) before declaring a winner.

Rules of thumb:
- Minimum 100 conversions per variant before drawing conclusions
- Run tests for at least 1-2 full weeks (capture weekly patterns)
- Test ONE thing at a time (otherwise you don't know what caused the difference)

### A/B Testing Tools

- **Google Optimize** (free, integrates with Analytics)
- **Optimizely** (enterprise)
- **VWO** (Visual Website Optimizer)
- **Posthog** (open-source, self-hostable)

### After the Test

```
Winner determined → 
  Update design system → 
    Roll out to 100% → 
      Document learning → 
        Identify next test hypothesis
```""",

# ────────────────────────────────────────────────
"Micro-interactions": """## The Small Details That Make Big Differences

**Micro-interactions** are small, contained product moments that accomplish a single task. They're the subtle animations, visual responses, and feedback mechanisms that make your product feel alive, polished, and thoughtful.

### The Anatomy of a Micro-interaction

Every micro-interaction has four parts:
1. **Trigger**  -  What initiates it (user click, system event)
2. **Rules**  -  What happens during the interaction
3. **Feedback**  -  How users know it's happening
4. **Loops & Modes**  -  Does it repeat? What happens next?

### Examples of Micro-interactions

**Button press feedback:**
```css
.btn {
    transition: transform 0.1s ease, box-shadow 0.1s ease;
}
.btn:active {
    transform: scale(0.97);  /* Slight shrink  -  physical press feeling */
    box-shadow: none;
}
```

**Loading state:**
```
User clicks "Enroll" → Button becomes "Enrolling..." with spinner
                     → 2 seconds later: "Enrolled! ✓" with checkmark
                     → Redirect to course
```

**Form field validation:**
```
User types email → Field outline turns green when valid ✓
                 → Turns red with error message when invalid ✗
                 → Happens in real-time, not just on submit
```

**Like button (Twitter/Instagram style):**
```
User clicks heart → Heart bounces and fills red
                  → Particle effect bursts out
                  → Counter increments
                  → Second click: reverses with animation
```

**Notification badge:**
```
New message arrives → Badge pops in with spring animation
                    → Badge color pulses once
                    → Number increments
```

### Why Micro-interactions Matter

1. **Feedback**  -  Users know their action was registered
2. **Error prevention**  -  Validates in real-time before submission
3. **Delight**  -  Unexpected animations create positive moments
4. **Personality**  -  Micro-interactions express brand character
5. **Status**  -  Shows system state (loading, success, error)

### Principles

- **Fast**  -  Most micro-interactions should be 150-300ms (feels instantaneous but visible)
- **Purposeful**  -  Every animation communicates something
- **Reversible**  -  Users should feel in control
- **Accessible**  -  Provide non-animated alternatives (prefers-reduced-motion)""",
}

# ══════════════════════════════════════════════════
# GENERATIVE AI THEORY (9 lessons)
# ══════════════════════════════════════════════════
GEN_AI_THEORY = {

"Discriminative vs. Generative Models": """## Two Fundamentally Different Ways ML Models Think

All machine learning models can be broadly classified into two types: **discriminative** and **generative**. Understanding this distinction is the foundation for understanding modern AI.

### Discriminative Models  -  Learning Boundaries

A **discriminative model** learns to classify or predict by drawing decision boundaries between categories. It answers: "Given this input, which class does it belong to?"

```
Training data:
  (cat photo) → label: "cat"
  (dog photo) → label: "dog"

Discriminative model learns:
  "If the features look like THIS, it's a cat. If like THAT, it's a dog."

At inference:
  Input: new photo → Output: "cat" (probability 0.92)
```

**Examples:** Logistic Regression, Support Vector Machines, classic neural network classifiers, BERT (for classification tasks).

The model learns **P(label | input)**  -  the probability of the label given the input.

### Generative Models  -  Learning Distributions

A **generative model** learns the underlying structure and distribution of the training data itself. It answers: "How would new examples in this distribution look?"

```
Training data: thousands of real human faces

Generative model learns:
  "Faces have two eyes, a nose, a mouth. Eyes are usually above the nose.
   Skin has these textures. Light falls this way..."

At inference:
  Input: random noise → Output: a brand-new photorealistic face
  (that no human has ever seen before)
```

**Examples:** GANs, VAEs, Diffusion Models, GPT, Stable Diffusion.

The model learns **P(input)**  -  the probability distribution of the data itself.

### Key Comparison

| | Discriminative | Generative |
|---|---|---|
| **Learns** | Decision boundaries | Data distribution |
| **Can classify?** | ✅ Yes | ✅ Yes (indirectly) |
| **Can generate?** | ❌ No | ✅ Yes |
| **Examples** | CNNs, BERT classifiers | GPT, Stable Diffusion, DALL-E |
| **Training data needed** | Less | Much more |

### Why This Matters for Modern AI

The explosion of generative AI (ChatGPT, Midjourney, Sora) is entirely driven by breakthroughs in generative models  -  specifically **Transformers** and **Diffusion Models**  -  that can generate text, images, audio, and video indistinguishable from human-created content.""",

# ────────────────────────────────────────────────
"The Latent Space": """## The Hidden Representation Behind Generative AI

The **latent space** is an abstract, compressed representation of data that a neural network learns during training. It's the mathematical "world model" that generative AI lives in  -  and understanding it reveals how these models can generate, interpolate, and manipulate content.

### What is the Latent Space?

Imagine you want to represent all possible human faces. A face has millions of pixels, but most are redundant. The important variations are:
- Age (young ↔ old)
- Gender presentation
- Skin tone
- Hair color and style
- Facial expression
- Face shape

A **latent space** compresses this into a much smaller set of numbers (latent vectors) that capture these meaningful dimensions. A face with latent vector `[0.2, 0.8, 0.5, ...]` corresponds to a specific combination of these attributes.

### How Autoencoders Create Latent Spaces

```
Input Image (512×512px = 786,432 numbers)
      ↓ Encoder
Latent Vector [z] (128 numbers  -  compressed representation)
      ↓ Decoder
Reconstructed Image (512×512px)

The encoder learns to compress; the decoder learns to reconstruct.
```

### The Power of Latent Spaces

**Interpolation**  -  smoothly blend between two images:
```
Face A latent: [0.1, 0.9, 0.3, ...]
Face B latent: [0.7, 0.2, 0.8, ...]

Midpoint:      [0.4, 0.55, 0.55, ...] → A face that's a blend of A and B
```
This is how AI-generated morphing videos work.

**Arithmetic**  -  add/subtract concepts:
```
Famous equation in Word2Vec embedding space:
  King - Man + Woman ≈ Queen

In image space:
  Smiling face - neutral face + sad face ≈ sad face
```

**Editing**  -  change one attribute:
```
Young face → find "age" direction in latent space → add it → Old face
Daytime photo → find "night" direction → add → Nighttime photo
```

### In Diffusion Models

Stable Diffusion and DALL-E 3 work entirely in a compressed latent space:
1. Image is encoded to latent space (8x smaller than pixel space)
2. Noise is added/removed in latent space (much faster!)
3. The denoised latent is decoded back to pixels""",

# ────────────────────────────────────────────────
"Attention is All You Need": """## The Paper That Changed AI Forever

In 2017, researchers at Google published a paper titled **"Attention Is All You Need"** introducing the **Transformer** architecture. This single paper is arguably the most important AI paper of the 21st century  -  it's the foundation of GPT, BERT, T5, Claude, Gemini, and every major language model today.

### The Problem Before Transformers

Before Transformers, sequence models (like RNNs and LSTMs) processed text word by word, left to right. This had critical limitations:
1. **Sequential processing**  -  couldn't be parallelized → slow training
2. **Vanishing gradients**  -  struggled to remember long-range dependencies
3. "The cat that the dog that the man trained bit **was** fat."  -  relating "was" to "cat" across many words was hard.

### The Transformer Solution

The Transformer processes the **entire sequence at once** (parallel!) using a mechanism called **self-attention** that lets every word directly attend to every other word.

```
Input: "The bank by the river had steep banks."

Traditional RNN:  The → bank → by → the → river → ...
                  (must process sequentially, forgets early words)

Transformer:      Every word attends to every other word simultaneously!
                  "bank" can directly look at "river" to disambiguate
                  (financial bank vs. river bank)
```

### The Architecture

```
Input Embeddings + Positional Encoding
         ↓
[Multi-Head Self-Attention Layer] × N   ← The key innovation
         ↓
[Feed-Forward Network]
         ↓
[Layer Normalization]
         ↓
Output
```

### Why "Attention Is All You Need"

Previous architectures combined attention with RNNs. The paper's insight: you don't need RNNs at all! Pure attention + feed-forward layers are sufficient and massively more scalable.

**Impact:**
- GPT (2018) → GPT-2 → GPT-3 (175B params) → GPT-4 → ChatGPT
- BERT → all modern NLP
- ViT (Vision Transformers) → applied to images
- Sora → applied to video
- Transformers in protein folding (AlphaFold 2)""",

# ────────────────────────────────────────────────
"Self-Attention Mechanism": """## How Transformers Read Language

**Self-attention** is the mathematical operation that allows a Transformer to understand relationships between words  -  regardless of how far apart they are in the sequence. It's the heart of why language models understand context so well.

### The Core Idea

When processing a word, self-attention asks: "For understanding THIS word, how much should I focus on EVERY OTHER word in the sequence?"

```
Input: "The animal didn't cross the street because it was too tired."

When processing "it":
- "it" pays attention to: animal (0.72), street (0.08), tired (0.12), ...
- The model learns "it" refers to "animal" based on context!
```

### The Q, K, V Mechanism

Self-attention uses three learned matrices to transform each word:

- **Query (Q):** "What am I looking for?"  -  the word asking the question
- **Key (K):** "What do I contain?"  -  every word advertising what it has
- **Value (V):** "What information do I provide?"  -  actual content to retrieve

```python
# Simplified self-attention:
def attention(Q, K, V):
    # 1. Compute similarity scores: Q×K^T
    scores = Q @ K.transpose(-2, -1)
    
    # 2. Scale (prevents exploding gradients):
    scores = scores / sqrt(d_k)
    
    # 3. Softmax  -  convert scores to probabilities (sum to 1):
    weights = softmax(scores, dim=-1)
    # weights[i][j] = "how much word i should attend to word j"
    
    # 4. Weighted sum of values:
    output = weights @ V
    
    return output
```

### Multi-Head Attention

Instead of one attention mechanism, Transformers use multiple "heads" in parallel:

```
Each head learns different types of relationships:
- Head 1: Subject-verb relationships
- Head 2: Noun-adjective relationships  
- Head 3: Coreference (pronoun → noun)
- Head 4: Long-range dependencies
...
All 8-32 heads run in parallel, outputs are concatenated
```

This allows the model to simultaneously consider multiple aspects of meaning.

### Positional Encoding

Since self-attention is order-agnostic ("cat bites dog" = "dog bites cat" without position info), Transformers add **positional encodings**  -  sinusoidal signals that encode each word's position in the sequence.""",

# ────────────────────────────────────────────────
"Tokenization": """## How Language Models Read Text

Before an LLM can process text, it must convert it into a form the neural network understands  -  numbers. **Tokenization** is this process of splitting text into **tokens** and mapping each token to a number.

### What is a Token?

A token is not exactly a word  -  it's a subword unit. Common words become single tokens; rare words are split into multiple tokens.

```
Text: "ChatGPT is surprisingly good at poetry!"

Tokens (approximate):
["Chat", "G", "PT", " is", " surprisingly", " good", " at", " poetry", "!"]

Token IDs:
[9126, 38, 2898, 374, 15206, 1695, 520, 18429, 0]
```

### Why Subwords Instead of Words?

- **Vocabulary size:** Using full words would need millions of tokens (one per word in every language). Subwords keep vocabulary to ~50,000-100,000 tokens.
- **Unknown words:** "tokenization" can be split into ["token", "ization"] even if the full word wasn't in training data.
- **Languages:** Better handles morphologically rich languages (Arabic, Finnish) where words have many forms.

### Common Tokenization Algorithms

**Byte Pair Encoding (BPE)**  -  used by GPT models:
1. Start with individual characters
2. Merge the most frequent pair repeatedly
3. Repeat until vocabulary size reached

**WordPiece**  -  used by BERT:
Similar to BPE but merges based on likelihood, not frequency.

**SentencePiece**  -  used by T5, LLaMA:
Treats whitespace as a regular character. Language-agnostic.

### Practical Implications

```python
# Using tiktoken (OpenAI's tokenizer):
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer

text = "Hello, this is a test of tokenization."
tokens = enc.encode(text)
print(tokens)        # [9906, 11, 420, 374, 264, 1296, 315, 47058, 13]
print(len(tokens))   # 9 tokens

# Token counting matters for:
# - API cost (charged per token)
# - Context window limits (GPT-4: 128K tokens)
# - Prompt engineering efficiency
```

### The "Context Window"

An LLM can only process a limited number of tokens at once  -  its **context window**:
- GPT-3.5: 4K-16K tokens
- GPT-4 Turbo: 128K tokens (~96,000 words!)
- Claude 3: 200K tokens
- Gemini 1.5 Pro: 1M tokens""",

# ────────────────────────────────────────────────
"Pre-training vs. Fine-tuning": """## How LLMs Learn and Specialize

Modern LLMs are trained in multiple stages. Understanding pre-training vs. fine-tuning explains how a model goes from raw intelligence to a helpful assistant  -  and how you can adapt models for specific tasks.

### Stage 1: Pre-training  -  Building General Intelligence

The model is trained on an enormous corpus of text (internet, books, code, etc.) using **self-supervised learning**: predict the next token, given all previous tokens.

```
Training data: ~1 trillion tokens of text
               (Wikipedia, Common Crawl, GitHub, books...)

Task: Given "The capital of France is ___", predict "Paris"
      Given "def calculate_area(radius):\n    ___", predict "return"
      
No human labels needed! The text itself provides supervision.

Result: A model that has "read" vast amounts of human knowledge
        and can complete any text sequence.
```

**Scale:** GPT-3  -  175 billion parameters, 300 billion tokens. Costs millions of dollars.

### Stage 2: Supervised Fine-tuning (SFT)  -  Teaching Format

The pre-trained model is helpful but raw  -  it'll complete text but won't follow instructions. SFT trains on human-written (prompt, ideal response) pairs:

```
Training example:
  Prompt: "Explain quantum computing in simple terms."
  Response: "Quantum computing uses quantum mechanics to process..."

Thousands of such examples → model learns to be helpful and follow instructions
```

### Stage 3: RLHF  -  Teaching Values

**Reinforcement Learning from Human Feedback (RLHF):**
1. Generate multiple responses to prompts
2. Humans rank responses (A > B > C)
3. Train a **reward model** to predict human preferences
4. Fine-tune LLM to maximize reward model score

This is why ChatGPT is helpful, harmless, and honest.

### Fine-tuning for Your Use Case

You can fine-tune existing models for specific tasks:

```python
# Types of fine-tuning:
# Full fine-tuning  -  update all weights (expensive)
# LoRA  -  Low-Rank Adaptation (efficient, popular)
# QLoRA  -  Quantized LoRA (even more efficient)
# Prompt tuning  -  only train soft prompts

from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")
config = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"])
model = get_peft_model(model, config)
# Now fine-tune on your domain-specific data
```""",

# ────────────────────────────────────────────────
"The Forward and Reverse Process": """## How Diffusion Models Generate Images

**Diffusion models** (like Stable Diffusion, DALL-E 3, Midjourney) are the technology behind AI image generation. They work by learning to reverse a process of gradually adding noise to images.

### The Key Insight

It's easy to destroy an image (add noise). Can we learn to reverse that destruction?

```
Forward process (destroy): 
Clean photo → add noise → add more noise → add more → pure random noise
                                                        (looks like TV static)

Reverse process (create):
Pure random noise → remove some noise → remove more → ... → Clean image
                                                        (the generated image!)
```

### The Forward Process (Training Time)

```
Step 0:  [Clear photo of a cat]
Step 1:  [Slightly noisy cat] ← add small amount of Gaussian noise
Step 2:  [Noisier cat]        ← add more noise
...
Step 500: [Very noisy]
...
Step 1000: [Pure random noise] ← completely destroyed
```

The noise schedule is controlled  -  we know exactly how noisy each step is.

### The Reverse Process (The Model)

The neural network (a **U-Net** or **Transformer**) is trained to predict: "Given this noisy image at step T, what was the noise added? How do I denoise it slightly?"

```python
# At each step:
noisy_image_at_t = noisy_image_at_t_plus_1
predicted_noise = model(noisy_image_at_t, timestep=t, text_prompt=prompt)
cleaner_image = noisy_image_at_t - predicted_noise * step_size
```

### Text-to-Image: Conditioning

The magic of "generate a cat wearing a hat" is **text conditioning**:
1. Text prompt → CLIP text encoder → text embedding
2. At each denoising step, the U-Net sees BOTH the noisy image AND the text embedding
3. The model learns to denoise toward images that match the text description

### Why Latent Diffusion?

Working in pixel space is expensive (512×512 = 262K pixels). Stable Diffusion uses **Latent Diffusion**  -  it works in a compressed latent space (8x smaller):

```
Image → VAE Encoder → Latent (64×64×4) → Diffuse → Denoise → Latent → VAE Decoder → Image
```
This is 64x fewer operations per step  -  enables running on consumer GPUs.""",

# ────────────────────────────────────────────────
"Temporal Consistency in Video": """## The Challenge of Generating Consistent Video

Generating a single image is one problem. Generating a video  -  where each frame must look consistent with the last, objects must persist through motion, and the world must feel physically coherent  -  is dramatically harder.

### Why Video Generation is Hard

**Frame-to-frame consistency:**
- A character's hair shouldn't change color between frames
- A hand that disappears behind a pillar must reappear correctly
- The lighting must be consistent as subjects move

**Temporal coherence:**
- Motion must be smooth (no jitter or teleporting)
- Physics must look realistic (water flows, objects fall naturally)
- Camera motion must be consistent (slow pan stays slow)

**Long-range consistency:**
- A character introduced at second 0 must look the same at second 30
- Background elements must remain stable

### Approaches to Temporal Consistency

**1. Extend Image Diffusion Temporally**
Add temporal attention layers to image diffusion models (Stable Video Diffusion, AnimateDiff):
- Generate each frame conditioned on neighboring frames
- Temporal attention allows frames to "look at" adjacent frames

**2. 3D Video Diffusion**
Model video as a 3D volume (height × width × time):
- The model sees all frames simultaneously
- Natural way to enforce consistency

**3. Video Prediction / Autoregressive**
Generate frames sequentially, conditioning on previous frames:
- Used by some models for long-form generation
- Prone to error accumulation

### Sora (OpenAI)  -  The Current State of the Art

Sora uses a **Diffusion Transformer (DiT)** applied to spacetime patches of video. Instead of treating video as frames, it treats video as a 3D volume:

```
Video → Compress (VAE) → 3D Spacetime Patches
     → Add noise → DiT Transformer denoises → Reconstruct
```

Key insight: By operating on spacetime patches (not frames), the model naturally learns temporal relationships.""",

# ────────────────────────────────────────────────
"Multimodality": """## AI That Sees, Hears, and Speaks  -  All at Once

The frontier of AI is **multimodal**  -  models that process and generate multiple types of data: text, images, audio, video, and code. This mirrors how humans experience the world: we see, hear, read, and speak simultaneously.

### What is Multimodality?

A **unimodal** model works with one type of data (GPT-4 text-only, or Stable Diffusion image-only).

A **multimodal** model understands and/or generates multiple types:

```
Inputs it can understand:
  Text: "What's in this image?"
  Image: [photo of a crowded market]
  Audio: [voice recording]
  Video: [clip of someone coding]

Output it generates:
  Text: "This is a busy outdoor market with stalls selling..."
  Or: Image, Audio, Video (for generative models)
```

### Current Multimodal Models

| Model | Can Input | Can Generate |
|---|---|---|
| GPT-4o | Text, Image, Audio | Text, Audio |
| Gemini 1.5 Pro | Text, Image, Audio, Video, Code | Text |
| Claude 3.5 | Text, Image | Text |
| DALL-E 3 | Text | Image |
| Sora | Text, Image | Video |
| Gemini 2.0 Flash | Text, Image, Audio, Video | Text, Image, Audio |

### How Multimodal Models Work

The key challenge: how do you make a language model understand images?

**CLIP-based approach:**
1. Train a model to align text and image representations
2. Image encoder maps images to the same space as text
3. Language model can now "see" images as if they're text tokens

**Unified tokenization:**
```
Text token:  "cat" → token ID 5427
Image patch: [16×16 pixels] → visual token (learned representation)
Audio frame: [mel spectrogram chunk] → audio token

All fed into the same Transformer as a mixed sequence!
```

### The Future: Native Multimodality

GPT-4o and Gemini 2.0 represent "any-to-any" models:
- Input: any combination of text, image, audio
- Output: any combination of text, image, audio
- True real-time voice conversation with visual understanding
- This is the direction all frontier models are moving""",
}

# ══════════════════════════════════════════════════
# DATA STRUCTURES & ALGORITHMS (23 lessons)
# ══════════════════════════════════════════════════
DSA_THEORY = {

"Space Complexity": """## Measuring Memory Usage of Algorithms

**Space complexity** measures how much memory an algorithm uses relative to its input size. Just as time complexity tells you how long an algorithm takes, space complexity tells you how much RAM it needs.

### Two Types of Space

**Auxiliary Space:** Extra space used by the algorithm itself (not counting input).
**Total Space:** Auxiliary space + space for the input.

In most interviews, "space complexity" means **auxiliary space**.

### Common Space Complexities

**O(1)  -  Constant Space:**
```python
def sum_array(arr):
    total = 0          # Only one variable, regardless of input size
    for num in arr:
        total += num
    return total
# Memory: one int (total)  -  doesn't grow with input
```

**O(n)  -  Linear Space:**
```python
def copy_array(arr):
    result = []        # Creates a new array of same size as input
    for item in arr:
        result.append(item)
    return result
# Memory grows linearly with input size
```

**O(n)  -  Recursive Call Stack:**
```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)  # Each call adds a stack frame
# 5! creates 5 stack frames → O(n) space
```

**O(log n)  -  Binary Search (Iterative):**
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1   # Only a few variables
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1
# O(1) auxiliary space  -  no recursion, no extra arrays
```

**O(n²)  -  Quadratic:**
```python
def create_matrix(n):
    return [[0] * n for _ in range(n)]  # n×n matrix → n² elements
```

### Time-Space Tradeoffs

Often you can trade space for time or vice versa:

```python
# Approach 1: O(n²) time, O(1) space
def has_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: return True
    return False

# Approach 2: O(n) time, O(n) space (using a hash set)
def has_duplicate_fast(arr):
    seen = set()            # O(n) extra space
    for num in arr:
        if num in seen: return True  # O(1) lookup!
        seen.add(num)
    return False
```

Hash sets trade memory for speed  -  a fundamental tradeoff in CS.""",

# ────────────────────────────────────────────────
"Comparing Algorithms": """## Using Big O to Choose the Right Algorithm

Big O notation gives us a vocabulary for comparing algorithms. But knowing the notation isn't enough  -  you need to understand how to apply it to real choices.

### Practical Comparison

| Algorithm | Time | Space | Best For |
|---|---|---|---|
| Linear Search | O(n) | O(1) | Small/unsorted data |
| Binary Search | O(log n) | O(1) | Sorted arrays |
| Hash Table Lookup | O(1) avg | O(n) | Fast lookups with memory |
| Bubble Sort | O(n²) | O(1) | Nearly sorted, tiny data |
| Merge Sort | O(n log n) | O(n) | General sorting, stable |
| Quick Sort | O(n log n) avg | O(log n) | In-place, general |
| Counting Sort | O(n+k) | O(k) | Integer keys, small range |

### Real Example: Finding Duplicates

```python
# Problem: Given a list of integers, do any appear twice?
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Approach 1: Nested loops  -  O(n²) time, O(1) space
def has_dup_v1(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: return True
    return False

# Approach 2: Sort then check neighbors  -  O(n log n) time, O(1) or O(n) space
def has_dup_v2(nums):
    nums.sort()      # O(n log n)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: return True  # O(n)
    return False

# Approach 3: Hash set  -  O(n) time, O(n) space
def has_dup_v3(nums):
    seen = set()
    for n in nums:
        if n in seen: return True
        seen.add(n)
    return False

# n=10M: v1 takes ~50 billion ops. v3 takes ~10M. v3 wins!
```

### When O(n²) Beats O(n log n)

Constants matter! For small n, simpler algorithms often win:
```python
# Insertion sort is O(n²) but extremely fast for small arrays (< ~20 items)
# Python's built-in sort (Timsort) uses insertion sort for small subarrays!

import timeit
small = [5, 3, 1, 4, 2]   # n=5
# Insertion sort: maybe 10 operations
# Merge sort: 10*log(5) ≈ 23 operations + overhead
# Winner for small arrays: insertion sort!
```

### Rule of Thumb for Interviews

- n ≤ 20: O(2^n) or O(n!) is fine
- n ≤ 500: O(n²) is fine
- n ≤ 10,000: O(n log n) is needed
- n ≤ 10^6: O(n) is needed
- n ≤ 10^9: O(log n) or O(1) is needed""",

# ────────────────────────────────────────────────
"Best/Average/Worst Case": """## Three Scenarios for Every Algorithm

When analyzing an algorithm's performance, there are three important scenarios: the **best case**, **average case**, and **worst case**. Big O notation typically refers to the worst case  -  but understanding all three gives a complete picture.

### The Three Cases Explained

**Best Case (Ω  -  Omega notation):**
The minimum number of operations for the most favorable input.

**Average Case (Θ  -  Theta notation):**
The expected number of operations over all possible inputs.

**Worst Case (O  -  Big O notation):**
The maximum number of operations for the most unfavorable input.

### Linear Search Example

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [3, 7, 1, 9, 4, 6, 2, 8]
```

- **Best case:** Target is the first element (1 comparison) → Ω(1)
- **Average case:** Target is in the middle (n/2 comparisons) → Θ(n)
- **Worst case:** Target is last or not present (n comparisons) → O(n)

### Quick Sort Example

```python
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]  # or arr[-1] for last-element pivot
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)
```

- **Best/Average case:** Pivot consistently divides array in half → O(n log n)
- **Worst case:** Pivot is always min or max (already sorted array with last-element pivot) → O(n²)

This is why randomizing the pivot is important!

```python
import random
def quicksort_safe(arr):
    if len(arr) <= 1: return arr
    pivot = arr[random.randint(0, len(arr)-1)]  # Random pivot
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_safe(left) + mid + quicksort_safe(right)
# Now worst case is extremely unlikely → average O(n log n)
```

### Why Worst Case Matters Most

For critical systems, you need to guarantee performance:
- Database query: Can't take 10 minutes for some inputs
- Real-time systems: Must respond within 50ms always
- Security applications: Worst-case timing must be predictable

This is why we usually quote worst-case Big O.""",

# ────────────────────────────────────────────────
"Amortized Analysis": """## The True Average Cost Over Time

**Amortized analysis** figures out the average cost per operation over a sequence of operations, even when individual operations vary wildly in cost. It's useful for data structures where occasional expensive operations are "paid for" by many cheap ones.

### The Classic Example: Dynamic Array (Python list)

Python lists automatically resize. When you `.append()` to a list, most of the time it's O(1). But occasionally, the array is full and must be resized  -  copying all n elements to a bigger array, which is O(n).

```python
import sys

lst = []
sizes = []
for i in range(1, 20):
    lst.append(i)
    sizes.append(sys.getsizeof(lst))

# sizes grows in jumps: 88, 120, 184, 184, 184, 216, 216, ...
# Python allocates extra capacity to avoid resizing every time!
```

The resizing strategy (doubling capacity each time):
```
Capacity 1 → 2 → 4 → 8 → 16 → 32 → ...

After n appends:
  Resize costs: 1 + 2 + 4 + 8 + ... + n/2 + n ≈ 2n total
  Regular costs: n × O(1) = n

Total cost: 3n
Per operation: 3n/n = 3 = O(1) amortized
```

So `append()` is O(1) amortized, even though individual resizes cost O(n).

### Stack with Pop-and-Push

```python
class AmorizedStack:
    def __init__(self):
        self.data = []
        self.trash = []
    
    def push(self, val):
        self.data.append(val)        # O(1)
    
    def pop(self):
        if not self.trash:
            while self.data:         # Move all to trash: O(n)
                self.trash.append(self.data.pop())
        return self.trash.pop()      # O(1) normally
    # Amortized: each element moved at most once → O(1) amortized pop!
```

### When to Use Amortized Analysis

Data structures designed for amortized O(1):
- `list.append()`  -  Python, Java ArrayList, C++ vector
- Hash table insertions (before resize)
- Binary counter (incrementing)
- Splay tree operations

Interview tip: When asked about `list.append()` time complexity, say "O(1) amortized"  -  this shows sophistication.""",

# ────────────────────────────────────────────────
"C Arrays": """## Raw Memory  -  How Data Actually Works

In C, arrays are the most fundamental data structure  -  a contiguous block of memory. Understanding C arrays illuminates what Python lists, JavaScript arrays, and all higher-level collections are built upon.

### Declaring Arrays in C

```c
#include <stdio.h>

// Fixed-size array  -  size must be known at compile time:
int grades[5] = {90, 85, 78, 92, 88};

// Size inferred from initializer:
double prices[] = {9.99, 14.99, 4.99};  // Length = 3

// Uninitialized (contains garbage values!):
char letters[26];

// Zero-initialized:
int zeros[10] = {0};
```

### Memory Layout

Arrays in C are laid out sequentially in memory:

```
int arr[5] = {10, 20, 30, 40, 50};

Memory address:  1000  1004  1008  1012  1016
Value:            10    20    30    40    50

arr[0] is at address 1000
arr[1] is at address 1004 (int = 4 bytes)
arr[2] is at address 1008
arr[i] is at address: base_address + i * sizeof(int)
```

This is why array access is O(1)  -  the address is calculated directly!

### Pointers and Arrays

In C, array names decay to pointers to the first element:

```c
int arr[] = {10, 20, 30, 40, 50};

int *ptr = arr;    // ptr points to arr[0]

printf("%d\n", arr[0]);   // 10
printf("%d\n", *ptr);     // 10  -  same thing!
printf("%d\n", ptr[2]);   // 30  -  pointer indexing!
printf("%d\n", *(ptr+2)); // 30  -  pointer arithmetic!

// Iterating with a pointer:
for (int *p = arr; p < arr + 5; p++) {
    printf("%d ", *p);
}
// 10 20 30 40 50
```

### Common C Array Pitfalls

```c
// 1. Buffer overflow  -  writing past the end:
int arr[5];
arr[10] = 99;  // UNDEFINED BEHAVIOR  -  corrupts memory!

// 2. No bounds checking:
int arr[5] = {1,2,3,4,5};
printf("%d\n", arr[5]);  // Reads garbage memory!

// 3. No length tracking:
// C arrays don't know their own length  -  you must track it manually
void print_array(int *arr, int length) {  // Must pass length separately!
    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
}
```

### Stack vs Heap Allocation

```c
// Stack-allocated (automatic, freed when function returns):
int stack_arr[100];  // 400 bytes on stack

// Heap-allocated (manual management):
int *heap_arr = malloc(100 * sizeof(int));  // 400 bytes on heap
// ... use the array ...
free(heap_arr);   // MUST free or you have a memory leak!
```""",

# ────────────────────────────────────────────────
"String Functions": """## Working with Strings in C

In C, a **string** is simply a null-terminated array of characters (`char[]`). There's no built-in String type. The `<string.h>` library provides essential string manipulation functions.

### C Strings  -  The Basics

```c
#include <stdio.h>
#include <string.h>

// A string literal:
char name[] = "Alice";
// Stored as: ['A', 'l', 'i', 'c', 'e', '\0']
// \0 (null terminator) marks the end of the string!

// Pointer to string:
char *greeting = "Hello";  // Points to read-only memory

// Check length:
printf("%zu\n", strlen(name));  // 5 (doesn't count \0)
```

### Essential String Functions (`<string.h>`)

```c
#include <string.h>

char src[] = "Hello, World!";
char dest[50];

// strlen  -  length of string (not counting \0):
size_t len = strlen(src);   // 13

// strcpy  -  copy string (UNSAFE  -  no bounds checking!):
strcpy(dest, src);          // dest = "Hello, World!"

// strncpy  -  safer copy with max length:
strncpy(dest, src, 49);    // Copy at most 49 chars
dest[49] = '\0';            // Always null-terminate!

// strcat  -  concatenate (UNSAFE):
char buf[50] = "Hello";
strcat(buf, ", World!");    // buf = "Hello, World!"

// strncat  -  safer concatenate:
strncat(buf, "!!!", 3);

// strcmp  -  compare strings (0 = equal, <0 = less, >0 = greater):
if (strcmp("apple", "banana") < 0) {
    printf("apple comes before banana\n");  // Prints this
}

// strstr  -  find substring:
char *pos = strstr("Hello, World!", "World");
if (pos) {
    printf("Found at position: %ld\n", pos - "Hello, World!");  // 7
}

// strchr  -  find first occurrence of a character:
char *excl = strchr("Hello!", '!');  // Points to '!'

// sprintf  -  format string into buffer:
char result[100];
sprintf(result, "Name: %s, Age: %d", "Alice", 25);
```

### Safer String Handling (Modern C)

```c
// snprintf  -  safe formatted output with max length:
char buf[20];
snprintf(buf, sizeof(buf), "Hello, %s!", "World");
// Never writes more than sizeof(buf) characters

// strtok  -  tokenize (split on delimiter):
char csv[] = "Alice,25,Lagos";
char *token = strtok(csv, ",");
while (token != NULL) {
    printf("%s\n", token);  // Alice, then 25, then Lagos
    token = strtok(NULL, ",");
}
```""",

# ────────────────────────────────────────────────
"2D Arrays": """## Grid Data  -  Matrices and Tables

A **2D array** is an array of arrays  -  organized as rows and columns. It's the foundational data structure for representing matrices, game boards, images, spreadsheets, and any grid-based data.

### Declaring 2D Arrays in C/Python

```c
// C  -  fixed-size 2D array:
int matrix[3][4];  // 3 rows, 4 columns

int grid[3][3] = {
    {1, 2, 3},    // Row 0
    {4, 5, 6},    // Row 1
    {7, 8, 9}     // Row 2
};

// Access: grid[row][column]
printf("%d\n", grid[1][2]);  // 6 (row 1, col 2)
```

```python
# Python  -  list of lists:
matrix = [
    [1, 2, 3],    # Row 0
    [4, 5, 6],    # Row 1
    [7, 8, 9]     # Row 2
]

print(matrix[1][2])   # 6

# Create a 3×4 matrix filled with zeros:
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]   # Correct!
# grid = [[0] * cols] * rows   # WRONG  -  rows share same list!
```

### Memory Layout (Row-Major Order)

```
grid[3][3] in memory (C, row-major):
[1][2][3][4][5][6][7][8][9]

grid[0][0] at offset 0
grid[0][1] at offset 1
grid[1][0] at offset 3  (cols per row)
grid[i][j] at offset: i * num_cols + j
```

### Common Operations

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(matrix)
cols = len(matrix[0])

# Traverse all elements:
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()  # Newline after each row

# Transpose (swap rows and cols):
transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
# [[1,4,7],[2,5,8],[3,6,9]]

# Using zip:
transposed = [list(row) for row in zip(*matrix)]

# Rotate 90 degrees clockwise:
rotated = [[matrix[rows-1-j][i] for j in range(rows)] for i in range(cols)]

# Sum of all elements:
total = sum(matrix[r][c] for r in range(rows) for c in range(cols))

# Row sums:
row_sums = [sum(row) for row in matrix]   # [6, 15, 24]
```

### Classic 2D Array Problems

```python
# Spiral traversal of a matrix
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)          # Take top row
        matrix = list(zip(*matrix))[::-1]  # Rotate remaining 90 degrees
    return result
```""",

# ────────────────────────────────────────────────
"String Manipulation": """## Classic String Problems and Techniques

String manipulation is one of the most common categories in coding interviews. Mastering these patterns makes you ready for LeetCode Easy/Medium and real interview questions.

### Reversing a String

```python
# Python  -  simplest:
s = "Hello, World!"
reversed_s = s[::-1]    # "!dlroW ,olleH"

# Without slicing:
def reverse(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1; right -= 1
    return ''.join(chars)
```

### Palindrome Check

```python
def is_palindrome(s):
    # Clean: lowercase, letters and digits only
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("race a car")                       # False
```

### Anagram Check

```python
from collections import Counter

def are_anagrams(s, t):
    return Counter(s) == Counter(t)
    # "listen" and "silent" → same character counts → True

# Without Counter:
def are_anagrams_v2(s, t):
    if len(s) != len(t): return False
    return sorted(s) == sorted(t)   # O(n log n)
```

### Sliding Window  -  Finding Substrings

```python
# Find the longest substring without repeating characters:
def length_of_longest_substring(s):
    char_index = {}   # char → most recent index
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1   # Shrink window
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

length_of_longest_substring("abcabcbb")  # 3 ("abc")
```

### Two Pointer Technique

```python
# Check if a string is a palindrome  -  O(n) time, O(1) space:
def is_palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    return True
```

### String Matching (KMP Preview)

```python
# Simple check  -  does pattern appear in text?
def contains(text, pattern):
    return pattern in text   # Python's built-in uses optimized algorithm

# All occurrences:
import re
positions = [m.start() for m in re.finditer('ab', 'abcababc')]
# [0, 3, 5]
```""",

# ────────────────────────────────────────────────
"Command Line Arguments": """## Accepting Input from the Terminal

Command-line arguments allow users to pass data to your program when they run it, without hardcoding values or using interactive input. Essential for scripting, automation, and building CLI tools.

### C  -  argc and argv

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // argc = argument COUNT (always >= 1, program name counts)
    // argv = argument VALUES as array of strings
    
    // argv[0] = program name ("./my_program")
    // argv[1] = first argument
    // argv[2] = second argument
    // ...
    
    printf("Program: %s\n", argv[0]);
    printf("Number of arguments: %d\n", argc - 1);
    
    for (int i = 1; i < argc; i++) {
        printf("arg[%d] = %s\n", i, argv[i]);
    }
    
    return 0;
}

// Run as: ./program hello world 42
// Output:
// Program: ./program
// Number of arguments: 3
// arg[1] = hello
// arg[2] = world
// arg[3] = 42
```

### Converting Arguments

```c
// Arguments are strings  -  convert as needed:
int age = atoi(argv[1]);          // String to integer
double price = atof(argv[2]);     // String to double

// Safer with strtol (detects errors):
char *endptr;
long n = strtol(argv[1], &endptr, 10);
if (*endptr != '\0') {
    fprintf(stderr, "Invalid number: %s\n", argv[1]);
    return 1;
}
```

### Python  -  sys.argv and argparse

```python
import sys

# sys.argv is a list of strings:
print(f"Script: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")

# Run as: python script.py --name Alice --age 25
# sys.argv = ['script.py', '--name', 'Alice', '--age', '25']

# Better  -  use argparse for real CLI tools:
import argparse

parser = argparse.ArgumentParser(description='Process student data')
parser.add_argument('name',          type=str,  help='Student name')
parser.add_argument('--gpa',        type=float, help='GPA', default=0.0)
parser.add_argument('--active',     action='store_true', help='Is active')
parser.add_argument('--courses',    nargs='+',  help='Course list')

args = parser.parse_args()

print(f"Name: {args.name}")
print(f"GPA: {args.gpa}")
print(f"Active: {args.active}")
print(f"Courses: {args.courses}")

# Run as: python script.py Alice --gpa 3.8 --active --courses Python SQL
```""",

# ────────────────────────────────────────────────
"Singly Linked List": """## Dynamic Node-Based Storage

A **linked list** is a data structure where each element (node) contains a value AND a pointer/reference to the next node. Unlike arrays, linked list elements don't need to be contiguous in memory  -  they can be scattered everywhere, connected by pointers.

### Structure

```
Array:        [10][20][30][40][50]     -  contiguous memory
Linked list:  10→20→30→40→50→None     -  scattered memory, connected by pointers

Node:
┌──────┬──────┐
│ data │ next │──→ (next node)
└──────┴──────┘
```

### Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add to end  -  O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:          # Traverse to end
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add to beginning  -  O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(' → '.join(map(str, elements)) + ' → None')
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count  # O(n)

ll = LinkedList()
ll.append(10); ll.append(20); ll.append(30)
ll.prepend(5)
ll.display()   # 5 → 10 → 20 → 30 → None
```

### Array vs Linked List

| Operation | Array | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(n) (shift) | O(1) |
| Insert at end | O(1) amortized | O(n) without tail ptr |
| Delete at beginning | O(n) (shift) | O(1) |
| Memory | Contiguous (cache-friendly) | Scattered (cache misses) |

**Use linked lists when:**
- Frequent insertions/deletions at the beginning
- Size is unknown and changes frequently
- No random access needed""",

# ────────────────────────────────────────────────
"Insert & Delete": """## Adding and Removing Nodes from a Linked List

Insertion and deletion are where linked lists truly shine  -  adding/removing from the beginning is O(1), versus O(n) for arrays.

### Insertion

```python
class LinkedList:
    # ... (Node class and head from before)
    
    def insert_after(self, prev_node, data):
        """Insert a new node after a given node  -  O(1) once you have the node"""
        if not prev_node:
            raise ValueError("Previous node must exist")
        new_node = Node(data)
        new_node.next = prev_node.next    # New node points where prev pointed
        prev_node.next = new_node          # Prev now points to new node
    
    def insert_at_position(self, pos, data):
        """Insert at specific position  -  O(n) to find position"""
        new_node = Node(data)
        
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(pos - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

# Visualization:
# Before:  A → B → C → None
# Insert X after B:
# Step 1: X.next = B.next (= C)
# Step 2: B.next = X
# After:   A → B → X → C → None
```

### Deletion

```python
    def delete_value(self, data):
        """Delete first node with given value  -  O(n)"""
        if not self.head:
            return
        
        # If head is the target:
        if self.head.data == data:
            self.head = self.head.next   # Just move head forward
            return
        
        # Traverse to find the node before target:
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Skip over the target
                return
            current = current.next
        # Not found  -  do nothing
    
    def delete_at_position(self, pos):
        """Delete node at given position  -  O(n)"""
        if not self.head:
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(pos - 1):
            if not current.next:
                raise IndexError("Position out of range")
            current = current.next
        
        current.next = current.next.next  # Skip deleted node

# Visualization:
# Before:  A → B → C → D → None
# Delete C:
# B.next = B.next.next (= D)
# After:   A → B → D → None
# (C is now unreferenced  -  garbage collected)
```""",

# ────────────────────────────────────────────────
"Reverse a Linked List": """## Classic Interview Problem  -  Multiple Approaches

Reversing a linked list is one of the most common interview questions. It tests your understanding of pointer manipulation and serves as a foundation for more complex linked list problems.

### The Problem

```
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None
```

### Iterative Solution  -  O(n) Time, O(1) Space

```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next   # Save next (we're about to overwrite it)
        current.next = prev        # Reverse the pointer!
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    
    return prev  # prev is now the new head

# Step-by-step trace for 1→2→3→None:
# Start:   prev=None, curr=1
# Step 1:  next=2, 1.next=None, prev=1, curr=2  →  None←1  2→3
# Step 2:  next=3, 2.next=1,   prev=2, curr=3  →  None←1←2  3→None
# Step 3:  next=None, 3.next=2, prev=3, curr=None  →  None←1←2←3
# Return:  prev=3  →  3→2→1→None ✓
```

### Recursive Solution  -  O(n) Time, O(n) Space (call stack)

```python
def reverse_list_recursive(head):
    # Base case: empty list or single node  -  already reversed
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list:
    new_head = reverse_list_recursive(head.next)
    
    # Make the next node point back to current:
    head.next.next = head
    head.next = None   # Current node is now the tail
    
    return new_head

# Trace for 1→2→3→None:
# recursive(1): calls recursive(2)
#   recursive(2): calls recursive(3)
#     recursive(3): returns 3 (base case)
#   Back in recursive(2): 3.next=2, 2.next=None → 3→2, new_head=3
# Back in recursive(1): 2.next=1, 1.next=None → 3→2→1, new_head=3
# Return 3 (new head)
```

### Reverse in Groups of K

```python
def reverse_k_group(head, k):
    """Reverse every K consecutive nodes."""
    count = 0
    node = head
    while node and count < k:
        node = node.next
        count += 1
    
    if count < k:   # Less than k nodes left  -  don't reverse
        return head
    
    new_head = reverse_list(head)  # reverse first k nodes
    head.next = reverse_k_group(node, k)  # Recurse on rest
    return new_head
```""",

# ────────────────────────────────────────────────
"Detect Cycle": """## Floyd's Cycle Detection Algorithm

A cycle in a linked list means a node's next pointer points back to a previously visited node  -  creating an infinite loop. Detecting this is a classic interview problem.

### Visual Representation

```
No cycle:         1 → 2 → 3 → 4 → None
With cycle:       1 → 2 → 3 → 4
                            ↑       ↓
                            6 ← 5
(Node 4's next points back to node 3  -  cycle!)
```

### Naive Approach  -  O(n) Space (Hash Set)

```python
def has_cycle_naive(head):
    visited = set()
    current = head
    while current:
        if id(current) in visited:   # We've seen this node before!
            return True
        visited.add(id(current))
        current = current.next
    return False
```

### Floyd's Tortoise and Hare  -  O(1) Space!

Use two pointers: **slow** (moves 1 step at a time) and **fast** (moves 2 steps). If there's a cycle, fast will eventually lap slow and they'll meet inside the cycle.

```python
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps
        
        if slow is fast:           # They met! Cycle exists!
            return True
    
    return False   # fast reached None  -  no cycle

# Why does it work?
# In a cycle of length C, if slow enters at position p,
# fast enters at position 2p (mod C).
# Relative speed of fast vs slow: 1 step per iteration.
# They'll meet after at most C iterations.
```

### Finding the Cycle Start

```python
def find_cycle_start(head):
    slow = fast = head
    
    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None   # No cycle
    
    # Phase 2: Find start of cycle
    # Mathematical proof: slow2 starting from head and slow
    # starting from meeting point both reach cycle start simultaneously
    slow2 = head
    while slow2 is not slow:
        slow2 = slow2.next
        slow = slow.next
    
    return slow   # Cycle start node
```""",

# ────────────────────────────────────────────────
"Merge Two Sorted Lists": """## Combining Sorted Linked Lists

Merging two sorted linked lists is a fundamental operation used in **merge sort** and a common interview problem. The key insight: compare heads, take the smaller one, recurse/iterate.

### The Problem

```
List 1: 1 → 3 → 5 → 7 → None
List 2: 2 → 4 → 6 → None

Result: 1 → 2 → 3 → 4 → 5 → 6 → 7 → None
```

### Iterative Solution  -  O(n+m) Time, O(1) Space

```python
def merge_sorted_lists(l1, l2):
    # Dummy head simplifies edge cases:
    dummy = Node(0)
    current = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1     # Take from l1
            l1 = l1.next
        else:
            current.next = l2     # Take from l2
            l2 = l2.next
        current = current.next
    
    # Append remaining nodes (one list is exhausted):
    current.next = l1 or l2
    
    return dummy.next   # Skip the dummy head

# Trace:
# l1=1→3→5, l2=2→4→6
# 1 < 2: take 1. dummy→1, l1=3→5, l2=2→4→6
# 3 > 2: take 2. dummy→1→2, l1=3→5, l2=4→6
# 3 < 4: take 3. dummy→1→2→3, l1=5→None, l2=4→6
# 5 > 4: take 4. dummy→1→2→3→4, l1=5→None, l2=6→None
# 5 < 6: take 5. dummy→1→2→3→4→5, l1=None, l2=6→None
# l1 exhausted: append l2 → dummy→1→2→3→4→5→6
```

### Recursive Solution  -  O(n+m) Time, O(n+m) Space (stack)

```python
def merge_recursive(l1, l2):
    # Base cases:
    if not l1: return l2
    if not l2: return l1
    
    if l1.data <= l2.data:
        l1.next = merge_recursive(l1.next, l2)  # l1 wins, attach rest
        return l1
    else:
        l2.next = merge_recursive(l1, l2.next)  # l2 wins, attach rest
        return l2
```

### Merge K Sorted Lists (Extended Problem)

```python
import heapq

def merge_k_sorted(lists):
    """Merge K sorted linked lists efficiently using a min-heap."""
    heap = []
    
    # Add head of each list to heap:
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.data, i, head))
    
    dummy = current = Node(0)
    while heap:
        val, i, node = heapq.heappop(heap)   # Get minimum
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.data, i, node.next))
    
    return dummy.next
# Time: O(N log k) where N = total nodes, k = number of lists
```""",

# ────────────────────────────────────────────────
"Stack (LIFO)": """## Last In, First Out Data Structure

A **stack** is a collection of elements with two primary operations: **push** (add to top) and **pop** (remove from top). The last element added is the first to be removed  -  like a stack of plates.

### Stack Visualization

```
Push 1, Push 2, Push 3:
    ┌───┐
    │ 3 │  ← Top (most recently added)
    ├───┤
    │ 2 │
    ├───┤
    │ 1 │
    └───┘

Pop → returns 3, stack becomes:
    ┌───┐
    │ 2 │  ← New top
    ├───┤
    │ 1 │
    └───┘
```

### Python Implementation

```python
# Python list works perfectly as a stack:
stack = []
stack.append(1)   # push
stack.append(2)
stack.append(3)
print(stack.pop())   # 3  -  LIFO!
print(stack.pop())   # 2
print(stack[-1])     # 1  -  peek (don't remove)
print(len(stack))    # 1

# Or use collections.deque for thread safety:
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.pop()    # 'b'
```

### Class-Based Implementation

```python
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)    # O(1) amortized
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()    # O(1)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]      # O(1)
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
```

### Classic Stack Applications

**1. Balanced Parentheses:**
```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

is_balanced("({[]})")   # True
is_balanced("([)]")     # False
```

**2. Undo Mechanism:** Push each action; pop to undo.

**3. Function Call Stack:** Every programming language uses a stack to track function calls and local variables.

**4. Depth-First Search (DFS):** Implement DFS iteratively using a stack.""",

# ────────────────────────────────────────────────
"Queue (FIFO)": """## First In, First Out Data Structure

A **queue** processes elements in the order they arrive  -  like a supermarket checkout line. The first element added is the first to be removed (FIFO).

### Queue Visualization

```
Enqueue 1, 2, 3:
Front → 1 | 2 | 3 ← Back

Dequeue → returns 1:
Front → 2 | 3 ← Back

Dequeue → returns 2:
Front → 3 ← Back
```

### Python Implementation

```python
# Use collections.deque  -  O(1) at both ends:
from collections import deque

queue = deque()
queue.append('Alice')      # enqueue (add to back)
queue.append('Bob')
queue.append('Carol')
print(queue.popleft())     # dequeue (remove from front): 'Alice'
print(queue[0])            # peek front: 'Bob' (no removal)
print(len(queue))          # 2

# Don't use list as queue! list.pop(0) is O(n)  -  shifts all elements
```

### Class-Based Queue

```python
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)       # O(1)  -  add to back
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()   # O(1)  -  remove from front
    
    def peek(self):
        return self._items[0]          # O(1)  -  see front without removing
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
```

### Priority Queue (Heap)

A **priority queue** dequeues the highest-priority item first (not FIFO):

```python
import heapq

pq = []
heapq.heappush(pq, (3, 'low priority task'))
heapq.heappush(pq, (1, 'high priority task'))
heapq.heappush(pq, (2, 'medium priority task'))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"{priority}: {task}")
# 1: high priority task
# 2: medium priority task
# 3: low priority task
```

### Queue Applications

- **BFS (Breadth-First Search):** Process nodes level by level using a queue
- **Task schedulers:** OS process scheduling (ready queue)
- **Print spooler:** Jobs printed in order received
- **Web server request handling:** Requests served in order
- **Message queues:** Kafka, RabbitMQ (system-level queues)""",

# ────────────────────────────────────────────────
"Binary Trees": """## Hierarchical Data Structure

A **binary tree** is a hierarchical structure where each node has at most two children  -  a **left** child and a **right** child. Trees model hierarchical relationships and enable efficient search, insertion, and many other operations.

### Tree Terminology

```
              10          ← Root (no parent)
            /    \
           5      15      ← Internal nodes
          / \    /  \
         3   7  12   20   ← Leaf nodes (no children)

Depth of node 7: 2 (edges from root)
Height of tree:  2 (max depth)
```

### Implementation

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the tree manually:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)
```

### Binary Search Tree (BST) Property

A **BST** has a special property: for every node, all values in the LEFT subtree are smaller, all in the RIGHT subtree are larger.

```python
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)
    
    def search(self, val):
        def _search(node, val):
            if not node: return False
            if val == node.val: return True
            if val < node.val: return _search(node.left, val)
            return _search(node.right, val)
        return _search(self.root, val)
```

### BST Operations  -  Time Complexity

| Operation | Average | Worst (unbalanced) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

Balanced BSTs (AVL, Red-Black trees) guarantee O(log n) always.""",

# ────────────────────────────────────────────────
"Tree Traversal": """## Visiting Every Node in the Right Order

**Tree traversal** is visiting every node in a tree exactly once. The order in which nodes are visited varies, and different orders are useful for different purposes.

### The Three DFS Orders

```
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

**Inorder (Left, Root, Right):** 4, 2, 5, 1, 6, 3, 7
→ For BST, gives nodes in sorted ascending order!

**Preorder (Root, Left, Right):** 1, 2, 4, 5, 3, 6, 7
→ Useful for copying a tree, serialization

**Postorder (Left, Right, Root):** 4, 5, 2, 6, 7, 3, 1
→ Useful for deleting a tree, calculating directory sizes

### Implementation

```python
def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Iterative inorder (using a stack):
def inorder_iterative(root):
    result, stack = [], []
    current = root
    while current or stack:
        while current:          # Go left as far as possible
            stack.append(current)
            current = current.left
        current = stack.pop()   # Process this node
        result.append(current.val)
        current = current.right  # Go right
    return result
```

### BFS / Level-Order Traversal

Visits nodes level by level, left to right:

```python
from collections import deque

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    
    while queue:
        level_size = len(queue)    # Process all nodes at current level
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    
    return result
# For our tree: [[1], [2, 3], [4, 5, 6, 7]]
```""",

# ────────────────────────────────────────────────
"Bubble Sort": """## The Classic Sorting Algorithm (and Why We Teach It)

**Bubble sort** repeatedly swaps adjacent elements that are in the wrong order. Larger elements "bubble up" to the end with each pass. It's one of the simplest sorting algorithms  -  and also one of the most inefficient for large datasets.

### How It Works

```
Array: [64, 34, 25, 12, 22, 11, 90]

Pass 1:
Compare 64 and 34 → swap: [34, 64, 25, 12, 22, 11, 90]
Compare 64 and 25 → swap: [34, 25, 64, 12, 22, 11, 90]
Compare 64 and 12 → swap: [34, 25, 12, 64, 22, 11, 90]
Compare 64 and 22 → swap: [34, 25, 12, 22, 64, 11, 90]
Compare 64 and 11 → swap: [34, 25, 12, 22, 11, 64, 90]
Compare 64 and 90 → no swap
After pass 1: 90 is in its final position ✓

... (continue for remaining elements)
```

### Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        if not swapped:   # Optimization: stop if no swaps in a pass
            break         # Array is already sorted!
    return arr

# Test:
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # [11, 12, 22, 25, 34, 64, 90]
```

### Performance

| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

### When to Use (and Not Use) Bubble Sort

✅ **Use for:**
- Educational purposes (simplest to understand)
- Very small arrays (n < 20, constants matter)
- Nearly sorted arrays (with the optimization above, it's O(n))

❌ **Never use for:**
- Large datasets  -  O(n²) is catastrophic for n > 10,000
- Production code  -  use Python's built-in `sorted()` (Timsort, O(n log n))

### Better Alternatives

```python
# Python's built-in  -  always use this in practice:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = sorted(arr)           # O(n log n)  -  Timsort
arr.sort()                         # In-place O(n log n)
```""",

# ────────────────────────────────────────────────
"Memoization": """## Remembering Past Work to Avoid Repetition

**Memoization** is an optimization technique that stores (caches) the results of expensive function calls and returns the cached result when the same inputs occur again. It's the top-down approach to dynamic programming.

### The Problem Without Memoization

```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# fib(5) call tree:
#              fib(5)
#            /        \
#        fib(4)       fib(3)
#        /    \       /    \
#    fib(3) fib(2) fib(2) fib(1)
#    ...
# fib(3) is computed MULTIPLE TIMES  -  exponential!
# Time: O(2^n)  -  fib(50) would take years
```

### With Memoization  -  Top-Down DP

```python
# Method 1: Manual dictionary cache
def fib_memo(n, cache={}):
    if n in cache: return cache[n]   # Already computed!
    if n <= 1: return n
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]
# Time: O(n)  -  each subproblem computed exactly once!

# Method 2: Python's @lru_cache decorator (cleanest)
from functools import lru_cache

@lru_cache(maxsize=None)   # Cache all results
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

fib(50)   # Instant! Returns 12586269025
```

### When to Apply Memoization

Look for these patterns:
1. **Recursive function** with overlapping subproblems
2. **Same inputs** called multiple times
3. **Pure function**  -  same input always gives same output

### Classic Memoization Problems

```python
# Coin change  -  minimum coins to make amount:
@lru_cache(maxsize=None)
def min_coins(amount, coins):
    if amount == 0: return 0
    if amount < 0: return float('inf')
    return 1 + min(min_coins(amount - c, coins) for c in coins)

min_coins(11, (1, 5, 6, 9))  # 2 (6+5 or 9+2×1)

# Longest Common Subsequence:
@lru_cache(maxsize=None)
def lcs(s1, s2):
    if not s1 or not s2: return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))

lcs("ABCBDAB", "BDCAB")  # 4 ("BCAB" or "BDAB")
```""",

# ────────────────────────────────────────────────
"Prefix Trees": """## Tries  -  Efficient String Retrieval

A **trie** (prefix tree) is a tree data structure used to store strings where each path from root to node represents a prefix. It enables extremely fast prefix-based searches  -  the foundation of autocomplete, spell checkers, and IP routing.

### Structure

```
Words: ["cat", "car", "card", "care", "dog"]

        (root)
       /      \
      c        d
      |        |
      a        o
     / \       |
    t   r      g
        |     (end)
       / \
      d   e
      |   |
    (end)(end)

Each path from root = a string or prefix
Marked nodes (end) = complete words
```

### Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char → TrieNode
        self.is_end = False   # Is this node the end of a word?

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word  -  O(m) where m = word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        """Does this exact word exist?  -  O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        """Does any word start with this prefix?  -  O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def autocomplete(self, prefix):
        """Return all words starting with prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children: return []
            node = node.children[char]
        
        results = []
        self._dfs(node, prefix, results)
        return results
    
    def _dfs(self, node, current, results):
        if node.is_end: results.append(current)
        for char, child in node.children.items():
            self._dfs(child, current + char, results)

trie = Trie()
for word in ["cat", "car", "card", "care", "dog"]:
    trie.insert(word)
print(trie.autocomplete("car"))   # ['car', 'card', 'care']
```""",

# ────────────────────────────────────────────────
"BFS vs DFS": """## Two Fundamental Graph Traversal Strategies

When exploring a graph or tree, there are two fundamental strategies: **Breadth-First Search (BFS)** explores level by level, and **Depth-First Search (DFS)** goes as deep as possible before backtracking. Choosing correctly is critical.

### Breadth-First Search (BFS)

Uses a **queue**. Explores all neighbors at distance 1 before exploring neighbors at distance 2.

```
Graph:    1
         /|\
        2 3 4
       /|   \
      5 6    7

BFS order: 1, 2, 3, 4, 5, 6, 7 (level by level)
```

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# BFS finds the SHORTEST PATH in unweighted graphs!
def shortest_path(graph, start, end):
    if start == end: return [start]
    visited = {start}
    queue = deque([[start]])   # Queue of paths
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]   # Found! Return the path
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None   # No path exists
```

### Depth-First Search (DFS)

Uses a **stack** (or recursion). Goes deep into one path before backtracking.

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    result = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph[node])  # Add neighbors
    return result
```

### When to Use Which

| Use BFS when... | Use DFS when... |
|---|---|
| Finding shortest path | Checking if path exists |
| Level-by-level processing | Detecting cycles |
| Social network distance | Topological sort |
| Web crawling (nearby pages first) | Maze solving |
| Memory: O(w) where w = width | Memory: O(h) where h = depth |

**BFS memory warning:** On wide graphs, BFS can use enormous memory (all nodes at one level). DFS uses memory proportional to the depth  -  better for deep graphs.""",
}


# ══════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════
if __name__ == "__main__":
    patch("tech_entrepreneurship.json", TECH_THEORY)
    patch("ui_ux.json",                UI_THEORY)
    patch("generative_theory.json",    GEN_AI_THEORY)
    patch("data_structures_algorithms.json", DSA_THEORY)
    print("\n\nBatch 2 complete!")
