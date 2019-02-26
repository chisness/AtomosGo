#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:25:31 2019

@author: schirmer
"""

from dlgo import agent
from dlgo import goboard as goboard
from dlgo import gotypes
from dlgo import mcts
from dlgo.utils import print_board, print_move, point_from_coords
from six.moves import input

def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = mcts.MCTSAgent()
    
    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            if human_move == 'pass':
                move=goboard.Move.pass_turn()
            else:
                point = point_from_coords(human_move.strip())
                move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        game = game.apply_move(move)
        print_move(game.next_player, move)
        
if __name__=='__main__':
    main()