#!/usr/bin/env python3
"""
Naija-Voice-AI CLI Application
Interactive Nigerian Pidgin Translator
"""

import os
import sys
from translator import NaijaVoiceTranslator


def print_banner():
    """Display welcome banner"""
    banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           🇳🇬  NAIJA-VOICE-AI TRANSLATOR  🇳🇬             ║
║                                                           ║
║         AI-Powered Nigerian Pidgin Translation            ║
║              Powered by Google Gemini                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
    print(banner)


def get_api_key():
    """
    Get Gemini API key from environment or user input
    
    Returns:
        API key string
    """
    # Check environment variable first
    api_key = os.environ.get('GEMINI_API_KEY')
    
    if api_key:
        print("✅ API key loaded from environment")
        return api_key
    
    # Prompt user to paste key
    print("\n🔑 Gemini API Key Required")
    print("=" * 50)
    print("Paste your Google Gemini API key below")
    print("(Key will not be saved - set GEMINI_API_KEY env var for persistence)")
    print()
    
    api_key = input("API Key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        sys.exit(1)
    
    return api_key


def translate_mode(translator: NaijaVoiceTranslator):
    """
    Interactive translation mode
    
    Args:
        translator: Initialized translator instance
    """
    print("\n" + "=" * 60)
    print("🌍 TRANSLATION MODE")
    print("=" * 60)
    print("\nCommands:")
    print("  1 - English → Pidgin")
    print("  2 - Pidgin → English")
    print("  3 - Auto-detect")
    print("  q - Quit")
    print()
    
    while True:
        print("\n" + "-" * 60)
        choice = input("\nSelect mode (1/2/3/q): ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Thanks for using Naija-Voice-AI!")
            break
        
        if choice not in ['1', '2', '3']:
            print("❌ Invalid choice. Try again.")
            continue
        
        # Get input text
        print()
        if choice == '1':
            text = input("English text: ").strip()
            if not text:
                continue
            print("\n🔄 Translating to Pidgin...")
            result = translator.translate_to_pidgin(text)
            print(f"\n✅ Pidgin: {result}")
        
        elif choice == '2':
            text = input("Pidgin text: ").strip()
            if not text:
                continue
            print("\n🔄 Translating to English...")
            result = translator.translate_from_pidgin(text)
            print(f"\n✅ English: {result}")
        
        elif choice == '3':
            text = input("Enter text (any language): ").strip()
            if not text:
                continue
            
            print("\n🔍 Detecting language...")
            lang = translator.detect_language(text)
            print(f"Detected: {lang.upper()}")
            
            if lang == 'english':
                print("\n🔄 Translating to Pidgin...")
                result = translator.translate_to_pidgin(text)
                print(f"\n✅ Pidgin: {result}")
            elif lang == 'pidgin':
                print("\n🔄 Translating to English...")
                result = translator.translate_from_pidgin(text)
                print(f"\n✅ English: {result}")
            else:
                print("\n⚠️  Language unclear. Choose mode 1 or 2 manually.")


def batch_mode(translator: NaijaVoiceTranslator):
    """
    Batch file translation mode
    
    Args:
        translator: Initialized translator instance
    """
    print("\n📁 BATCH MODE")
    print("=" * 60)
    
    input_file = input("Input file path: ").strip()
    
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return
    
    output_file = input("Output file path (default: output.txt): ").strip()
    if not output_file:
        output_file = "output.txt"
    
    mode = input("Translate to (pidgin/english): ").strip().lower()
    
    if mode not in ['pidgin', 'english']:
        print("❌ Invalid mode. Use 'pidgin' or 'english'")
        return
    
    print(f"\n🔄 Processing {input_file}...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        results = []
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                results.append("")
                continue
            
            print(f"  Translating line {i}/{len(lines)}...", end='\r')
            
            if mode == 'pidgin':
                translation = translator.translate_to_pidgin(line)
            else:
                translation = translator.translate_from_pidgin(line)
            
            results.append(translation)
        
        # Write results
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
        
        print(f"\n✅ Batch translation complete!")
        print(f"Output saved to: {output_file}")
        
    except Exception as e:
        print(f"\n❌ Batch processing error: {str(e)}")


def main():
    """Main application entry point"""
    print_banner()
    
    # Get API key
    api_key = get_api_key()
    
    # Initialize translator
    try:
        print("\n🔧 Initializing Gemini translator...")
        translator = NaijaVoiceTranslator(api_key)
        print("✅ Ready!")
    except Exception as e:
        print(f"\n❌ Initialization failed: {str(e)}")
        sys.exit(1)
    
    # Main menu
    while True:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1. Interactive Translation")
        print("2. Batch File Translation")
        print("3. Quick Test")
        print("q. Quit")
        print()
        
        choice = input("Select option: ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Goodbye!")
            break
        
        elif choice == '1':
            translate_mode(translator)
        
        elif choice == '2':
            batch_mode(translator)
        
        elif choice == '3':
            # Quick test
            print("\n🧪 QUICK TEST")
            print("=" * 60)
            
            test_sentences = [
                "Good morning, how are you?",
                "I am going to the market",
                "This food is very delicious"
            ]
            
            for sentence in test_sentences:
                pidgin = translator.translate_to_pidgin(sentence)
                print(f"\nEnglish: {sentence}")
                print(f"Pidgin:  {pidgin}")
        
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
