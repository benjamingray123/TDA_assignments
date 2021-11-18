play = True

while play:
    exclamation = input('enter an exclamation! ')
    adverb = input('enter an adverb ')
    noun = input('enter a noun ')
    adjective = input('enter an adjective ')
    story = f'{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife.'
    print(story)
    if 'y' in input('play again? (y/n) ').lower():
        continue
    else:
        break 
