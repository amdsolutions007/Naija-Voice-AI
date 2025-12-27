#!/usr/bin/env python3
"""
Naija-Voice-AI Translator Engine
Google Gemini-powered Nigerian Pidgin Translator
"""

import os
import sys
from typing import Optional

try:
    import google.generativeai as genai
except ImportError:
    print("❌ ERROR: google-generativeai not installed")
    print("Run: pip install google-generativeai")
    sys.exit(1)


class NaijaVoiceTranslator:
    """
    AI-powered translator for Nigerian Pidgin using Google Gemini
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize translator with Gemini API key
        
        Args:
            api_key: Google Gemini API key (reads from env if not provided)
        """
        # Read API key from environment variable or constructor parameter
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "❌ GEMINI_API_KEY not found. "
                "Provide via constructor or set environment variable: export GEMINI_API_KEY='your-key-here'"
            )
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        
        # Use Gemini 2.0 Flash model (latest stable)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        print("✅ Naija-Voice-AI initialized with Gemini 2.0 Flash")
    
    def translate_to_pidgin(self, text: str) -> str:
        """
        Translate English text to Nigerian Pidgin
        
        Args:
            text: English text to translate
            
        Returns:
            Nigerian Pidgin translation
        """
        if not text or not text.strip():
            return ""
        
        # Craft expert prompt for natural Pidgin translation
        prompt = f"""You are a Nigerian Pidgin expert and native speaker.

Translate this exact English text to natural, authentic Nigerian Pidgin:

"{text}"

IMPORTANT RULES:
1. Use natural Nigerian Pidgin expressions (e.g., "wetin dey happen" not "what is happening")
2. Maintain the original meaning and tone
3. Use common Pidgin words: "dey", "na", "wetin", "abi", "shey", "no be", "e don", etc.
4. Keep it conversational and natural (how Nigerians actually speak)
5. Don't explain - just provide the Pidgin translation
6. If the text is already Pidgin, return it unchanged

Translation:"""
        
        try:
            # Generate translation
            response = self.model.generate_content(prompt)
            
            # Extract translation
            translation = response.text.strip()
            
            # Remove quotes if Gemini added them
            if translation.startswith('"') and translation.endswith('"'):
                translation = translation[1:-1]
            
            return translation
            
        except Exception as e:
            error_msg = f"❌ Translation error: {str(e)}"
            print(error_msg, file=sys.stderr)
            return f"[ERROR: {str(e)}]"
    
    def translate_from_pidgin(self, pidgin_text: str) -> str:
        """
        Translate Nigerian Pidgin to English
        
        Args:
            pidgin_text: Nigerian Pidgin text to translate
            
        Returns:
            English translation
        """
        if not pidgin_text or not pidgin_text.strip():
            return ""
        
        prompt = f"""You are a Nigerian Pidgin expert.

Translate this Nigerian Pidgin text to clear, natural English:

"{pidgin_text}"

RULES:
1. Provide clear, fluent English translation
2. Maintain the original meaning and tone
3. Don't explain - just provide the English translation
4. If already English, return it unchanged

Translation:"""
        
        try:
            response = self.model.generate_content(prompt)
            translation = response.text.strip()
            
            # Remove quotes if added
            if translation.startswith('"') and translation.endswith('"'):
                translation = translation[1:-1]
            
            return translation
            
        except Exception as e:
            error_msg = f"❌ Translation error: {str(e)}"
            print(error_msg, file=sys.stderr)
            return f"[ERROR: {str(e)}]"
    
    def detect_language(self, text: str) -> str:
        """
        Detect if text is English or Nigerian Pidgin
        
        Args:
            text: Text to analyze
            
        Returns:
            'pidgin', 'english', or 'mixed'
        """
        prompt = f"""Analyze this text and determine if it's:
1. Nigerian Pidgin
2. English
3. Mixed (both Pidgin and English)

Text: "{text}"

Reply with ONLY ONE WORD: pidgin, english, or mixed"""
        
        try:
            response = self.model.generate_content(prompt)
            result = response.text.strip().lower()
            
            if 'pidgin' in result:
                return 'pidgin'
            elif 'english' in result:
                return 'english'
            elif 'mixed' in result:
                return 'mixed'
            else:
                return 'unknown'
                
        except Exception as e:
            print(f"❌ Detection error: {str(e)}", file=sys.stderr)
            return 'unknown'


# Example usage
if __name__ == "__main__":
    print("🇳🇬 Naija-Voice-AI Translator Engine")
    print("=" * 50)
    
    # Check for API key
    api_key = os.environ.get('GEMINI_API_KEY')
    
    if not api_key:
        print("\n❌ ERROR: GEMINI_API_KEY not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-key-here'")
        print("\nOr run app.py to paste the key interactively")
        sys.exit(1)
    
    # Initialize translator
    translator = NaijaVoiceTranslator(api_key)
    
    # Test translations
    print("\n🧪 TEST 1: English → Pidgin")
    english = "How are you doing today?"
    pidgin = translator.translate_to_pidgin(english)
    print(f"  English: {english}")
    print(f"  Pidgin:  {pidgin}")
    
    print("\n🧪 TEST 2: Pidgin → English")
    pidgin_text = "Wetin dey happen for Lagos today?"
    english = translator.translate_from_pidgin(pidgin_text)
    print(f"  Pidgin:  {pidgin_text}")
    print(f"  English: {english}")
    
    print("\n✅ Translator engine working!")
