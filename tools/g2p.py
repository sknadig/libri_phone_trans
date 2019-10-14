import argparse

parser = argparse.ArgumentParser(description='G2P')
parser.add_argument('lexicon', type=str, help='an integer for the accumulator')
parser.add_argument('transcript', type=str, help='an integer for the accumulator')

args = parser.parse_args()

def read_lexicon(file_path):
    contents = open(file_path, "r").readlines()
    contents = [ele.strip().split(",") for ele in contents]
    g2p = {}
    for row in contents:
        g2p[row[0]] = row[1]
    return g2p

lex = read_lexicon(args.lexicon)
# print(lex)

def read_transcript(file_path):
    contents = open(file_path, "r").readlines()
    contents = [ele.strip().split(" ") for ele in contents]
    return contents

def substitute_word_phone(word):
    return g2p[word]

def process_transcript(transcript):
    new_transcript = []
    for row in transcript:
        new_sentence = []
        for word in row[1:]:
            try:
                new_sentence.append(lex[word])
            except:
                print(word)
        new_transcript.append([row[0], new_sentence])
    return new_transcript
    
transcripts = read_transcript(args.transcript)
new_trans = process_transcript(transcripts)
for row in new_trans:
    print(row[0] + " " + " <space> ".join(row[1]))