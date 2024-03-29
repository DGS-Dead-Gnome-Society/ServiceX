# ServiceX
ServiceX is a database-driven (sqlite3) pseudo-services bot wrote using the python3-twisted library for the DGS (Dead Gnome Society) IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

**Please use this bot responsibly, ask channel owners for permission to join this bot to their channels.**

## How to use
Read the [wiki](https://github.com/DGS-Dead-Gnome-Society/ServiceX/wiki), if you don't read the wiki then I won't help you.

## What is DGS (Dead Gnome Society)?
DGS has been killing gnomes since 1806, so if you got any gnome pest then DGS is who you wanna call. Actually that was a joke but here's the truth, DGS started in 2005 as a WoW (World of Warcraft) guild that started to kill gnomes (a WoW race). The guild is strong as ever today and has also evolved into an IRC network with a lot of amazing people to help you, and chat with. If you want to see what we are about then feel free to connect to our IRC network at irc.poulskitchen.club on port 6667 or port 6697 (For SSL) and don't forget to read the MOTD.

## Feature Checklist
When features are proposed, they'll be added to this list. When features are implemented, they'll be checked out.
* [X] Database support for configuration and other data (sqlite3)
* [x] Command interpreter (Commands sent to ServiceX in channels and via PM and seems to fully work)
* [X] Join, part, cycle channels using the join, part and cycle commands (Made persistant in database)
* [X] Date and time commands
* [X] Database-driven module engine
* [X] Can construct dataframes to be sent over IRC
* [X] Support for both SSL and Non-SSL connections
* [ ] SASL authentication (Ability to authenticate via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Automatically join all channels in the `#DGS-* namespace` (Configurable)
* [ ] Verification of users based on the NickServ account username shown in their WHOIS
* [ ] Ability to use MemoServ to send messages to one or more users
* [ ] Polling System (Democracy)
* [ ] Channel Statistics
* [ ] Permissions system

## Demonstration console output
```$ ./servicex 
2023-01-28_19:10:17:info: ServiceX starting up...
2023-01-28_19:10:17:info: Checking if database file 'servicex.db' exists.
2023-01-28_19:10:17:info: Attempting to connect to the database.
2023-01-28_19:10:17:info: Successfully made connection with NitoRadio (irc.nitoradio.com:6667).
2023-01-28_19:10:24:info: Attempting to identify with NickServ as user 'X'.
2023-01-28_19:10:24:info: Attempting to join channel '#nitoradio'.
2023-01-28_19:10:24:info: Channel '#nitoradio' already exists in the database.
2023-01-28_19:10:24:info: Attempting to join channel '#bots'.
2023-01-28_19:10:24:info: Channel '#bots' already exists in the database.
2023-01-28_19:10:24:info: Successfully joined channel '#nitoradio'.
2023-01-28_19:10:24:info: Successfully joined channel '#bots'.
2023-01-28_19:10:36:info: Command 'ping' sent by 'Helenah!~s98259@06.11.654.623.threembb.co.uk' via channel '#nitoradio' was found.
2023-01-28_19:10:42:info: Command 'ping' sent by 'nito!~nito@89.187.lmw.jys' via channel '#nitoradio' was found.
2023-01-28_19:10:43:info: Command 'test' sent by 'Helenah!~s98259@06.11.654.623.threembb.co.uk' via channel '#nitoradio' was not found.
