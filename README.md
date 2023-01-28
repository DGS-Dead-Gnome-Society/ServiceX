# ServiceX
A pseudo-services bot wrote using the python3-twisted library for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

## How to use
Run servicex-setup to put a fresh database in place and populate it with initial entries:
```./servicex-setup```

Then run servicex:
```./servicex```

## What is DGS (Dead Gnome Sociaty)?
DGS has been killing gnomes since 1806, so if you got any gnome pest then DGS is who you wanna call. Actually that was a joke but here's the truth, DGS (Dead Gnome Society) started in 2005 as a WoW (World of Warcraft) guild that started to kill gnomes (a WoW race). The guild is strong as ever today and has also evolved into an IRC network with a lot of amazing people to help you, and chat with. If you want to see what we are about then feel free to connect to our IRC network at irc.poulskitchen.club on port 6667 or port 6697 (For SSL) and don't forget to read the MOTD.

## Feature Checklist
When features are proposed, they'll be added to this list. When features are implemented, they'll be checked out.
* [X] Database support for configuration files and other data (sqlite3)
* [x] Command interpreter (Commands sent to ServiceX in channels and via PM and seems to fully work)
* [ ] SASL authentication (Ability to authenticate via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Automatically join all channels in the `#DGS-* namespace` (Configurable)
* [ ] Module engine
* [ ] Verification of users based on the NickServ account username shown in their WHOIS
* [ ] Ability to use MemoServ to send messages to one or more users
* [ ] Polling System (Democracy)
* [ ] Channel Statistics

## Demonstration console output
```$ ./servicex 
2023-01-28 12:24:07+0000 [-] Log opened.
2023-01-28 12:24:07+0000 [-] Attempting to load database file 'servicex.db'.
2023-01-28 12:24:07+0000 [-] Starting factory <__main__.ServiceXFactory object at 0x7f0fc6de8bb0>
2023-01-28 12:24:13+0000 [-] Attempting to identify with NickServ as user 'X'.
2023-01-28 12:24:13+0000 [-] Attempting to join channel '#bots'.
2023-01-28 12:24:19+0000 [-] Successfully joined channel '#bots'.
2023-01-28 12:24:33+0000 [-] Command 'ping' sent by 'Helenah!~s98259@user/helenah' via channel '#bots' was found.
2023-01-28 12:24:36+0000 [-] Command 'test' sent by 'Helenah!~s98259@user/helenah' via channel '#bots' was not found.
2023-01-28 12:24:44+0000 [-] Command 'ping' sent by 'Helenah!~s98259@user/helenah' via PM was found.
2023-01-28 12:24:48+0000 [-] Command '!ping' sent by 'Helenah!~s98259@user/helenah' via PM was not found.
2023-01-28 12:24:50+0000 [-] Command 'test' sent by 'Helenah!~s98259@user/helenah' via PM was not found.```
