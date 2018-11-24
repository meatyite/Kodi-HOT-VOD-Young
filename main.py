# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

VIDEOS = {'Flashback 2': [{'name': 'Episode 1',
                       'thumb': 'https://images1.ynet.co.il/PicServer5/2017/05/08/7766384/FLASHBACK2_01.jpg',
                       'video': 'http://ynethd-i.akamaihd.net/i/0517/HOT/0805171400FLASHBACK_2_ep01.mp4/master.m3u8',
                       'genre': 'Series'}
                      ],
            'Tzafoof': [{'name': 'Episode 1',
                      'thumb': 'https://images1.ynet.co.il/PicServer5/2017/04/23/7735379/TZAFUF_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0417/HOT/1604171200TZAFUF_ep_01.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Episode 3',
                      'thumb': 'https://images1.ynet.co.il/PicServer5/2017/04/23/7735379/TZAFUF_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0517/HOT/2105171230TZAFUF_ep03_768Kbps_360p.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Episode 4',
                      'thumb': 'https://images1.ynet.co.il/PicServer5/2017/04/23/7735379/TZAFUF_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0517/HOT/2105171230TZAFUF_ep04_768Kbps_360p.mp4/master.m3u8',
                      'genre': 'Series'}
                     ],
            'Schona': [{'name': 'Season 2 Episode 1 + 2',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0916/HOT/0109161130SHCHUNA_S02E01.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 3',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0916/HOT/0409161300SHCHUNA_S02E03.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 4',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0916/HOT/0509161100SHCHUNA_S02E04.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 5',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0916/HOT/0609161330SHCHUNA_S02E05.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 27',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0217/HOT/0602172130SHCHUNA_2_ep27.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 28',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0217/HOT/0602172130SHCHUNA_2_ep28.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 2 Episode 29',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/08/21/7214411/SHCHUNA2_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0217/HOT/0602172130SHCHUNA_2_ep29.mp4/master.m3u8',
                      'genre': 'Series'}
                     ],
            'Galis': [{'name': 'Season 1 Episode 1',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/1202121630galis1.flv/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 1 Episode 2',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/1302121430galis02.flv/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 1 Episode 3',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/1502121000galis3.flv/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 1 Episode 4',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/1502121530galis04.flv/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 1 Episode 5',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/2002121100galis05.flv/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 1 Episode 6',
                      'thumb': 'https://images1.ynet.co.il/PicServer3/2014/01/22/5112591/galis_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0212/2002121530galis06.flv/master.m3u8',
                      'genre': 'Series'}
                     ],
            'Hakalmarim': [{'name': 'Season 5 Episode 1',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/07/07/7117953/HAKALMARIM5_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0716/HOT/0607162300HAKALMARIM_5_ep01.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 5 Episode 2',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/07/07/7117953/HAKALMARIM5_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0716/HOT/0607162300HAKALMARIM_5_ep02.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 5 Episode 3',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/07/07/7117953/HAKALMARIM5_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0716/HOT/0607162300HAKALMARIM_5_ep03.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 5 Episode 4',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2016/07/07/7117953/HAKALMARIM5_01.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0716/HOT/0607162300HAKALMARIM_5_ep04.mp4/master.m3u8',
                      'genre': 'Series'}
                     ],
            'HaPijamot': [{'name': 'Season 9 Episode 1',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2015/01/11/5809268/PIJ9_011.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0115/HOT/0401_1020_HAPIGAMOT_EP_1_ynet.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 9 Episode 2',
                      'thumb': 'https:/https://images1.ynet.co.il/PicServer4/2015/01/11/5809268/PIJ9_011.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0115/HOT/0501_1200_HAPIGAMOT_EP_2_ynet.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 9 Episode 3',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2015/01/11/5809268/PIJ9_011.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0115/HOT/06011230HAPIGAMOT_EP_3.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 9 Episode 4',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2015/01/11/5809268/PIJ9_011.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0115/HOT/07011530HAPIGAMOT_EP_4.mp4/master.m3u8',
                      'genre': 'Series'},
                     {'name': 'Season 9 Episode 5',
                      'thumb': 'https://images1.ynet.co.il/PicServer4/2015/01/11/5809268/PIJ9_011.jpg',
                      'video': 'http://ynethd-i.akamaihd.net/i/0115/HOT/1101_1230_HAPIGAMOT_EP_5_ynet.mp4/master.m3u8',
                      'genre': 'Series'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
