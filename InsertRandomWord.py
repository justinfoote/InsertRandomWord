import os

from random import randint
import sublime
import sublime_plugin

settings = sublime.load_settings("InsertRandomWord.sublime-settings")

def getSetting(key, default = None):
    value = settings.get(key)
    if value is None:
        return default
    return value


class InsertRandomWordCommand(sublime_plugin.TextCommand):
    _WORD_LIST_FILE_NAME = 'wordlist.txt'

    _MIN_LENGTH = getSetting('min_length', 0)
    _MAX_LENGTH = max(getSetting('max_length', float('inf')), _MIN_LENGTH)


    _wordListPath = os.path.join(sublime.packages_path(), 'InsertRandomWord', 
            _WORD_LIST_FILE_NAME)
    _wordList = None


    def run(self, edit):
        word = self._getWord()
        for s in self.view.sel():
            if s.size():
                self.view.replace(edit, s, word)
            else:
                self.view.insert(edit, s.begin(), word)


    def _getWord(self):
        if self._wordList is None:
            lines = [l.strip() for l in open(self._wordListPath).readlines()]
            self._wordList = [l for l in lines if self.isOk(l)]

        return self._wordList[randint(0, len(self._wordList) - 1)]


    def isOk(self, word):
        return ((self._MIN_LENGTH is None or len(word) >= self._MIN_LENGTH)
                and (self._MAX_LENGTH is None or len(word) <= self._MAX_LENGTH))