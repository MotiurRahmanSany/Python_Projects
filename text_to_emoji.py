def textToEmoji(sentence):
    emojis = {
        ':)' : '😃',
        ':(' : '😞',
        '>_<' : '😡',
        ':?' : '🤨',
        '>~<': '🤫',
        ':|': '😐️',
    }
    words = sentence.split();
    sentenceWithEmoji = ''
    for word in words:
        sentenceWithEmoji += emojis.get(word, word) + ' '
    
    return sentenceWithEmoji

