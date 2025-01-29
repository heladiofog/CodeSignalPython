# You are given two lists, sentences and words, each comprising n strings, where n ranges from # 1 to 100 inclusive. Each string in the sentences list has a length ranging from 1 to 500 inclusive. Each word in the words list is a single lowercase English alphabet word of length 1 to 10 inclusive.

# Your task is to find all instances of each word in the corresponding sentence from the sentences list and replace them with the reverse of the word. The words and sentences at the same index in their respective lists are deemed to correspond to each other.

# Return a new list comprising `n` strings, where each string is the sentence from the sentences list at the corresponding index, with all instances of the word from the words list at the same index replaced with its reverse.

# If the word is not found in the respective sentence, keep the sentence as it is.

# Remember, while replacing the instances of word in the sentence, you should preserve the case of the initial letter of the word. If a word starts with a capital letter in the sentence, its reversed form should also start with a capital letter.

# Example

# For sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] and words = ['simple', 'bond', 'e'], the output should be ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'].

def solution(sentences, words):
  # TODO: implement the solution
  pass

# Solution:
def solution(sentences, words):
  # TODO: implement the solution
  resulting_sentences = []
  
  for sentence, word in zip(sentences, words):
    sentence_words = sentence.split()
    resulting_sentence_words = []
    
    for sentence_word in sentence_words:
      if sentence_word.lower().find(word) != -1:
        # reversed_word = word[::-1] if sentence_word[0].islower() else word[len(word) - 1].upper() + word[::-1][1::]
        # Above line works but original word is trikcy because of lacking of specs regarding non-alpha chars
        if sentence_word[0].islower():
          reversed_word = word[::-1]
          original_word = word
        else:
          reversed_word = word[len(word) - 1].upper() + word[::-1][1::]
          original_word = word[0].upper() + word[1::]
        
        # replace the original word with the reversed word
        resulting_sentence_words.append(sentence_word.replace(original_word, reversed_word))
      else:
        resulting_sentence_words.append(sentence_word)
    
    resulting_sentences.append(' '.join(resulting_sentence_words))
  
  print(f"Resulting sentences: {resulting_sentences} replacing {words}")
  return resulting_sentences
  pass