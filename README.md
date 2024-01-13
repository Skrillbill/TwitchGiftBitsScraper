<h1>Twitch Gift and Bits Leaderboard scraper</h1>

<p>This script uses ChromeWebDriver to save screenshot of your streams Gifts and Bits leaderboards. </p>

<h3>Configurables: </h3>
<ul>
  <li>Stream handle</li>
  <li>Screenshot output directory</li>
</ul>


<h2>Getting started</h2>
<p>Install Python if you haven't already: https://www.python.org/downloads/ (default installation, be sure to add python to PATH when it asks). </p>

<p>Download TwitchGiftBitScraper.py and requirements.txt . </p>

<p>Go to where python is installed and create a scripts folder if there isn't one, and copy the .py and requirement file you downloaded to the scripts folder. </p>

Open a windows terminal and type `python.exe -m pip install -r requirements.txt`

Open the .py file to find and change: 
Find https://www.twitch.tv/popout/yourstreamerhere/chat and replace yourstreamerhere with your Twitch handle. 

Find <i>C:\\path\\to\\your\\folder\\here\\</i> and replace with the path to where you want to save screenshots. 
> **You MUST use double back slashes for the path**

<h2>Usage</h2>

Open a terminal (assuming you have added python to PATH) and type ` .\TwitchGiftBitsScraper.py `.

A window will pop up and load your channels chat. **You do NOT have to be live for this to run.** There are deliberate delays in the script to account for instances where the page loads slowly. The longest of these delays is 15 seconds. Don't worry, it still running and the window will close when its finished. 

