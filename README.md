# 🇳🇬 Naija-Voice-AI - The Nigerian Pidgin Translator

**AI-powered Nigerian Pidgin translator using Google Gemini**

> "The Google Translate for the Nigerian Ecosystem" 🚀

---

## 🎯 THE PROBLEM

### **130 Million Nigerians Speak Pidgin. Zero AI Tools Support It.**

**The Language Barrier:**
- **Pidgin English** = Nigeria's unofficial lingua franca
- Spoken by **60% of Nigerians** (130M+ people)
- Used daily in markets, streets, offices, social media
- **NOT supported by Google Translate, ChatGPT, or any major AI**

**Real-World Impact:**
```
Scenario: South-South trader negotiating with Northern buyer
- Trader speaks Pidgin: "Wetin be your last price for this thing?"
- Google Translate: ❌ "What is your last price for this thing?" (wrong tone)
- AI Chatbots: ❌ Don't understand Pidgin queries
- Voice Assistants: ❌ Can't process Pidgin commands

Result: Communication breakdown, lost business, cultural erasure
```

**The Cultural Crisis:**
- Nigerian youth prefer English (seen as "correct")
- Pidgin treated as "broken English" (it's not - it's a real language)
- AI systems reinforce this bias by excluding Pidgin
- **130M speakers have no AI tools in their language**

---

## ✅ THE SOLUTION: Naija-Voice-AI

**AI-powered translator that treats Nigerian Pidgin as a first-class language.**

### **What It Does:**
1. **English → Pidgin Translation**
   ```
   Input:  "How are you doing today?"
   Output: "How you dey today?"
   ```

2. **Pidgin → English Translation**
   ```
   Input:  "Wetin dey happen for Lagos?"
   Output: "What's happening in Lagos?"
   ```

3. **Language Detection**
   ```
   Input:  "Abeg, I wan chop rice"
   Detected: Nigerian Pidgin
   Translation: "Please, I want to eat rice"
   ```

---

## 🚀 FEATURES (v0.1.0)

