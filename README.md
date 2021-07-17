# XenoBot
> This branch conains a development build of 1.1 version of XenoBeep<br/>
> It is not done yet, so use it on your own risk<br/>
> I am __not__ giving any support if it breaks for you!

## What is all about this bot?
The main goal of this bot are functions like games and some other fun stuff. I don't have any plans right now to add any administrative functions to it, but i might change my mind, for now there are many other bots that are more suited for this.

## How frequent it is updated?
Rarely, and randomly

## What commands does it have? 
**The commands are divided into several categories:**
 - Administrative (disabled by default, they are comented out in code)
 - Fun (8 ball, Truth or Dare, Lotto, but kinda lame)
 - Experimental (aka my container for various random stuff, with are not always... good. I recomend getting rid of this cog `experimental.py` or add at its beginning tzw. the so-called the floor => `_` )
 - Tools (clear, ping, about)

# How can I add this bot?
>I don't plan to host this bot publicly, but you can put it on your own hosting! (if u want for some reason) 

**All the things needed to run the bot are in `requirements.txt`**<br/>
**A python version that will work 100% will be in `runtime.txt`**<br/>
**How to host it is described on the Wiki (but it is in Polish. Wiki will be updated after the release of 1.1)**<br/>

# Economy (alfa) (not bothering translating it, because it's kinda lame in it's current state)
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

