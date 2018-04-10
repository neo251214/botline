# -*- coding: utf-8 -*-

"""
This is the file place to setting the application before you try to run it!
"""

class Settings:
	def __init__(self):
		# -> Main setting.
		# Your authentication token.
		self.AUTH_TOKEN = "hsC1JrkmF2oUvLLKM1LOqKq+UTeafwpqqP6yVs/vHopxbFsFDhE0Uk4NXCgXAu0jguVbGSG3MzcczlWHhzXN1SsfrqOSZ3KXs3Qx+IH4KOPDKgjfvYseXq11voIhZi7lPEoce8A6/3M6xGrwwOtCjAdB04t89/1O/w1cDnyilFU=" 
		
		# -> Youtube video downloader setting.
		# Integrate with your site url + the path for saving the downloaded videos.
		self.SITE_URL = "http://yoursite.com/DIRECTORY" #your address site to see the saved videos, eg: http://site.com/videos/.
		self.SITE_PATH = "YOUR_PATH" #path/directory to save the videos, eg: /home/user/public_html/videos/.
		
		# -> Welcome Message when you are accepted the invite groups.
		self.WELCOME_MESSAGE = '\
		Hai, Aq satpamnya Genre Music Community . Silahkan gunakan perintah\
		"!bothelp" untuk melihat perintah yang tersedia.'
		
		# -> Auto reply setting.
		# Replacing "simi" words to another words.
		self.REPLACEMENT_CALL = "Satpam Jinak"

		# -> Not Important setting.
		# Have another account? you can set it for your secondary account, it will called you/the others account as a boss.
		self.HERE_IAM_YOUR_BOSS = "0xffa" 
