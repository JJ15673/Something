meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego",
    "OMG": "Wyrażenie zdziwienia lub zdumienia",
    "WTF": "Wyrażenie zdziwienia, zdumienia lub oburzenia",
    "BRB": "Be Right Back, chwila przerwy",
    "IDK": "I Don't Know, nie wiem",
    "AFK": "Away From Keyboard, nieobecny przy klawiaturze",
    
}
  
while True:
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("To słowo nie zostało odnalezione w naszej bibliotece :(")
