import eng_to_ipa as ipa
import csv
# Reads the input conll file, in this case the ouput of the pragmatics script
# Conll file reader
def conll_read(file):
    #Reading a conll format file
    with open(file, "r", encoding="utf-8") as file:
        conll=file.readlines()
    print(f"Read {len(conll)} lines from the file.") 
    file.close()
    return conll

# Writes the output conll file, in this case the output of your function for adding the columns with phonetics info.
#Conll file writer
def conll_write(file, text):
    #Writing a file in conll format
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for sen in text:
            for dict in sen:
                f.write(dict["paragraph"] + " ")
                f.write(dict["sentence"] + " ")
                f.write(dict["id"] + " ")
                f.write(dict["word"] + " ")
                f.write(dict["lemma"] + " ")
                f.write(dict["upos"] + " ")
                f.write(dict["xpos"] + " ")
                f.write(dict["features"] + " ")
                f.write(dict["dependency"] + " ")
                f.write(dict["function"] + " ")
                f.write(dict["start_char"] + " ")
                f.write(dict["end_char"] + " ")
                f.write(dict["ner"] + " ")
                f.write(dict["tense"] + " ")
                f.write(dict["phrasalverb"] + " ")
                f.write(dict["irregularform"] + " ")
                f.write(dict["pragmatics"] + " ")
                f.write(dict["transcription"] + " ")
                # Write in csv format
                writer.writerow(dict["phonetic_contrast"]) 
                # Write in a string representation
                # f.write(repr(dict["phonetic_contrast"]) + "\n")
            f.write("\n")
    f.close()


# Write here your function to read the info of the text and add columns to it with the newly found phonetic information
def annotate_phonetics(conll):

    # Initializing variables to store sentence and whole text information for later
    whole_text=[] #Variable to return (whole text annotated)
    sentence_list=[] #Variable to save sentences individually

    #This chunk of code is for reading the info from the conll, column by column
    for line in conll:
        elements = line.split()
        if len(elements) > 0:
            paragraph=elements[0]
            sentence=elements[1]
            id=elements[2]
            word=elements[3]
            lemma=elements[4]
            upos=elements[5]
            xpos=elements[6]
            features=elements[7]
            dependency=elements[8]
            function=elements[9]
            start_char=elements[10]
            end_char=elements[11]
            ner=elements[12]
            tense=elements[13]
            phrasalverb=elements[14]
            irregularform=elements[15]
            pragmatics=elements[16]
           
            # Here I am initializing your two new columns with empty info (a hyphen "-")
            # Throughout this function, replace these two elements with the corresponding info of the word, which you may access from the variables above
            # Steven's code
            transcription= ipa.convert(word)
            
            # List of phonetic alphabets to check
            two_list = [ "eɪ", "eə", "ɪə", "əʊ", "eʊ", "aʊ", "ts", "dz", "tr", "dr", "ŋ*"]
            one_list = ["æ", "ɛ", "ʌ", "ɑ", "ɔ", "ɪ", "i", "ɜ", "ɒ", "u", "ʊ", "b", "p", "v", "f", "s", "z", "ʃ", "θ", "ð", "d", "t", "ʧ", "ʤ", "w", "g", "k", "h", "j", "n", "ŋ", "m", "l", "r"]
            vowels = ["ɑ","ɒ","æ","ɛ","i", "ɪ","ɔ","ʊ","u","ʌ","ə","o","a"]
            phonoCon = []
  
            i = 0 
            while i < len(transcription):
              if i + 1 < len(transcription):
                two_char = transcription[i:i+2]
                if two_char in two_list:
                  phonoCon.append(two_char)  
                  i += 2  
                  continue
    
              one_char = transcription[i]
              if one_char in one_list:
                if one_char in vowels and i-1 >= 0:
                    if transcription [i-1] not in vowels:
                      phonoCon.append(one_char)
                elif one_char in vowels and i-1 < 0:
                  phonoCon.append(one_char)
                elif one_char not in vowels:
                 phonoCon.append(one_char)

              i+= 1

            phonetic_contrast = phonoCon
            #Diccionari de features de cada linia per guardar a la llista de frase
            # Here I save all of the info of each sentence as a dictionary
            feature_dict = {"paragraph":paragraph,
                            "sentence":sentence,
                            "id":id,
                            "word":word,
                            "lemma":lemma,
                            "upos":upos,
                            "xpos":xpos,
                            "features":features,
                            "dependency":dependency,
                            "function":function,
                            "start_char":start_char,
                            "end_char":end_char,
                            "ner":ner,
                            "tense":tense,
                            "phrasalverb":phrasalverb,
                            "irregularform":irregularform,
                            "pragmatics":pragmatics,
                            "transcription":transcription,
                            "phonetic_contrast":phonetic_contrast
                            }
            
            #Appending the feature dictionary of every line to sentence info
            sentence_list.append(feature_dict)

        else: #Enters here every time there is a new sentence, chance to reset variables for checking sentence level stuff
                
            #Appending every sentence (but the last one) to the whole_text and resetting variables
            whole_text.append(sentence_list)
            sentence_list = []

    #Appending the very last sentence of the file
    whole_text.append(sentence_list)

    #Returning the annotated text
    return whole_text


def main():
    # Path to the output of the pragmatics file
    infile = "/Users/stevenzhou/Desktop/TaskGen/input/pragmatics.conll"
    outfile = "/Users/stevenzhou/Desktop/TaskGen/results/phonetics.conll"

    # Variable to store the sentences read from the input file
    conll = conll_read(infile)

    # Calling your function on the sentences and storing the new info
    text = annotate_phonetics(conll)

    # After calling your function, code here needs to be Writing the output conll file with all the phonetic information, so a file that is the same as the input file but with the two extra columns added.
    # Here you will need to make sure that the encoding allows you to store phonetic transcription symbols, I believe if you set the encoding to Unicode it should work
    #Write the output conll file
    conll_write(outfile, text)

main()