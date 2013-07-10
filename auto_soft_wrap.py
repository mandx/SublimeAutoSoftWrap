from pprint import pprint
from os.path import splitext

import sublime
from sublime_plugin import EventListener as SublimeEventListener


class AutoSoftWrapEventListener(SublimeEventListener):

    PLUGIN_NAME = 'AutoSoftWrap'
    SETTINGS_FILE = PLUGIN_NAME + '.sublime-settings'
    DEFAULT_EXTENSIONS = 'markdown,mdown,md,textile,rdoc,org,creole,mediawiki,rst,asciidoc,pod,txt'.split(',')

    def on_load(self, view):
        extension = splitext(view.file_name())[1]
        plugin_settings = sublime.load_settings(self.SETTINGS_FILE)
        extensions = plugin_settings.get('extensions', self.DEFAULT_EXTENSIONS)
        if extension[1:] in extensions:
            view.run_command('set_setting', {'setting': 'word_wrap', 'value': True, })
            sublime.status_message('{plugin}: Enabled soft word wrap ("{ext}")'.format(
                plugin=self.PLUGIN_NAME, ext=extension,
            ))
