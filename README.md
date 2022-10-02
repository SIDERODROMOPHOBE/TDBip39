# TDBip39
Blockchain Programming TD2 Gabriel Saliba

This the TD2 of Blockchain Programming on BIP39 and mnemonic words creation

TD2.py is the main python file to execute.

TD2.py has # comment to describe how does it work
TD2.py has a console interface to use the various fonctions (press 1 or 2 to make choices)
Checksum is made through a SHA256 Hash, and is integrated via another .py file named sha256.py wich is in the same repository and necessary to let TD2.py work properly.
(source : GitHub Sha256)


it has fucntion Generate_Seed() and Import_Seed()

Generate_Seed() can find the Bip39 Mnemo words form a wanted entropy, or can generate a new crypto-safe one using Secrets library

Import_Seed() take seed words in parameter, and returns the binary and the integer entropy that permits to generate this chain of words
Import_Seed() is bugged and doesnt work properly :'-(

Bip39 words are imported via BUP39words.txt wich is a txt files ontaining the bip39 mnemo words in order. it is necessary to have it in the repository
