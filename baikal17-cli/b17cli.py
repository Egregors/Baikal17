# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import argparse
import logging


def read_story(path: str) -> list:
    """ Read story from the file

    :arg path: path to file with story
    :type path: str

    :return: list of strings
    """

    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError as err:
        logging.critical(err)
        exit()


def start_story(path: str):
    """ Docstring """
    story = read_story(path)
    adventure = CLIStory(story=story)
    adventure.go()


class CLIStory(object):
    """ Doc
    """

    def __init__(self, story: list):
        self.story = story

    def go(self):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('story_path', help='path to story file')
    start_story(path=parser.parse_args().story_path)
