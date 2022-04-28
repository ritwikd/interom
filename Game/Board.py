# -*- coding: utf-8 -*-

from . import History, Pieces, Position

position = Position.Position

STARTING_POSITION = {

    'white': {
        # Main Pieces
        'king': position(4, 0),
        'queen': position(3, 0),
        'rook1': position(0, 0),
        'rook2': position(7, 0),
        'knight1': position(1, 0),
        'knight2': position(6, 0),
        'bishop1': position(2, 0),
        'bishop2': position(5, 0),
        # Pawns
        'pawnA': position(0, 1),
        'pawnB': position(1, 1),
        'pawnC': position(2, 1),
        'pawnD': position(3, 1),
        'pawnE': position(4, 1),
        'pawnF': position(5, 1),
        'pawnG': position(6, 1),
        'pawnH': position(7, 1)
    },

    'black': {
        # Main Pieces
        'king': position(4, 7),
        'queen': position(3, 7),
        'rook1': position(0, 7),
        'rook2': position(7, 7),
        'knight1': position(1, 7),
        'knight2': position(6, 7),
        'bishop1': position(2, 7),
        'bishop2': position(5, 7),
        # Pawns
        'pawnA': position(0, 6),
        'pawnB': position(1, 6),
        'pawnC': position(2, 6),
        'pawnD': position(3, 6),
        'pawnE': position(4, 6),
        'pawnF': position(5, 6),
        'pawnG': position(6, 6),
        'pawnH': position(7, 6)
    }
}