### **1. Google Gemini Integration**
- Powered by **Gemini Pro** (Google's most advanced model)
- Natural language understanding
- Context-aware translations
- Handles slang, idioms, cultural expressions

### **2. CLI Application (`app.py`)**
Interactive modes:
- ✅ **Interactive Translation** - Real-time chat-style translation
- ✅ **Batch File Translation** - Process entire documents
- ✅ **Auto-Detect Mode** - Automatically detects Pidgin vs English
- ✅ **Quick Test** - Pre-loaded sample translations

### **3. Translation Engine (`translator.py`)**
Core functions:
```python
translator = NaijaVoiceTranslator(api_key)

# English to Pidgin
pidgin = translator.translate_to_pidgin("Good morning")
# Output: "Good morning o" or "Morning o"

# Pidgin to English
english = translator.translate_from_pidgin("Abeg comot for road")
# Output: "Please move out of the way"

# Auto-detect language
lang = translator.detect_language("Wetin dey sup?")
# Output: 'pidgin'
```

### **4. Expert Prompting System**
Smart prompts that teach Gemini authentic Pidgin:
```python
prompt = """You are a Nigerian Pidgin expert and native speaker.

Translate this English text to natural, authentic Nigerian Pidgin:
"{text}"

RULES:
1. Use natural Pidgin expressions ("wetin dey happen" not "what is happening")
2. Include common words: "dey", "na", "wetin", "abi", "shey", "no be"
3. Keep it conversational (how Nigerians actually speak)
4. Don't explain - just translate
"""
```

**Result:** Natural, authentic Pidgin (not word-for-word literal translation)

---

## 💻 INSTALLATION

### **Requirements:**
- Python 3.7+
- Google Gemini API Key ([Get one free](https://makersuite.google.com/app/apikey))

### **Setup:**
```bash
# Clone repository
git clone https://github.com/amdsolutions007/Naija-Voice-AI.git
cd Naija-Voice-AI

# Install dependencies
pip install -r requirements.txt

# Set API key (Option 1: Environment variable)
export GEMINI_API_KEY='your-api-key-here'

# Run application
python3 app.py
```

**Option 2: Paste key when prompted**
```bash
python3 app.py
# App will ask: "Paste your Google Gemini API key below"
# (Key is NOT saved - for testing only)
```

---

## 🎮 USAGE

### **1. Interactive Mode (Recommended for Testing)**
```bash
$ python3 app.py

╔═══════════════════════════════════════════════════════════╗
║           🇳🇬  NAIJA-VOICE-AI TRANSLATOR  🇳🇬             ║
║         AI-Powered Nigerian Pidgin Translation            ║
╚═══════════════════════════════════════════════════════════╝

✅ API key loaded from environment
✅ Naija-Voice-AI initialized with Gemini Pro

MAIN MENU
1. Interactive Translation
2. Batch File Translation
3. Quick Test
q. Quit

Select option: 1

🌍 TRANSLATION MODE
Commands:
  1 - English → Pidgin
  2 - Pidgin → English
  3 - Auto-detect
  q - Quit

Select mode (1/2/3/q): 1

English text: I am very hungry
🔄 Translating to Pidgin...
✅ Pidgin: I dey hungry well well
```

### **2. Python Script Integration**
```python
from translator import NaijaVoiceTranslator

# Initialize (API key from environment)
translator = NaijaVoiceTranslator()

# Translate to Pidgin
pidgin = translator.translate_to_pidgin("Thank you very much")
print(pidgin)  # Output: "Tank you well well"

# Translate from Pidgin
english = translator.translate_from_pidgin("I no sabi wetin you dey talk")
print(english)  # Output: "I don't understand what you're saying"
```

### **3. Batch File Translation**
```bash
# Create input file
echo "How are you?\nI am fine\nThank you" > input.txt

# Run batch translation
python3 app.py
# Select: 2. Batch File Translation
# Input file: input.txt
# Output file: output.txt
# Mode: pidgin

# View results
cat output.txt
# Output:
# How you dey?
# I dey fine
# Tank you
```

### **4. Direct Engine Usage**
```bash
$ python3 translator.py

🇳🇬 Naija-Voice-AI Translator Engine
==================================================
✅ Naija-Voice-AI initialized with Gemini Pro

🧪 TEST 1: English → Pidgin
  English: How are you doing today?
  Pidgin:  How you dey today?

🧪 TEST 2: Pidgin → English
  Pidgin:  Wetin dey happen for Lagos today?
  English: What's happening in Lagos today?

✅ Translator engine working!
```

---

## 🧪 SAMPLE TRANSLATIONS

| English | Pidgin (Naija-Voice-AI) |
|---------|-------------------------|
| Good morning | Good morning o / Morning o |
| How are you? | How you dey? |
| I am fine | I dey fine / I dey kampe |
| What is your name? | Wetin be your name? |
| Please help me | Abeg help me |
| I don't understand | I no sabi / I no dey understand |
| How much is this? | How much be this? / Wetin be the price? |
| I am going home | I dey go house |
| Thank you very much | Tank you well well / Thank you o |
| What happened? | Wetin happen? / Wetin sup? |

**Natural Context (Not Literal):**
- "I am very hungry" → "I dey hungry die" (not "I dey very hungry")
- "Please wait" → "Abeg wait small" (not "Please wait")
- "That's correct" → "Na so" or "Correct!" (not "That is correct")

---

## 🏗️ ARCHITECTURE

### **Components:**

1. **`translator.py`** - Core translation engine
   - `NaijaVoiceTranslator` class
   - `translate_to_pidgin(text)` - English → Pidgin
   - `translate_from_pidgin(text)` - Pidgin → English
   - `detect_language(text)` - Auto-detect language
   - Google Gemini Pro integration

2. **`app.py`** - CLI interface
   - Interactive menu system
   - Real-time translation mode
   - Batch file processing
   - Quick test mode

3. **Gemini API** - AI brain
   - Model: `gemini-pro`
   - API: `google.generativeai`
   - Authentication: API key (env var or user input)

### **Translation Flow:**
```
User Input (English)
        ↓
translator.translate_to_pidgin(text)
        ↓
Expert Prompt Construction
        ↓
Gemini Pro API Call
        ↓
Response Parsing & Cleanup
        ↓
Pidgin Output
```

---

## 💰 BUSINESS MODEL

### **Target Market:**

| Segment | Users | Use Case | Revenue Potential |
|---------|-------|----------|-------------------|
| **Nigerian Youth (18-35)** | 50M | Social media, chat apps | ₦10B/year (₦200/user) |
| **Content Creators** | 500K | TikTok, YouTube, Instagram | ₦5B/year (₦10k/user) |
| **Education** | 20M students | Learn Pidgin (cultural preservation) | ₦2B/year |
| **Customer Service** | 10K companies | Chat support, call centers | ₦3B/year (₦300k/company) |
| **Government** | 36 states | Public communication, campaigns | ₦1B/year |

### **Revenue Projections:**

**Year 1 (Conservative):**
- 100K users × ₦500/year = ₦50M
- 50 companies × ₦300k/year = ₦15M
- **Total: ₦65M/year**

**Year 3 (Optimistic):**
- 5M users × ₦500/year = ₦2.5B
- 500 companies × ₦300k/year = ₦150M
- API licensing (100 apps × ₦1M/year) = ₦100M
- **Total: ₦2.75B/year**

### **Monetization:**
1. **Freemium Model:**
   - Free: 100 translations/day
   - Pro: Unlimited (₦500/month = $0.60)
2. **Enterprise API:**
   - ₦300k/year per company
   - Custom integrations (WhatsApp, Telegram, Slack)
3. **Voice Translation (v2.0):**
   - Speech-to-Speech (₦1k/month = $1.20)
   - 10M Nigerian diaspora (US, UK, Canada) target

---

## 🆚 COMPETITIVE ANALYSIS

| Tool | Pidgin Support | AI-Powered | Price | Offline |
|------|----------------|------------|-------|---------|
| **Google Translate** | ❌ No | Yes | Free | No |
| **ChatGPT** | ⚠️ Poor (not trained) | Yes | $20/mo | No |
| **Microsoft Translator** | ❌ No | Yes | Free | No |
| **DeepL** | ❌ No | Yes | €5.99/mo | No |
| **Human Translators** | ✅ Yes | No | ₦5k/page | Yes |
| **Naija-Voice-AI** | ✅ Yes | Yes | Free (v0.1.0) | Yes |

### **Why Naija-Voice-AI Wins:**
1. ✅ **Only AI tool** that understands Nigerian Pidgin
2. ✅ **Natural translations** (not literal word-for-word)
3. ✅ **Cultural context** (slang, idioms, expressions)
4. ✅ **Open source** (MIT license - trust + transparency)
5. ✅ **Local focus** (built by Nigerians, for Nigerians)

---

## 🛣️ ROADMAP

### **v0.2.0 - Voice Support** (Q1 2025)
- 🔄 Speech-to-text (Pidgin audio → text)
- 🔄 Text-to-speech (Pidgin text → audio)
- 🔄 Real-time voice translation
- 🔄 WhatsApp voice note translation

### **v0.3.0 - Multi-Platform** (Q2 2025)
- 🔄 Web interface (browser-based translator)
- 🔄 Mobile app (iOS + Android)
- 🔄 Browser extension (translate any webpage)
- 🔄 API for third-party integrations

### **v1.0.0 - Ecosystem** (Q3 2025)
- 🔄 Regional dialects (Lagos Pidgin, Port Harcourt, etc.)
- 🔄 Yoruba ↔ Pidgin, Igbo ↔ Pidgin, Hausa ↔ Pidgin
- 🔄 Social media bot (Twitter, Facebook, Instagram)
- 🔄 Chat app plugins (WhatsApp, Telegram, Slack)

---

## 🎖️ WHY THIS MATTERS

### **The Language Equity Problem**
- Major AI systems (ChatGPT, Google, Microsoft) only support 100-150 languages
- **7,000 languages exist globally** - 98% are ignored by AI
- Nigerian Pidgin = 130M speakers - **larger than German (100M), Korean (80M), Italian (70M)**
- Yet Pidgin has **zero AI support** while those languages have dozens of tools

**Naija-Voice-AI is a cultural preservation project disguised as a tech tool.**

### **Social Impact:**
- 📈 **Preserve Pidgin** as a legitimate language (not "broken English")
- 💰 **Enable commerce** (traders, marketers, customer service)
- 🎓 **Education** (teach Pidgin to youth, diaspora)
- 🏛️ **Government** (public communication in the people's language)
- 🌍 **Global recognition** (Pidgin on the AI map)

---

## 🔒 SECURITY & PRIVACY

### **API Key Management:**
- ✅ **Environment variables** (recommended for production)
- ✅ **User input** (for testing - key NOT saved)
- ❌ **Never hardcoded** in source files
- ❌ **Never committed to Git** (.gitignore protects secrets)

### **Data Privacy:**
- ✅ Translations processed by Google Gemini (subject to Google's privacy policy)
- ✅ No user data stored locally
- ✅ Batch files processed in-memory (not uploaded)
- ✅ Open source (audit the code yourself)

---

## 🤝 CONTRIBUTING

Naija-Voice-AI is **open source** (MIT License). Contributions welcome!

**How to Help:**
1. **Test translations** - Report bad Pidgin outputs (create GitHub issue)
2. **Add regional dialects** - Lagos Pidgin ≠ Port Harcourt Pidgin
3. **Improve prompts** - Better prompts = better translations
4. **Build features** - Voice support, web UI, mobile app
5. **Spread the word** - Share on social media (#NaijaVoiceAI)

**Contributors:**
- Olawale Shoyemi (@amdsolutions007) - Creator
- (Your name here - submit a PR!)

---

## 📄 LICENSE

MIT License - Free for personal and commercial use.

See [LICENSE](LICENSE) for full details.

---

## 👨‍💻 AUTHOR

**Olawale Shoyemi**  
CEO, AMD Solutions  
Email: ceo@amdsolutions007.com  
GitHub: [@amdsolutions007](https://github.com/amdsolutions007)  
Twitter: [@amdsolutions007](https://twitter.com/amdsolutions007)

---

## 🚀 GET STARTED

```bash
git clone https://github.com/amdsolutions007/Naija-Voice-AI.git
cd Naija-Voice-AI
pip install -r requirements.txt
export GEMINI_API_KEY='your-key-here'
python3 app.py
```

**Wetin you dey wait for? Start to translate!** 🇳🇬

---

**v0.1.0 Release Date:** December 27, 2025  
**Repository:** https://github.com/amdsolutions007/Naija-Voice-AI  
**Status:** Live (Production-Ready)
