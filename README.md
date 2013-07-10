AutoSoftWrap
============

SublimeText 2/3 to auto enable "Word Wrap" only for certain extensions

Description
-----------

AutoSoftWrap is a plugin for Sublime Text 2 and 3 that when enabled, every time a new buffer is loaded, and the filename extension is listed in the plugin settings, automatically enables `View -> Word Wrap`. This is mostly useful when viewing/editing lightweight markup languages like [Markdown](http://daringfireball.net/projects/markdown/).

Really useful when reading documentation maintained inside code repositories, but enabling `Word Wrap` globally is not desirable.

Installation
------------

AutoSoftWrap can be installed in a variety of ways:

* Using [Package Control](http://wbond.net/sublime_packages/package_control)

    Open Package Control
    Select 'Install Package'
    Find and select 'AutoSoftWrap'

* By cloning this repository in Packages

        cd into your Packages folder
        git clone https://github.com/mandx/SublimeAutoSoftWrap.git .

Configuration
-------------
Right now there's only one setting to configure AutoSoftWrap `extensions`: It's a list of extensions to check when a file is first loaded, and if it matches one on this list, then `Word Wrap` is automatically enabled.

By default the default extension list is set to:

    {
        "extensions": [
            "markdown", "mdown", "md",
            "textile", "rdoc", "org",
            "creole", "mediawiki", "rst",
            "asciidoc", "pod", "txt"
        ]
    }

This is the same list of lightweight markup formats supported by [GitHub Markup](https://github.com/github/markup)
