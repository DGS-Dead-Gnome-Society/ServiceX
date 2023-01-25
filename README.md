# ServiceX
A pseudo-services bot wrote in Python 3 for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

**Please note:** IRC daemons tend to break the RFC standards for IRC meaning they don't entirely abide by them, they have their own protocol level differences. ServiceX is developed for the DGS (Dead Gnome Society) network and DGS servers run UnrealIRCd which breaks those standards, that means that ServiceX ***may*** crash if used on a non-UnrealIRCd IRC network depending on the IRCd they use. We are not responsible for any crashes you ***may*** endure due to running ServiceX on a non-UnrealIRCd IRC network.

## How will ServiceX work?
At current, I have multiple models on how ServicesX should be coded.

## What is DGS (Dead Gnome Sociaty)?
DGS has been killing gnomes since 1806, so if you got any gnome pest then DGS is who you wanna call. Actually that was a joke but here's the truth, DGS (Dead Gnome Society) started in 2005 as a WoW (World of Warcraft) guild that started to kill gnomes (a WoW race). The guild is strong as ever today and has also evolved into an IRC Network with a lot of amazing people to help you, and chat with. If you want to see what we are about then feel free to connect to our IRC network at irc.poulskitchen.club on port 6667 or port 6697 (For SSL) and don't forgot to read the MOTD.

## Feature Checklist
When features are proposed, they'll be added to this list. When features are implemented, they'll be checked out.
* [ ] Configurability (Either TOML or JSON)
* [ ] Ensured compatibility with `UnrealIRCd specifics`
* [ ] SASL authentication (Ability to authentication via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Automatically join all channels in the `#DGS-* namespace` (Configurable)
* [ ] Command interpreter (Commands sent to ServiceX in channels and via PM)
* [ ] Module engine
* [ ] Verification of users based on the NickServ account username shown in their WHOIS
* [ ] Polling System (Democracy)
* [ ] Channel Statistics

## Features that will not be supported and why
First of all, why add extra features if they really aren't necessary for our needs? Lets try to abide by the KISS (Keep It Simple Stupid) principle.
* ***SSL and IPv6 support:*** ServiceX has been designed to provide services tailored to the culture and needs of the DGS IRC network and connect via 127.0.0.1
