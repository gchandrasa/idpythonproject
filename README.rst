===========
ID Python
===========
:Info: Website Python Indonesia
:Author: Gilang Chandrasa (http://github.com/gchandrasa)
:Maintainer: Gilang Chandrasa (http://github.com/gchandrasa)

Collaborators :
===============

- Adesanto Asman (@adesst)
- Fanani M. Ihsan (@fananimi)
- Gilang Chandrasa (@gchandrasa)
- Sakti Dwi Cahyono (@saktidc)
- Selwin Ong (@selwin)

Untuk settings lokal gunakan nama file settings_local.py, contoh isi file settings_local.py :
::

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'pencerah',                      # Or path to database file if using sqlite3.
	        'USER': 'username',                      # Not used with sqlite3.
	        'PASSWORD': 'password',                  # Not used with sqlite3.
	        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	    }
	}
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG

Note : 
Jangan masukan settings_local.py ke dalam git repository