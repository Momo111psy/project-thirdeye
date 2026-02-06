# Contributing to Project Thirdeye

Thank you for your interest in contributing to Thirdeye! This document provides guidelines for contributing to the project.

## Ways to Contribute

### 1. Expand the Transcript Knowledge Base

The current version includes 3 high-signal episodes:
- Shreyas Doshi (Product Strategy)
- Marty Cagan (Empowered Teams)
- Teresa Torres (Continuous Discovery)

**How to add more**:
1. Identify relevant Lenny's Podcast episodes with strong PM/product insights
2. Download transcripts from [lennys-podcast-transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts)
3. Add to `thirdeye/references/` with descriptive filename (e.g., `april-dunford-positioning.md`)
4. Update `SKILL.md` to reference the new transcript in the "Load Expert Knowledge" section
5. Submit a PR with example roast showing the new transcript in action

### 2. Improve Roast Quality

**Prompt Engineering**:
- Refine the roast tone (ruthless but not cruel)
- Improve citation extraction logic
- Enhance pre-mortem timeline structure
- Add new roast categories (e.g., pricing strategy, go-to-market)

**How to contribute**:
1. Test Thirdeye on real product ideas
2. Document what works / what doesn't
3. Propose changes to `SKILL.md` with before/after examples
4. Submit PR with test cases

### 3. Test on Real Ideas

We need diverse product ideas to test Thirdeye's roast quality.

**Submit test cases**:
1. Create an issue with your product idea
2. Tag it with `test-case` label
3. Include context (industry, stage, target user)
4. We'll run Thirdeye and share the roast
5. Provide feedback on accuracy, usefulness, tone

### 4. Build Integrations

Thirdeye currently works within Manus. We'd love integrations with:
- **Slack**: `/roast [idea]` command
- **Notion**: Inline roast widget for product docs
- **Linear/Jira**: Pre-mortem automation for new epics
- **CLI tool**: Standalone roast engine

**How to contribute**:
1. Open an issue proposing the integration
2. Get feedback from maintainers
3. Build and test the integration
4. Submit PR with documentation

## Development Setup

### Prerequisites
- Manus account (free tier works)
- Access to Lenny's podcast transcripts
- Basic understanding of Manus Skills

### Local Setup

```bash
# Clone the repo
git clone https://github.com/Momo111psy/project-thirdeye.git
cd project-thirdeye

# Copy skill to Manus skills directory
cp -r thirdeye /home/ubuntu/skills/

# Validate the skill
python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py thirdeye
```

### Testing Changes

1. Edit `thirdeye/SKILL.md` or add transcripts to `thirdeye/references/`
2. Validate with the quick_validate script
3. Test in Manus by asking for a roast
4. Document results in your PR

## Submission Guidelines

### Pull Request Process

1. **Fork the repo** and create a feature branch
2. **Make your changes** following the guidelines above
3. **Test thoroughly** - include test cases in PR description
4. **Update documentation** - README, SKILL.md, or other docs as needed
5. **Submit PR** with clear description of changes and why they improve Thirdeye

### PR Template

```markdown
## Description
[What does this PR do?]

## Motivation
[Why is this change needed?]

## Testing
[How did you test this? Include example roasts if applicable]

## Screenshots/Examples
[If UI/output changes, show before/after]

## Checklist
- [ ] Tested locally in Manus
- [ ] Validated with quick_validate.py
- [ ] Updated documentation
- [ ] Added test cases
```

### Code Review

All PRs require:
- Passing validation (quick_validate.py)
- At least one example roast demonstrating the improvement
- Maintainer approval

## Community Guidelines

### Be Respectful
- Thirdeye roasts product ideas, not people
- Keep feedback constructive and evidence-based
- Respect diverse perspectives on product strategy

### Be Collaborative
- Ask questions if guidelines are unclear
- Help other contributors
- Share learnings from testing Thirdeye

### Be Transparent
- Disclose conflicts of interest (e.g., if you work for a competitor)
- Credit sources when adding transcripts or insights
- Document limitations of your contributions

## Questions?

- **GitHub Issues**: [project-thirdeye/issues](https://github.com/Momo111psy/project-thirdeye/issues)
- **Twitter**: [@BeyondtheFrame7](https://twitter.com/BeyondtheFrame7)
- **Build Club**: [campus.buildclub.ai/projects/thirdeye](https://campus.buildclub.ai/projects/thirdeye)

---

**Thank you for helping make Thirdeye better!** 💀
