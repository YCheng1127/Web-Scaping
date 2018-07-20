# Web-Scaping

2018/7/19
I tried scraping data from https://mojim.com/twza1.htm and I suffer from settling the environment of linux subsystem under Window10.

The stuff I had done:
1. install chrome (success)
2. install selenium (success)
3. install firefox (failed)
4. install ubuntu-desk (not knowing what for)

It seems that selenium can do many things and can help me grab Web javascript rendered stuff.
But I have problem installing firefox, even though I had installed the geckodriver, it still don't work. Then I tried using chrome, but chrome also demand a chromedriver to start. And one thing to aware of is that the version of chromedriver has to corresbond to the version of chrome.The installation of chrome is not very convenient. I had type few instructions at the command line to make it. 

	1.wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	2.dpkg -i google-chrome-stable_currentamd64.deb
	3.apt-get install -f
	4.download chromedriver and put it in the folder where the selenium is

actually it was not that complicate, but I used to check the version and see if the stuff is install. So I type chrome --version to see. And I found nothing, which makes me very anxious. Then I found that we can use "apt-get install google-chrome-stable" to check the version.

Another thing that confused me is that firefox doesn't work when I type "firefox" at the command line, and it said that no display environment variables. It seems that I need more than a terminal to start it. This also made me very anxious since phantomjs was no longer useful.
