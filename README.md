# Insert Random Word

A simple Sublime Text 2 plugin that inserts a word selected at random from a wordlist into the current document.  
I use this plugin extensively for unit testing.  How many times have you written something like this into a test:

        userName = 'userName',
        title = 'title',
Now you don't have to!

        userName = 'alloxans offhand'
        title = 'jingall doubts'

## Use

The default hotkey for the plugin is ctrl+shift+r.  It will insert a word into a single selection, or the same word into a multiple selection.  

## Settings

There are two settings.  

* min_length: sets the minimum size of the word to be inserted
* max_length: sets the maximum size of the word to be inserted

The wordlist used for this plugin has no words shorter than 2 characters, and no words longer than 8 characters.  A value of None for either the min_length or max_length will make these settings ignored.  