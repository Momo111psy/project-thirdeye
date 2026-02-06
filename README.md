# 💀 Project Thirdeye: The PM Devil's Advocate

> **A ruthless Manus Skill that roasts product ideas using Lenny's 300+ podcast transcripts to expose blind spots and failure modes before you ship.**

[![Manus Academy](https://img.shields.io/badge/Manus-Academy-blue)](https://campus.buildclub.ai)
[![Lenny's Challenge](https://img.shields.io/badge/Lenny's-Challenge-orange)](https://campus.buildclub.ai/challenges)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 What is Thirdeye?

Thirdeye is a **Manus Skill** that acts as your PM Devil's Advocate — a no-BS adversarial agent that forces you to **prove why you should build** instead of assuming you should.

Most AI assistants are yes-men that enable confirmation bias. Thirdeye is the antidote: it weaponizes expert insights from Lenny's Podcast archive to deliver brutal, citation-backed critiques that save you months of wasted effort.

### The Problem

**70-80% of new features fail** because teams skip discovery and jump straight to solutions. Confirmation bias, feature stacking, and buzzword-driven thinking doom products before they launch. Most AI tools make this worse by cheerleading bad ideas.

### The Solution

Thirdeye runs **automated pre-mortems** on your product ideas by:
1. Searching Lenny's podcast transcripts for relevant failure patterns
2. Identifying cognitive biases and strategic errors
3. Generating month-by-month failure timelines
4. Citing expert evidence from Shreyas Doshi, Marty Cagan, Teresa Torres, and 300+ other guests
5. Recommending concrete fixes or kill decisions

---

## 🔥 Demo: See Thirdeye in Action

**Input**: "Build an AI-powered gamified productivity app with social features — think Duolingo meets Strava meets TikTok dopamine loops for habits."

**Thirdeye Output**:

💀 **THE VERDICT**: Kill. Hard kill. This is "feature Frankenstein" meets "buzzword bingo" — a Hail Mary bet that confuses extrinsic motivation theater with actual behavior change.

📉 **THE TRAP**: Solution-in-Search-of-a-Problem + Feature Stacking Fallacy

💣 **THE PRE-MORTEM**: Here's how this dies in 12 months:
- Month 1-2: MVP ships, early adopters love the novelty, DAU spikes
- Month 3-4: Retention craters at 80% churn, users feel guilty about broken streaks
- Month 5-6: Pivot to "AI coaching," burn runway, CAC climbs to $40
- Month 10-12: Zombie app with 200 DAU, shut down or acqui-hire for $500K

🧠 **EXPERT EVIDENCE**:
- **Teresa Torres**: "Everything in our backlog is a bet. Discovery is helping us make a better bet." (Zero discovery = risky bet)
- **Marty Cagan**: Warns against feature teams that ship features without validating value
- **Shreyas Doshi**: Calls out "placebo productivity" — feeling productive without delivering leverage

🔧 **THE FIX**: KILL this version. Pick ONE habit domain, validate the opportunity with 20 user interviews, test assumptions before building.

[**Full roast →**](examples/roast-gamified-productivity.md)

---

## 📚 Example Roasts

See Thirdeye in action with these real roast examples:

### 1. AI-Powered Gamified All-in-One Habit App
**Idea**: "Build an AI-powered productivity app with gamification (streaks, badges, leaderboards) + social features. Think Duolingo meets Strava meets TikTok dopamine loops for tasks, meditation, reading, and fitness all in one place."

**Verdict**: Kill. Hard kill. Feature Frankenstein meets buzzword bingo.

**Key Citations**:
- Teresa Torres on jumping to solutions without discovery
- Marty Cagan on feature factory thinking
- Shreyas Doshi on placebo productivity

[**Read full roast →**](examples/roast-gamified-productivity.md)

### 2. AI Meeting Assistant (Otter + Fireflies + Reclaim Love Child)
**Idea**: "AI meeting assistant that auto-generates action items, summaries, suggests follow-up messages in Slack/Teams. Real-time listening, context understanding, sentiment analysis, calendar integration. Basically Otter.ai + Fireflies + Reclaim.ai love child, but with better AI and zero privacy concerns because enterprise-grade."

**Verdict**: Kill (or Pivot to 10x narrower). Tool worship meets symptom treatment.

**Key Citations**:
- Shreyas Doshi on high leverage vs positive ROI
- Teresa Torres on treating symptoms vs root causes
- Marty Cagan on tools don't fix culture

[**Read full roast →**](examples/roast-ai-meeting-assistant.md)

---

## 🚀 How It Works

Thirdeye is built as a **Manus Skill** — a modular capability that extends Manus's AI agent with specialized knowledge and workflows.

### Architecture

```
thirdeye/
├── SKILL.md                    # Roast protocol and instructions
└── references/                 # Expert transcript knowledge base
    ├── shreyas-doshi.md        # Product strategy, prioritization traps
    ├── marty-cagan.md          # Empowered teams, discovery vs delivery
    └── teresa-torres.md        # Continuous discovery, assumption testing
```

### Roast Protocol

1. **Load Expert Knowledge**: Grep transcripts for relevant failure patterns (gamification, social features, discovery, etc.)
2. **Generate Structured Roast**:
   - 💀 **Verdict**: Ship, Kill, or Pivot + brutal one-sentence judgment
   - 📉 **Trap**: Name the cognitive bias or strategic error
   - 💣 **Pre-Mortem**: Month-by-month failure timeline
   - 🧠 **Expert Evidence**: 3-5 citations from Lenny's archive
   - 🔧 **Fix or Kill**: Concrete next steps or kill rationale
3. **Deliver Actionable Critique**: No fluff, no cheerleading, just truth

---

## 📦 Installation

### Option 1: Use in Manus (Recommended)

1. Download the `.skill` file from [Releases](https://github.com/Momo111psy/project-thirdeye/releases)
2. In Manus, go to **Skills** → **Import Skill**
3. Upload the `.skill` file
4. Activate Thirdeye in your workspace

### Option 2: Install Manually

```bash
# Clone the repo
git clone https://github.com/Momo111psy/project-thirdeye.git

# Copy to Manus skills directory
cp -r project-thirdeye/thirdeye /home/ubuntu/skills/

# Validate the skill
python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py thirdeye
```

---

## 💡 Usage

Once installed, Thirdeye activates automatically when you:
- Ask Manus to "roast" or "stress-test" a product idea
- Request a pre-mortem analysis
- Ask "what could go wrong with this idea?"
- Want adversarial critique backed by expert evidence

### Example Prompts

```
"Roast this idea: Build a blockchain-based social network for pet owners"

"Run a pre-mortem on our plan to add gamification to our B2B SaaS product"

"What would Shreyas Doshi say about this feature roadmap?"

"Stress-test this: AI-powered meeting notes app with auto-summarization"
```

---

## 🏆 Built for Lenny's Newsletter Challenge

This project was created for the [Lenny's Newsletter Challenge](https://campus.buildclub.ai/challenges) (powered by Manus Academy), which challenges builders to create useful tools using Lenny's 300+ podcast transcripts.

### Why Thirdeye Wins

- **High Utility**: Saves PMs/founders months of wasted effort by killing bad ideas early
- **High Leverage**: Automates what normally requires senior advisors or painful team debates
- **Native to Manus**: Built as a proper Manus Skill, not a wrapper around external APIs
- **Citation-Backed**: Every roast references actual expert insights from Lenny's archive
- **Differentiated**: Only adversarial agent in the ecosystem — everything else is a yes-man

### Tech Stack

- **Manus**: Core agent platform and orchestration
- **Lenny's Transcripts**: 300+ episodes as knowledge base (Shreyas, Marty, Teresa, and more)
- **Manus Skills**: Modular architecture for reusability and community sharing

---

## 📚 Documentation

- [SKILL.md](thirdeye/SKILL.md) - Complete roast protocol and usage guide
- [Demo Roast](thirdeye_roast_demo.md) - Full example roast with citations
- [GitHub Audit](github_audit.md) - Profile cleanup notes

---

## 🤝 Contributing

Thirdeye is open to collaborators! Ways to contribute:

1. **Add more transcripts**: Expand the knowledge base with additional Lenny episodes
2. **Improve roast quality**: Refine the prompt engineering and citation logic
3. **Test on real ideas**: Submit product ideas to roast and share feedback
4. **Build integrations**: Connect Thirdeye to Slack, Notion, or other PM tools

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Lenny Rachitsky** for creating the podcast and making transcripts available
- **Shreyas Doshi, Marty Cagan, Teresa Torres** and all guests for their wisdom
- **Manus team** for building the agent platform that makes this possible
- **Build Club community** for the challenge and feedback

---

## 🔗 Links

- **Build Club Project**: [campus.buildclub.ai/projects/thirdeye](https://campus.buildclub.ai/projects/thirdeye)
- **Twitter**: [@BeyondtheFrame7](https://twitter.com/BeyondtheFrame7)
- **Lenny's Podcast**: [lennyspodcast.com](https://lennyspodcast.com)
- **Manus**: [manus.im](https://manus.im)

---

**Thirdeye sees what you're too close to see. Use it before you ship.** 💀