class Board:
    def __init__(self):
        self.data = [[None for x in range(8)] for y in range(8)]

        # Use for xy_to_alg conversion
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.castle = {'K': 'O-O', 'Q': 'O-O-O'}
        self.symbols = {
            'white': {
                'K': '♔',
                'Q': '♕',
                'R': '♖',
                'N': '♘',
                'B': '♗',
                'P': '♙',
                'S': '◽'
            },

            'black': {
                'K': '♚',
                'Q': '♛',
                'R': '♜',
                'N': '♝',
                'B': '♞',
                'P': '♟',
                'S': '◾'
            }
        }

        self.alg_castle = {
            True: {
                'O-O': [position(4,0), position(6,0)],
                'O-O-O' : [position(4,0), position(2,0)]
            },
            False: {
                'O-O': [position(4,7), position(6,7)],
                'O-O-O': [position(4,7), position(2,7)]
            }
        }

        self.types = ['K','Q','R','B','N']
        self.log = History.Log.Log()
        self.taken = []

    def position_to_notation(self, position):
        """Convert """
        return self.letters[position.x] + str(position.y + 1)

    def set_start_position(self):

        K = Pieces.Other.King.King
        Q = Pieces.Major.Queen.Queen
        R = Pieces.Major.Rook.Rook
        B = Pieces.Minor.Bishop.Bishop
        N = Pieces.Minor.Knight.Knight
        Pl = Pieces.Other.Pawn.Pawn

        position_starting_board = STARTING_POSITION
        pieces_to_add = []

        # Add white Pieces
        pieces_to_add.append(K(self, position_starting_board['white']['king'], True))

        pieces_to_add.append(Q(self, position_starting_board['white']['queen'], True))

        pieces_to_add.append(R(self, position_starting_board['white']['rook1'], True))
        pieces_to_add.append(R(self, position_starting_board['white']['rook2'], True))

        pieces_to_add.append(B(self, position_starting_board['white']['bishop1'], True))
        pieces_to_add.append(B(self, position_starting_board['white']['bishop2'], True))

        pieces_to_add.append(N(self, position_starting_board['white']['knight1'], True))
        pieces_to_add.append(N(self, position_starting_board['white']['knight2'], True))

        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnA'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnB'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnC'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnD'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnE'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnF'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnG'], True))
        pieces_to_add.append(Pl(self, position_starting_board['white']['pawnH'], True))

        # Add black Pieces

        pieces_to_add.append(K(self, position_starting_board['black']['king'], False))

        pieces_to_add.append(Q(self, position_starting_board['black']['queen'], False))

        pieces_to_add.append(R(self, position_starting_board['black']['rook1'], False))
        pieces_to_add.append(R(self, position_starting_board['black']['rook2'], False))

        pieces_to_add.append(B(self, position_starting_board['black']['bishop1'], False))
        pieces_to_add.append(B(self, position_starting_board['black']['bishop2'], False))

        pieces_to_add.append(N(self, position_starting_board['black']['knight1'], False))
        pieces_to_add.append(N(self, position_starting_board['black']['knight2'], False))

        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnA'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnB'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnC'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnD'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnE'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnF'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnG'], False))
        pieces_to_add.append(Pl(self, position_starting_board['black']['pawnH'], False))

        for piece in pieces_to_add:
            self.set_piece(piece.position_current, piece)

    def knight_conflict(self, position_new, turn):
        piece_conflict = []

        piece_conflict.append(Position.Position(position_new.x + 1, position_new.y + 2))
        piece_conflict.append(Position.Position(position_new.x + 2, position_new.y + 1))
        piece_conflict.append(Position.Position(position_new.x + 2, position_new.y - 1))
        piece_conflict.append(Position.Position(position_new.x + 1, position_new.y - 2))

        piece_conflict.append(Position.Position(position_new.x - 1, position_new.y + 2))
        piece_conflict.append(Position.Position(position_new.x - 2, position_new.y + 1))
        piece_conflict.append(Position.Position(position_new.x - 2, position_new.y - 1))
        piece_conflict.append(Position.Position(position_new.x - 1, position_new.y - 2))

        conflicts = list(map(self.get_piece, piece_conflict))

        knights = []
        for R in conflicts:
            if R[0]:
                if R[1].type == 'N':
                    if R[1].color == turn:
                        knights.append(R[1])

        if (len(knights) > 1):
            if knights[0].position_current.x == knights[1].position_current.x:
                return 2
            else:
                return 1
        else:
            return 0

    def rook_conflict(self, position_new, turn):
        piece_conflict = []

        column_conflict = position_new.x
        row_confict = position_new.y

        # Column
        piece_conflict += [Position.Position(column_conflict, n) for n in range(8)]
        # Row
        piece_conflict += [Position.Position(n, row_confict) for n in range(8)]

        conflicts = list(map(self.get_piece, piece_conflict))

        rooks = []
        for R in conflicts:
            if R[0]:
                if R[1].type == 'R':
                    if R[1].color == turn:
                        rooks.append(R[1])

        for rook in rooks:
            if not rook.valid_move(position_new):
                return 0

        if (len(rooks) > 1):
            if rooks[0].position_current.x == rooks[1].position_current.x:
                return 2
            else:
                return 1
        else:
            return 0

    def potential_check_square(self, potential_position_conflict, current_position_conflict):
        # Determine if position could potentially be in check
        for rank in self.data:
            for square in rank:
                if square != None:
                    if square.color != current_position_conflict:
                        if square.valid_move(potential_position_conflict):
                            return True

        return False

    def check_any(self):
        check_status = {'w': False, 'b': False}
        p_kings = {'w': None, 'b': None}

        # Get king positions
        for rank in self.data:
            for square in rank:
                if square != None:
                    if square.type == 'K':
                        if square.color:
                            p_kings['w'] = square.position_current
                        else:
                            p_kings['b'] = square.position_current

        # Determine if either king is in check
        for rank in self.data:
            for square in rank:
                if square != None:
                    if square.color:
                        black_check = square.valid_move(p_kings['b'])
                        if black_check:
                            check_status['b'] = black_check
                    else:
                        white_check = square.valid_move(p_kings['w'])
                        if white_check:
                            check_status['w'] = white_check

        return check_status

    def mate_any(self):
        mate_status = {'w': False, 'b': False}

        return mate_status

    #def revert_move(self, move):


    def do_move(self, position_original, position_new, S_i):
        """Move piece from Position Orig (position_original) to Position New (position_new) """

        # Get information about position_original
        position_original_store = self.get_piece(position_original)
        if position_original_store[0]:
            # Get object and color of piece at position_original
            Piece = position_original_store[1]
            white_move = Piece.color
            # Check if position_new is a valid move for Piece at position_original
            if Piece.valid_move(position_new):
                # Check for castling
                if Piece.type == 'position':
                    Piece_t = None
                    position_new_store = self.get_piece(position_new)
                    # Check if there is a piece at position_new
                    take = position_new_store[0]
                    if take:
                        # Get object of piece at position_new
                        Piece_t = position_new_store[1]
                        Piece_t = None
                        # Get information about position_new
                        position_new_store = self.get_piece(position_new)
                        # Check if there is a piece at position_new
                        take = position_new_store[0]
                        if take:
                            # Get object of piece at position_new
                            Piece_t = position_new_store[1]
                        # Make proposed move from position_original to position_new
                        self.set_piece(position_new, Piece)
                        self.set_piece(position_original, None)
                        # Check if the current Player's king is now in check
                        check_status = self.check_any()
                        mate_status = self.mate_any()
                        if (white_move and check_status['w'] or
                                    not white_move and check_status['b']):

                            # Revert move and return false
                            self.set_piece(position_original, Piece)
                            self.set_piece(position_new, None)
                            if take:
                                self.set_piece(position_new, Piece_t)
                            return False
                        if take:
                            self.taken.append(Piece_t)
                        checks = True in [check_store[1] for check_store in list(check_status.items())]
                        mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                        move = History.Move.Move(white_move, Piece, position_original, position_new, True,
                                                 Piece_t, checks, mates, None)
                        self.log.add_move(move)
                        return True
                    else:
                        ep_check = abs(position_new.y - position_original.y) == 1 and abs(position_new.x - position_original.x) == 1
                        if ep_check:
                            P_ep_p = position(position_new.x, position_original.y)
                            ep_p = self.get_piece(P_ep_p)[1]
                            self.set_piece(position_new, Piece)
                            self.set_piece(position_original, None)
                            self.set_piece(P_ep_p, None)
                            # Check if the current Player's king is now in check
                            check_status = self.check_any()
                            mate_status = self.mate_any()
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):
                                # Revert move and return false
                                self.set_piece(position_original, Piece)
                                self.set_piece(position_new, None)
                                self.set_piece(P_ep_p, ep_p)
                                return False
                            self.taken.append(ep_p)
                            checks = True in [check_store[1] for check_store in list(check_status.items())]
                            mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                            move = History.Move.Move(white_move, Piece, position_original, position_new, True,
                                                     ep_p, checks, mates, None)
                            self.log.add_move(move)
                            return True
                        else:
                            Piece_t = None
                            # Get information about position_new
                            position_new_store = self.get_piece(position_new)
                            # Check if there is a piece at position_new
                            take = position_new_store[0]
                            if take:
                                # Get object of piece at position_new
                                Piece_t = position_new_store[1]
                            # Make proposed move from position_original to position_new
                            self.set_piece(position_new, Piece)
                            self.set_piece(position_original, None)
                            # Check if the current Player's king is now in check
                            check_status = self.check_any()
                            mate_status = self.mate_any()
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):

                                # Revert move and return false
                                self.set_piece(position_original, Piece)
                                self.set_piece(position_new, None)
                                if take:
                                    self.set_piece(position_new, Piece_t)
                                return False
                            if take:
                                self.taken.append(Piece_t)
                            checks = True in [check_store[1] for check_store in list(check_status.items())]
                            mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                            move = History.Move.Move(white_move, Piece, position_original, position_new, True,
                                                     Piece_t, checks, mates, None)
                            self.log.add_move(move)
                            return True


                elif Piece.type == 'K':
                    castle_check = abs(position_new.x - position_original.x) == 2
                    if castle_check:
                        # Check if last move was check
                        if self.log.get_last_move().check:
                            return False
                        else:
                            # Move king
                            self.set_piece(position_new, Piece)
                            self.set_piece(position_original, None)
                            # Compute position_original and position_new for rook, as well as side
                            castle_type = ''
                            if (position_new.x > position_original.x):
                                position_rook_original = Position.Position(7, position_original.y)
                                position_rook_new = Position.Position(4, position_original.y)
                                if white_move:
                                    castle_type = 'Q'
                                else:
                                    castle_type = 'K'
                            else:
                                position_rook_original = Position.Position(0, position_original.y)
                                position_rook_new = Position.Position(2, position_original.y)
                                if white_move:
                                    castle_type = 'K'
                                else:
                                    castle_type = 'Q'
                            # Move rook
                            self.set_piece(position_rook_new, self.get_piece(position_rook_original))
                            self.set_piece(position_rook_original, None)
                            check_status = self.check_any()
                            mate_status = self.check_any()
                            checks = True in [check_store[1] for check_store in list(check_status.items())]
                            mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):
                                # Revert move and return false
                                self.set_piece(position_rook_original, self.get_piece(position_rook_new))
                                self.set_piece(position_original, self.get_piece(position_new))
                                self.set_piece(position_rook_new, None)
                                self.set_piece(position_new, None)
                                return False
                            move = History.Move.Move(white_move, Piece, position_original, position_new, False,
                                                     None, checks, mates, castle_type)
                            self.log.add_move(move)
                            return True
                    else:
                        # Normal move
                        Piece_t = None
                        # Get information about position_new
                        position_new_store = self.get_piece(position_new)
                        # Check if there is a piece at position_new
                        take = position_new_store[0]
                        if take:
                            # Get object of piece at position_new
                            Piece_t = position_new_store[1]
                        # Make proposed move from position_original to position_new
                        self.set_piece(position_new, Piece)
                        self.set_piece(position_original, None)
                        # Check if the current Player's king is now in check
                        check_status = self.check_any()
                        mate_status = self.mate_any()
                        if (white_move and check_status['w'] or
                                    not white_move and check_status['b']):

                            # Revert move and return false
                            self.set_piece(position_original, Piece)
                            self.set_piece(position_new, None)
                            if take:
                                self.set_piece(position_new, Piece_t)
                            return False
                        if take:
                            self.taken.append(Piece_t)
                        checks = True in [check_store[1] for check_store in list(check_status.items())]
                        mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                        move = History.Move.Move(white_move, Piece, position_original, position_new, take,
                                                 Piece_t, checks, mates, None)
                        self.log.add_move(move)
                        return True
                # Run normal moves
                else:
                    Piece_t = None
                    # Get information about position_new
                    position_new_store = self.get_piece(position_new)
                    # Check if there is a piece at position_new
                    take = position_new_store[0]
                    if take:
                        # Get object of piece at position_new
                        Piece_t = position_new_store[1]
                    # Make proposed move from position_original to position_new
                    self.set_piece(position_new, Piece)
                    self.set_piece(position_original, None)
                    # Check if the current Player's king is now in check
                    check_status = self.check_any()
                    mate_status = self.mate_any()
                    if (white_move and check_status['w'] or
                                not white_move and check_status['b']):

                        # Revert move and return false
                        self.set_piece(position_original, Piece)
                        self.set_piece(position_new, None)
                        if take:
                            self.set_piece(position_new, Piece_t)
                        return False
                    if take:
                        self.taken.append(Piece_t)
                    checks = True in [check_store[1] for check_store in list(check_status.items())]
                    mates = True in [mate_store[1] for mate_store in list(mate_status.items())]
                    move = History.Move.Move(white_move, Piece, position_original, position_new, True,
                                             Piece_t, checks, mates, None)
                    self.log.add_move(move)
                    return True
            else:
                return False

        else:
            return False

    def move_to_alg(self, move):
        """Convert move object to Algebraic Notation."""
        output = ''

        position_new_notation = self.position_to_notation(move.position_new)

        if (move.castle in list(self.castle.keys())):
            return self.castle[move.castle]

        # Piece type indicator
        if move.Piece.type == 'position':
            # Pawn letter
            output += self.letters[move.position_original.x]

        else:
            # Piece Type
            output += move.Piece.type

            # Knight and Rook Handling
            possible_conflict = {}
            possible_conflict['R'] = self.rook_conflict(move.position_new, move.color)
            possible_conflict['N'] = self.knight_conflict(move.position_new, move.color)

            if move.Piece.type == 'N' and possible_conflict['N'] > 0:
                output += position_new_notation[possible_conflict['N'] - 1]

            if move.Piece.type == 'R' and possible_conflict['R'] > 0:
                output += position_new_notation[possible_conflict['N'] - 1]

        # Take Indicator
        if move.take:
            output += 'x'

        # Final Coordinate
        output += position_new_notation

        # Check Handling
        if move.check:
            # Mate Handling
            if move.mate:
                output += '#'
            else:
                output += '+'

        return output

    def out_of_board(self, position):
        """ Check if given Position is within board."""
        if (position.x < 0 or position.x > 7 or position.y < 0 or position.y > 7):
            return True
        else:
            return False

    # Get piece at position_requested (position requested)
    def get_piece(self, position_requested):
        if self.out_of_board(position_requested):
            return [False]
        data_requested = self.data[position_requested.y][position_requested.x]
        if data_requested != None:
            return [True, data_requested]
        else:
            return [False]

    def set_piece(self, piece_set, data):
        if self.out_of_board(piece_set):
            return False
        else:
            if data != None:
                data.position_current = piece_set
            self.data[piece_set.y][piece_set.x] = data

    def print_board(self):
        output = [['' for x in range(8)] for y in range(8)]
        for i in range(8):
            for j in range(8):
                Piece_r = self.get_piece(position(i, j))
                if Piece_r[0]:
                    if Piece_r[1].color:
                        output[j][i] = self.symbols['white'][Piece_r[1].type]
                    else:
                        output[j][i] = self.symbols['black'][Piece_r[1].type]
                else:
                    if j % 2 == 0:
                        if i % 2 == 0:
                            output[j][i] = self.symbols['black']['S']
                        else:
                            output[j][i] = self.symbols['white']['S']
                    else:
                        if i % 2 == 0:
                            output[j][i] = self.symbols['white']['S']
                        else:
                            output[j][i] = self.symbols['black']['S']
        output.reverse()

        for line in output:
            print(' '.join(line))

    def game_to_alg(self):
        moves = self.log.get_move_history()
        output = []
        for move in moves:
            output.append(self.move_to_alg(move))
        return '\n'.join(output)
