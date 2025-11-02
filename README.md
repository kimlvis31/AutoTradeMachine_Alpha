# AutoTradeMachine_Alpha

This is the first version of my Auto Trade Machine project.
I started this project as I was just beginning to learn Python, 
so this version only provides a few very basic GUI functions (tkinter) and a simple data download test via the Binance API (ccxt library).

Honestly, there's not much to see here - I just wanted to put it out there for a personal record.

*** 
If you ever happen to be interested to look at the code, you'll see that in the main file the `accessManager` part (which tests Binance API interaction) is commented out. 
That's because in the original version, `accessManager` reads API Keys from a text file named "apikeys.txt" upon initialization, but there's no exception handling implemented for when that file doesn't exist.
I could fix it, but wanted to keep the code as original as possible. So I just commented that part out - since you know, this particular version doesn't really do anything anyways haha

Anyways, when you run the program, you'll still be able to play with the little interaction test GUI I made - so enjoy!
***