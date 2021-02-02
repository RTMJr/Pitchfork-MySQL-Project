# Pitchfork-MySQL-Project

This project extracts albums entered by the user at the command line and 
and searches for their review on [Pitchfork](https://pitchfork.com/). If the
review exists, it loads the review information into a MySQL database that is
created called pitchfork. The table that is created is called reviews.

The dependencies for this application are the python 
[discogs](https://github.com/joalla/discogs_client) client, the mysql package, 
and the [pitchfork python api](https://pypi.org/project/pitchfork/). 

The update\_certificates.py file must be executed prior to using main.py
each user session.

Lastly, application variables must be placed into the config file in order for
the app to function - MySQL client info, and when using discogs client you must
name your app, and generate a user token (see discogs client link in this README).
