Introduction
============
collective.piwik.mediaelement displays a video play counter for Plone sites that use collective.mediaelementjs (http://pypi.python.org/pypi/collective.mediaelementjs).
A download counter is displayed when used in combination with collective.transcode.star (http://pypi.python.org/pypi/collective.transcode.star) or Plumi (http://plumi.org).

Usage data is stored and retrieved by Piwik (http://piwik.org), an open source analytics platform.

How to get it working
=====================

 - Install collective.piwik.core and collective.mediaelementjs from the Plone control panel.
 - You need to have access to a working Piwik installation. Create a new site in the Piwik admin UI and a new user who should have view access for that site.
 - Go to the Piwik Settings page in the Plone control panel and enter the URL of your Piwik instance, the siteId and the user's authentication token
 - Upload a video that can be played by mediaelementjs and click play

If you do the above a viewlet should appear on top of mediaelementjs displaying the number of views of each video. 

Credits
=======

The product was created by Unweb.me (https://unweb.me)
