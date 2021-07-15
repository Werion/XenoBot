# XenoBot
> Aka bot przeznacony do ogólnego użytku

## O co chodzi z tym botem?
Głównym założeniem bota są funkcje typu gry i  zabawy, nie planuję bawić się w funkje administracyjne, od tego jest już wiele botów które radzą sobie lepiej.

## Jak często jest aktualizowany?
Zadko, i losowo

## Jakie komędy posiada? 
**Komędy dzielą się na kilka kategori:**
 - Administracyjne (domyślie wyłączone, w kodzie są zakomętowane)
 - Zabawy (8 ball, Prawda czy Wyzwanie, Lotto)
 - Eksperymentalne (czyli mój tzw. pojemnik na różne losowe rzeczy, które nie zawsze są dobre. Radzę pozbyć się coga `experimental.py` albo dodać na jego początku tzw. podłogę => `_` )
 - Narzędzia (clear, ping, about)

# Jak mogę dodać tego bota?
>Nie mam w planach hostować tego bota publicznie, lecz ty możesz samodzielnie go postawić na własnym hostingu!

**Wszystkie rzeczy potrzebne do uruchomienia bota znajdują się w `requirements.txt`**

**Wersja pythona która będzie działać na 100% będzie znajdować się w `runtime.txt`**

**Jak mniej więcej zrobić by bot działał pisze na Wiki**

# Ekonomia (alfa)
> System nie jest jeszcze w 100% gotowy, zalecane jest wyłączenie modułu `vault.py` znajdującego się w folderze `cogs` (czyli dodaj przed nazwą coga tzw. podłogę: `_` )
## Od teraz użytkownicy mogą zarabiać walutę serwera uzywając XenoBota!
Pierwsza wersja systemu (alpha) będzie pozwalać tylko na transakcje w bocie, czyli jedynie XenoBot będzie miał dostęp do zasobów `vault.json` i jedynie jego komędy będą mogły modyfikować dane

W teori da sie wpływać na dane importując `vault`

```python
from cogs import vault

user = ctx.message.author.id # ctx is from discord.py 
server = ctx.message.guild.id
vault.add_data(userID=user, serverID=server, mode="Wallet", amount=prize) #System that adds new data
```
Załadowanie danych
```python
def load_data():
    with open("vault.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
```
Zapisywanie danych w bazie
```python
def write_data(new_data, serverID, userID, mode):
    data = load_data()
    data["Economy"][str(serverID)][str(userID)][str(mode.title())] = int(new_data)
    with open('vault.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
```
Ustawienie "na sztywno" danych w bazie
```python
def set_data(userID, serverID, mode, amount):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        add_user(serverID=serverID, userID=userID)
        data = load_data()
    write_data(new_data=int(amount), serverID=str(serverID), userID=str(userID), mode=str(mode))
```
Dodanie danych do bazy
```python
def add_data(userID, serverID, mode, amount):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        add_user(serverID=serverID, userID=userID)
        data = load_data()
    new_data = int(data["Economy"][str(serverID)][str(userID)][str(mode.title())]) + int(amount)
    write_data(new_data=int(new_data), serverID=str(serverID), userID=str(userID), mode=str(mode))
```

