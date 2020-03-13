# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:31:36 2020
@author: adrian
"""

from controllers.controller import Controller
from ui.ui import UI


def main():
    controller = Controller()
    ui = UI(controller)
    ui.run()


main()
