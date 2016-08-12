# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import argparse
import logging

from baikal17.core import Story


def start_story(path: str):
    """ Init CLI UI for story and start adventure

    :arg path: path to file with story
    """
    story_source = read_story(path)
    adventure = CLIStory(story=story_source)
    adventure.go()


def read_story(path: str) -> list:
    """ Read story from the file

    :arg path: path to file with story
    :return list of strings
    """

    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError as err:
        logging.critical(err)
        exit()


class CLIStory(object):
    """ Doc
    """

    def __init__(self, story: list):
        self.story = Story(story)

    def go(self):
        print(self.story)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('story_path', help='path to story file')
    start_story(path=parser.parse_args().story_path)
