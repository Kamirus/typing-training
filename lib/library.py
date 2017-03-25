import random
import json
import os

CONST = {
    'filename': '.typingtraininglib.json'
}


class Library(object):
    def __init__(self):
        self._dirpath = os.path.dirname(os.path.realpath(__file__))
        self._path = os.path.join(self._dirpath, CONST['filename'])
        self.list = None

        # check if file exists
        if os.path.exists(self._path):
            return

        # create default file
        defaultlist = [
            {
                'difficulty': 0,
                'text': "You will all be running. In a world you cannot hide. And the end is coming. For the lemming standing in line."
            },
            {
                'difficulty': 0,
                'text': 'def __init__(self, arg): super(ClassName, self).__init__()'
            },
            {
                'difficulty': 0,
                'text': 'for ind4x, v4L in enumerate(2 ** _285 for _285 in l492)'
            },
            {
                'difficulty': 0,
                'text': "Overcoming. Let the fury build inside. It could all be broken. If you only opened your eyes"
            },
            {
                'difficulty': 1,
                'text': "As I survey the chaos, taking in the lack of raw humanity. It's as if the entire world's fallen in love with their insanity. Hear the innocent voices scream. As their tormentors laugh through all of it. No forgiveness from all I've seen. A degradation I cannot forget"
            },
            {
                'difficulty': 1,
                'text': "Raw emotion, pure devotion. They will testify. And our memory will endure for all time. Never hiding, no dividing. Let them witness us move as one now. Show no mercy, let the world see. We're invincible. Show them nothing is beyond our control. Take it higher, our desire. Will determine what we’ve become now"
            },
            {
                'difficulty': 2,
                'text': "qo29*328s@xcsa^0-[]-;-/+1421d()ED#b6X&x*^@"
            },
            {
                'difficulty': 2,
                'text': '#En0rm0u$11'
            }
        ]
        with open(self._path, mode='w', encoding='utf-8') as f:
            json.dump(
                defaultlist,
                f,
                ensure_ascii=False,
                indent=4,
                sort_keys=True
            )

    def load(self):
        with open(self._path, encoding='utf-8') as f:
            self.list = json.load(f)
            if type(self.list) is not list:
                raise TypeError('Loaded file is not a list: {}'.format(type(self.list)))

    def getrandom(self, difficulty=None):
        # Load the file if it is not loaded
        if self.list is None:
            self.load()

        # transform param to set
        if type(difficulty) is not set:
            # maybe its iterable
            try:
                difficulty = set(difficulty)
            # its not iterable
            except TypeError:
                difficulty = {difficulty}

        # get list of wanted texts
        textslist = [
            elem['text'] for elem in self.list
            if difficulty is None or
            elem['difficulty'] in difficulty
        ]

        return textslist[random.randrange(0, len(textslist))]