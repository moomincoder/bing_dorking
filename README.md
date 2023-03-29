# bing_dorking
 
This is a script to check to see if there are any vulnerable assets just chilling in the wind, just waiting for you t ofind them.

All you need to do is format a txt file like this, with however many targets or variants of the target you want, just make sure that each one is on a new line <br>
    www.example.com <br>
    example.com

and include the dorks file that is in the repo.

total command is ```python3 ./web_dorking.py dorks.txt targets.txt```