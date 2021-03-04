# -*- coding: utf-8 -*-

from . import History, Pieces, Position

P = Position.Position

STARTING_POSITION = {

    'white': {
        # Main Pieces
        'king': P(4, 0),
        'queen': P(3, 0),
        'rook1': P(0, 0),
        'rook2': P(7, 0),
        'knight1': P(1, 0),
        'knight2': P(6, 0),
        'bishop1': P(2, 0),
        'bishop2': P(5, 0),
        # Pawns
        'pawnA': P(0, 1),
        'pawnB': P(1, 1),
        'pawnC': P(2, 1),
        'pawnD': P(3, 1),
        'pawnE': P(4, 1),
        'pawnF': P(5, 1),
        'pawnG': P(6, 1),
        'pawnH': P(7, 1)
    },

    'black': {
        # Main Pieces
        'king': P(4, 7),
        'queen': P(3, 7),
        'rook1': P(0, 7),
        'rook2': P(7, 7),
        'knight1': P(1, 7),
        'knight2': P(6, 7),
        'bishop1': P(2, 7),
        'bishop2': P(5, 7),
        # Pawns
        'pawnA': P(0, 6),
        'pawnB': P(1, 6),
        'pawnC': P(2, 6),
        'pawnD': P(3, 6),
        'pawnE': P(4, 6),
        'pawnF': P(5, 6),
        'pawnG': P(6, 6),
        'pawnH': P(7, 6)
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
                'O-O': [P(4,0), P(6,0)],
                'O-O-O' : [P(4,0), P(2,0)]
            },
            False: {
                'O-O': [P(4,7), P(6,7)],
                'O-O-O': [P(4,7), P(2,7)]
            }
        }

        self.types = ['K','Q','R','B','N']
        self.log = History.Log.Log()
        self.taken = []

    def P_to_nt(self, P):
        """Convert """
        return self.letters[P.x] + str(P.y + 1)

    def set_start_pos(self):

        K = Pieces.Other.King.King
        Q = Pieces.Major.Queen.Queen
        R = Pieces.Major.Rook.Rook
        B = Pieces.Minor.Bishop.Bishop
        N = Pieces.Minor.Knight.Knight
        Pl = Pieces.Other.Pawn.Pawn

        P_s_board = STARTING_POSITION
        pieces_to_add = []

        # Add white Pieces
        pieces_to_add.append(K(self, P_s_board['white']['king'], True))

        pieces_to_add.append(Q(self, P_s_board['white']['queen'], True))

        pieces_to_add.append(R(self, P_s_board['white']['rook1'], True))
        pieces_to_add.append(R(self, P_s_board['white']['rook2'], True))

        pieces_to_add.append(B(self, P_s_board['white']['bishop1'], True))
        pieces_to_add.append(B(self, P_s_board['white']['bishop2'], True))

        pieces_to_add.append(N(self, P_s_board['white']['knight1'], True))
        pieces_to_add.append(N(self, P_s_board['white']['knight2'], True))

        pieces_to_add.append(Pl(self, P_s_board['white']['pawnA'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnB'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnC'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnD'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnE'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnF'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnG'], True))
        pieces_to_add.append(Pl(self, P_s_board['white']['pawnH'], True))

        # Add black Pieces

        pieces_to_add.append(K(self, P_s_board['black']['king'], False))

        pieces_to_add.append(Q(self, P_s_board['black']['queen'], False))

        pieces_to_add.append(R(self, P_s_board['black']['rook1'], False))
        pieces_to_add.append(R(self, P_s_board['black']['rook2'], False))

        pieces_to_add.append(B(self, P_s_board['black']['bishop1'], False))
        pieces_to_add.append(B(self, P_s_board['black']['bishop2'], False))

        pieces_to_add.append(N(self, P_s_board['black']['knight1'], False))
        pieces_to_add.append(N(self, P_s_board['black']['knight2'], False))

        pieces_to_add.append(Pl(self, P_s_board['black']['pawnA'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnB'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnC'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnD'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnE'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnF'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnG'], False))
        pieces_to_add.append(Pl(self, P_s_board['black']['pawnH'], False))

        for piece in pieces_to_add:
            self.set_piece(piece.P_c, piece)

    def knight_conflict(self, P_n, turn):
        Ps_c = []

        Ps_c.append(Position.Position(P_n.x + 1, P_n.y + 2))
        Ps_c.append(Position.Position(P_n.x + 2, P_n.y + 1))
        Ps_c.append(Position.Position(P_n.x + 2, P_n.y - 1))
        Ps_c.append(Position.Position(P_n.x + 1, P_n.y - 2))

        Ps_c.append(Position.Position(P_n.x - 1, P_n.y + 2))
        Ps_c.append(Position.Position(P_n.x - 2, P_n.y + 1))
        Ps_c.append(Position.Position(P_n.x - 2, P_n.y - 1))
        Ps_c.append(Position.Position(P_n.x - 1, P_n.y - 2))

        R_c = list(map(self.get_piece, Ps_c))

        knights = []
        for R in R_c:
            if R[0]:
                if R[1].type == 'N':
                    if R[1].color == turn:
                        knights.append(R[1])

        if (len(knights) > 1):
            if knights[0].P_c.x == knights[1].P_c.x:
                return 2
            else:
                return 1
        else:
            return 0

    def rook_conflict(self, P_n, turn):
        Ps_c = []

        c_c = P_n.x
        r_c = P_n.y

        # Column
        Ps_c += [Position.Position(c_c, n) for n in range(8)]
        # Row
        Ps_c += [Position.Position(n, r_c) for n in range(8)]

        R_c = list(map(self.get_piece, Ps_c))

        rooks = []
        for R in R_c:
            if R[0]:
                if R[1].type == 'R':
                    if R[1].color == turn:
                        rooks.append(R[1])

        for rook in rooks:
            if not rook.valid_move(P_n):
                return 0

        if (len(rooks) > 1):
            if rooks[0].P_c.x == rooks[1].P_c.x:
                return 2
            else:
                return 1
        else:
            return 0

    def potential_check_square(self, P_p_c, C_p_c):
        # Determine if position could potentially be in check
        for rank in self.data:
            for square in rank:
                if square != None:
                    if square.color != C_p_c:
                        if square.valid_move(P_p_c):
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
                            p_kings['w'] = square.P_c
                        else:
                            p_kings['b'] = square.P_c

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


    def do_move(self, P_o, P_n, S_i):
        """Move piece from Position Orig (P_o) to Position New (P_n) """

        # Get information about P_o
        R_P_o = self.get_piece(P_o)
        if R_P_o[0]:
            # Get object and color of piece at P_o
            Piece = R_P_o[1]
            white_move = Piece.color
            # Check if P_n is a valid move for Piece at P_o
            if Piece.valid_move(P_n):
                # Check for castling
                if Piece.type == 'P':
                    Piece_t = None
                    R_P_n = self.get_piece(P_n)
                    # Check if there is a piece at P_n
                    take = R_P_n[0]
                    if take:
                        # Get object of piece at P_n
                        Piece_t = R_P_n[1]
                        Piece_t = None
                        # Get information about P_n
                        R_P_n = self.get_piece(P_n)
                        # Check if there is a piece at P_n
                        take = R_P_n[0]
                        if take:
                            # Get object of piece at P_n
                            Piece_t = R_P_n[1]
                        # Make proposed move from P_o to P_n
                        self.set_piece(P_n, Piece)
                        self.set_piece(P_o, None)
                        # Check if the current Player's king is now in check
                        check_status = self.check_any()
                        mate_status = self.mate_any()
                        if (white_move and check_status['w'] or
                                    not white_move and check_status['b']):

                            # Revert move and return false
                            self.set_piece(P_o, Piece)
                            self.set_piece(P_n, None)
                            if take:
                                self.set_piece(P_n, Piece_t)
                            return False
                        if take:
                            self.taken.append(Piece_t)
                        checks = True in [c_s[1] for c_s in list(check_status.items())]
                        mates = True in [m_s[1] for m_s in list(mate_status.items())]
                        move = History.Move.Move(white_move, Piece, P_o, P_n, True,
                                                 Piece_t, checks, mates, None)
                        self.log.add_move(move)
                        return True
                    else:
                        ep_check = abs(P_n.y - P_o.y) == 1 and abs(P_n.x - P_o.x) == 1
                        if ep_check:
                            P_ep_p = P(P_n.x, P_o.y)
                            ep_p = self.get_piece(P_ep_p)[1]
                            self.set_piece(P_n, Piece)
                            self.set_piece(P_o, None)
                            self.set_piece(P_ep_p, None)
                            # Check if the current Player's king is now in check
                            check_status = self.check_any()
                            mate_status = self.mate_any()
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):
                                # Revert move and return false
                                self.set_piece(P_o, Piece)
                                self.set_piece(P_n, None)
                                self.set_piece(P_ep_p, ep_p)
                                return False
                            self.taken.append(ep_p)
                            checks = True in [c_s[1] for c_s in list(check_status.items())]
                            mates = True in [m_s[1] for m_s in list(mate_status.items())]
                            move = History.Move.Move(white_move, Piece, P_o, P_n, True,
                                                     ep_p, checks, mates, None)
                            self.log.add_move(move)
                            return True
                        else:
                            Piece_t = None
                            # Get information about P_n
                            R_P_n = self.get_piece(P_n)
                            # Check if there is a piece at P_n
                            take = R_P_n[0]
                            if take:
                                # Get object of piece at P_n
                                Piece_t = R_P_n[1]
                            # Make proposed move from P_o to P_n
                            self.set_piece(P_n, Piece)
                            self.set_piece(P_o, None)
                            # Check if the current Player's king is now in check
                            check_status = self.check_any()
                            mate_status = self.mate_any()
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):

                                # Revert move and return false
                                self.set_piece(P_o, Piece)
                                self.set_piece(P_n, None)
                                if take:
                                    self.set_piece(P_n, Piece_t)
                                return False
                            if take:
                                self.taken.append(Piece_t)
                            checks = True in [c_s[1] for c_s in list(check_status.items())]
                            mates = True in [m_s[1] for m_s in list(mate_status.items())]
                            move = History.Move.Move(white_move, Piece, P_o, P_n, True,
                                                     Piece_t, checks, mates, None)
                            self.log.add_move(move)
                            return True


                elif Piece.type == 'K':
                    castle_check = abs(P_n.x - P_o.x) == 2
                    if castle_check:
                        # Check if last move was check
                        if self.log.get_last_move().check:
                            return False
                        else:
                            # Move king
                            self.set_piece(P_n, Piece)
                            self.set_piece(P_o, None)
                            # Compute P_o and P_n for rook, as well as side
                            castle_type = ''
                            if (P_n.x > P_o.x):
                                P_rook_o = Position.Position(7, P_o.y)
                                P_rook_n = Position.Position(4, P_o.y)
                                if white_move:
                                    castle_type = 'Q'
                                else:
                                    castle_type = 'K'
                            else:
                                P_rook_o = Position.Position(0, P_o.y)
                                P_rook_n = Position.Position(2, P_o.y)
                                if white_move:
                                    castle_type = 'K'
                                else:
                                    castle_type = 'Q'
                            # Move rook
                            self.set_piece(P_rook_n, self.get_piece(P_rook_o))
                            self.set_piece(P_rook_o, None)
                            check_status = self.check_any()
                            mate_status = self.check_any()
                            checks = True in [c_s[1] for c_s in list(check_status.items())]
                            mates = True in [m_s[1] for m_s in list(mate_status.items())]
                            if (white_move and check_status['w'] or
                                        not white_move and check_status['b']):
                                # Revert move and return false
                                self.set_piece(P_rook_o, self.get_piece(P_rook_n))
                                self.set_piece(P_o, self.get_piece(P_n))
                                self.set_piece(P_rook_n, None)
                                self.set_piece(P_n, None)
                                return False
                            move = History.Move.Move(white_move, Piece, P_o, P_n, False,
                                                     None, checks, mates, castle_type)
                            self.log.add_move(move)
                            return True
                    else:
                        # Normal move
                        Piece_t = None
                        # Get information about P_n
                        R_P_n = self.get_piece(P_n)
                        # Check if there is a piece at P_n
                        take = R_P_n[0]
                        if take:
                            # Get object of piece at P_n
                            Piece_t = R_P_n[1]
                        # Make proposed move from P_o to P_n
                        self.set_piece(P_n, Piece)
                        self.set_piece(P_o, None)
                        # Check if the current Player's king is now in check
                        check_status = self.check_any()
                        mate_status = self.mate_any()
                        if (white_move and check_status['w'] or
                                    not white_move and check_status['b']):

                            # Revert move and return false
                            self.set_piece(P_o, Piece)
                            self.set_piece(P_n, None)
                            if take:
                                self.set_piece(P_n, Piece_t)
                            return False
                        if take:
                            self.taken.append(Piece_t)
                        checks = True in [c_s[1] for c_s in list(check_status.items())]
                        mates = True in [m_s[1] for m_s in list(mate_status.items())]
                        move = History.Move.Move(white_move, Piece, P_o, P_n, take,
                                                 Piece_t, checks, mates, None)
                        self.log.add_move(move)
                        return True
                # Run normal moves
                else:
                    Piece_t = None
                    # Get information about P_n
                    R_P_n = self.get_piece(P_n)
                    # Check if there is a piece at P_n
                    take = R_P_n[0]
                    if take:
                        # Get object of piece at P_n
                        Piece_t = R_P_n[1]
                    # Make proposed move from P_o to P_n
                    self.set_piece(P_n, Piece)
                    self.set_piece(P_o, None)
                    # Check if the current Player's king is now in check
                    check_status = self.check_any()
                    mate_status = self.mate_any()
                    if (white_move and check_status['w'] or
                                not white_move and check_status['b']):

                        # Revert move and return false
                        self.set_piece(P_o, Piece)
                        self.set_piece(P_n, None)
                        if take:
                            self.set_piece(P_n, Piece_t)
                        return False
                    if take:
                        self.taken.append(Piece_t)
                    checks = True in [c_s[1] for c_s in list(check_status.items())]
                    mates = True in [m_s[1] for m_s in list(mate_status.items())]
                    move = History.Move.Move(white_move, Piece, P_o, P_n, True,
                                             Piece_t, checks, mates, None)
                    self.log.add_move(move)
                    return True
            else:
                return False

        else:
            return False

    def move_to_alg(self, M):
        """Convert move object to Algebraic Notation."""
        output = ''

        P_n_not = self.P_to_nt(M.P_n)

        if (M.castle in list(self.castle.keys())):
            return self.castle[M.castle]

        # Piece type indicator
        if M.Piece.type == 'P':
            # Pawn letter
            output += self.letters[M.P_o.x]

        else:
            # Piece Type
            output += M.Piece.type

            # Knight and Rook Handling
            poss_conf = {}
            poss_conf['R'] = self.rook_conflict(M.P_n, M.color)
            poss_conf['N'] = self.knight_conflict(M.P_n, M.color)

            if M.Piece.type == 'N' and poss_conf['N'] > 0:
                output += P_n_not[poss_conf['N'] - 1]

            if M.Piece.type == 'R' and poss_conf['R'] > 0:
                output += P_n_not[poss_conf['N'] - 1]

        # Take Indicator
        if M.take:
            output += 'x'

        # Final Coordinate
        output += P_n_not

        # Check Handling
        if M.check:
            # Mate Handling
            if M.mate:
                output += '#'
            else:
                output += '+'

        return output

    def out_of_board(self, P):
        """ Check if given Position is within board."""
        if (P.x < 0 or P.x > 7 or P.y < 0 or P.y > 7):
            return True
        else:
            return False

    # Get piece at P_r (position requested)
    def get_piece(self, P_r):
        if self.out_of_board(P_r):
            return [False]
        data_req = self.data[P_r.y][P_r.x]
        if data_req != None:
            return [True, data_req]
        else:
            return [False]

    def set_piece(self, P_s, data):
        if self.out_of_board(P_s):
            return False
        else:
            if data != None:
                data.P_c = P_s
            self.data[P_s.y][P_s.x] = data

    def print_board(self):
        output = [['' for x in range(8)] for y in range(8)]
        for i in range(8):
            for j in range(8):
                Piece_r = self.get_piece(P(i, j))
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
