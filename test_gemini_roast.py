#!/usr/bin/env python3.11
"""Test Thirdeye standalone system prompt with Gemini API"""

import os
from google import genai

# Read the system prompt
with open('/home/ubuntu/project-thirdeye/SYSTEM_PROMPT.md', 'r') as f:
    content = f.read()
    # Extract just the system prompt section
    start = content.find('You are **Thirdeye**')
    end = content.find('## END SYSTEM PROMPT')
    system_prompt = content[start:end].strip()

# Initialize Gemini client
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

# Test product idea
product_idea = """Build a Web3 loyalty program for coffee shops where customers earn NFT badges for purchases, trade them on a marketplace, and unlock exclusive perks. Think Starbucks Rewards meets OpenSea."""

# Generate roast
print("🔥 Testing Thirdeye Standalone System Prompt with Gemini...\n")
print("=" * 80)
print()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"{system_prompt}\n\nUSER: Roast this idea: {product_idea}",
    config={
        'temperature': 0.8,
        'max_output_tokens': 4096,
    }
)

roast_output = response.text

# Save to file
with open('/home/ubuntu/project-thirdeye/test_roast_gemini_llm.md', 'w') as f:
    f.write(f"# Test Roast #2: Standalone LLM Version (Gemini)\n\n")
    f.write(f"**Product Idea**: \"{product_idea}\"\n\n")
    f.write("---\n\n")
    f.write(roast_output)

print(roast_output)
print()
print("=" * 80)
print("\n✅ Roast saved to: test_roast_gemini_llm.md")
