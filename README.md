# Introduction

I don't know why I didn't know about json back then. This program is completely useless if you have decent json viewer.

Curently this program uses lazy method to load up large log files.

However, since still program loads up all entries on QTreeWidget, that cause memory usage around 350MB with 30MB owncloud log file.

Since I also want QTreeWidget's sorting functionality, I'm stuck here.

----
Now Supports Nextcloud mainly, still supports owncloud(~=10.3.2). I moved to nextcloud, so I don't get any more owncloud logs to test with.

Owncloud logs tend to make 'message' section padded with trash strings, parsing json annoying.

Current state (log from owncloud 10.3.2): 
![Imgur](https://imgur.com/QCYzzbD.jpg)
