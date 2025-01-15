import eng_to_ipa as ipa
text = "cap is big and cup is small"

# Convert English to IPA
text_IPA = ipa.convert(text)
print(text_IPA)

# Select phonetic contrasts
words = text.split()
dictionary = {word:ipa.convert(word) for word in words }
phonoCon = [(word, transcription) for word, transcription in dictionary.items() if 'æ' in transcription or 'ə' in transcription ]
print (phonoCon)

# æ	e ʌ	ɑː eɪ eə ɔː	ɪə ɪ iː	ɜː ɒ əʊ	uː eʊ aʊ ʊ 		
# b p v f s z ʃ θ ð d t tʃ dʒ w g k h j ts dz dʒ tr	dr n ŋ ŋk m l r		