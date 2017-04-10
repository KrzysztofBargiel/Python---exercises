slownik_AI = {}
print "Witaj, jestem sztuczna inteligencja ktora zna odpowiedzi na 99% pytan"
key = ""
answer = ""
stop ="koniec"
while stop.lower() not in slownik_AI or stop.lower() not in slownik_AI.values():
    key = (raw_input("Jakie jest Twoje pytanie\n")).lower().strip()
    if key == "koniec":
         print "Dziekuje, konczymy"
         break
    elif key in slownik_AI:
        print slownik_AI[key]
        continue
    else:
        answer = (raw_input("Uuuuu, nie kojarze, jaka powinna byc odpowiedz na to pytanie\n")).lower().strip()
        if answer.lower() == "koniec":
            print "Dziekuje, konczymy"
            break
    slownik_AI.update({key: answer})
    print slownik_AI
