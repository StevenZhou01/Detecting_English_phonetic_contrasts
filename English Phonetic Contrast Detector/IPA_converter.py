import eng_to_ipa as ipa
text = "The bear is holding a pear."

# Convert English to IPA
text_IPA = ipa.convert(text)
print(text_IPA)

# Select phonetic contrasts
words = text.split()
dictionary = {word:ipa.convert(word) for word in words }
phonoCon = [(word, transcription) for word, transcription in dictionary.items() if 'b' in transcription or 'p' in transcription ]
print (phonoCon)	
