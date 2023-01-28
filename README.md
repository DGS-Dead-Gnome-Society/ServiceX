# ServiceX
A pseudo-services bot wrote using the python3-twisted library for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

## How to use
Run servicex-setup to put a fresh database in place and populate it with initial entries:
```./servicex-setup```

Then run servicex:
```./servicex```

## What is DGS (Dead Gnome Sociaty)?
DGS has been killing gnomes since 1806, so if you got any gnome pest then DGS is who you wanna call. Actually that was a joke but here's the truth, DGS (Dead Gnome Society) started in 2005 as a WoW (World of Warcraft) guild that started to kill gnomes (a WoW race). The guild is strong as ever today and has also evolved into an IRC Network with a lot of amazing people to help you, and chat with. If you want to see what we are about then feel free to connect to our IRC network at irc.poulskitchen.club on port 6667 or port 6697 (For SSL) and don't forgot to read the MOTD.

## Feature Checklist
When features are proposed, they'll be added to this list. When features are implemented, they'll be checked out.
* [X] Database support for configuration files and other data (sqlite3)
* [ ] SASL authentication (Ability to authenticate via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Automatically join all channels in the `#DGS-* namespace` (Configurable)
* [x] Command interpreter (Commands sent to ServiceX in channels and via PM and seems to fully work)
* [ ] Module engine
* [ ] Verification of users based on the NickServ account username shown in their WHOIS
* [ ] Ability to use MemoServ to send messages to one or more users
* [ ] Polling System (Democracy)
* [ ] Channel Statistics

## Features that will not be supported and why
First of all, why add extra features if they really aren't necessary for our needs? Lets try to keep to the KISS (Keep It Simple Stupid) approach.
* ***SSL and IPv6 support:*** ServiceX has been designed to provide services tailored to the culture and needs of the DGS IRC network and connect via 127.0.0.1
* ***Multithreading:*** We are a small IRC network so ServiceX won't be receiving much traffic, there are no features proposed at present that require multiple tasks to run concurrently
* ***Multi-network support:*** This should be obvious

## Demonstration console output
```$ ./servicex 
2023-01-27 02:05:51+0000 [-] Log opened.
2023-01-27 02:05:51+0000 [-] Starting factory <__main__.ServiceXFactory object at 0x7fb3d2742520>
2023-01-27 02:05:53+0000 [-] Attempting to identify with NickServ as user 'X'.
2023-01-27 02:05:53+0000 [-] I have joined channel '#DGS-Bots'.
2023-01-27 02:05:53+0000 [-] I have joined channel '##DGS-Bots'.
2023-01-27 02:05:53+0000 [-] Successfully identified with NickServ.
2023-01-27 02:06:09+0000 [-] Command 'ping' sent by 'Helenah!s98259@PoulsKitchen.Club' via channel '#DGS-Bots' was found.
2023-01-27 02:06:13+0000 [-] Command 'test' sent by 'Helenah!s98259@PoulsKitchen.Club' via channel '#DGS-Bots' was not found.
2023-01-27 02:06:15+0000 [-] Command 'time' sent by 'Helenah!s98259@PoulsKitchen.Club' via channel '#DGS-Bots' was found.
2023-01-27 02:06:20+0000 [-] Command 'ping' sent by 'Helenah!s98259@PoulsKitchen.Club' via PM was found.
2023-01-27 02:06:23+0000 [-] Command 'test' sent by 'Helenah!s98259@PoulsKitchen.Club' via PM was not found.
2023-01-27 02:06:28+0000 [-] Command '!test' sent by 'Helenah!s98259@PoulsKitchen.Club' via PM was not found.
2023-01-27 02:06:30+0000 [-] Command 'time' sent by 'Helenah!s98259@PoulsKitchen.Club' via PM was found.```
