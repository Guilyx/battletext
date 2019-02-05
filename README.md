# NameToBeFound Battle Game

## Principle

Text round per round battle game supporting one on one combats (User vs Random) for now. Supporting H²H, Magic Spells and Items use, dynamic health and mana bars, easy to create new spells/items.

*Architecture :*
> main.py : main code to start the combat session, ends with either player hitting the 0 HP mark.

> CharacterClass.py : First Character Class, defining attributes for everyone who's a character (which is everyone)

> Item.py : Item class defining the attributes for item creation

## Steps

* The first character to make a move is randomly decided. Either BOT or PLAYER1 supported at the moment. 

> Planning the implementation of a stat enhancing the probabilities for a player to start first. Will be supported in future Multiplayer mode.

[First round](https://www.noelshack.com/2019-06-2-1549376122-capture-du-2019-02-05-14-58-22.png "bla")

* Hit with the action of your choice the enemy (only one currently), then will have to choose the action and on which character to apply this action (heal an ally, heal yourself, hit the enemy, etc)

  *  ITEMS taking name, type, description, property as Class attributes
  
  ![ITEM use](https://www.noelshack.com/2019-06-2-1549376122-capture-du-2019-02-05-14-59-21.png)
  
  *  MAGIC taking name, cost, damage and type in a dictionnary (method in Character Class)
  
  ![MAGIC use](https://www.noelshack.com/2019-06-2-1549376122-capture-du-2019-02-05-14-58-46.png)
  
  *  ATTACK (h2h), defined in the Character Class.
  

 
## How to use it ?

To use the program, open your terminal, cd your way to the directory you want to put the repository in, then follow these steps :

```git clone https://github.com/Guilyx/battletext/tree/master``` 

```cd battle_game``` 

```python3 main.py``` 

## What's next ?



## Licence
[BSD 3-Clause License](https://github.com/Guilyx/battletext/blob/master/LICENSE)


 
