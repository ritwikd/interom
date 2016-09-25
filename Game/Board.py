import Piece, Position, History

class Board:
    def __init__(self):
        self.data = [[None] * 8] * 8

        # Use for xy_to_alg conversion
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.castle = {'K': 'O-O', 'Q': 'O-O-O'}
        self.log = History.Log();
        self.taken = []

    def P_to_nt(self, P):
        """Convert """
        return self.letters[P.x] + str(P.y + 1)

    def king_moves(self, white_playing):
        moves = 0
        move_history = self.log.getAll()
        for move in move_history:
            if moves.Piece.type == 'K' and \
                moves.Piece.color == white_playing:
                moves += 1


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

        R_c = map(self.get_piece, Ps_c)

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
        Ps_c += map(lambda n: Position.Position(c_c, n), range(8))
        # Row
        Ps_c += map(lambda n: Position.Position(n, r_c), range(8))

        R_c = map(self.get_piece, Ps_c)

        rooks = []
        for R in R_c:
            if R[0]:
                if R[1].type == 'R':
                    if R[1].color == turn:
                        rooks.append(R[1])

        if (len(rooks) > 1):
            if rooks[0].P_c.x == rooks[1].P_c.x:
                return 2
            else:
                return 1
        else:
            return 0

    def check_any(self):
        check_status = {'w': False, 'b': False}
        return check_status

    def mate_any(self):
        mate_status = {'w': False, 'b': False}
        return mate_status

    def do_move(self, P_o, P_n):
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
                if Piece.type == 'K':
                    castle_check = abs(P_n.x - P_o.x) == 2
                    if castle_check:
                        # Check if last move was check
                        check_cond = self.log.getLast().check
                        if check_cond:
                            return False
                        else:
                            # Move king
                            self.set_piece(P_n, Piece)
                            self.set_piece(P_o, None)
                            # Compute P_o and P_n for rook
                            if (P_n.x > P_o.x):
                                P_rook_o = Position.Position(7, P_o.y)
                                P_rook_n = Position.Position(4, P_o.y)
                            else:
                                P_rook_o = Position.Position(0, P_o.y)
                                P_rook_n = Position.Position(2, P_o.y)
                            # Move rook
                            self.set_piece(P_rook_n, self.get_piece(P_rook_o))
                            self.set_piece(P_rook_o, None)
                    else:
                        # Normal move
                        # TODO: Implement standard king move

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
                    if (white_move and check_status['w'] or
                                not white_move and check_status['b']):

                        # Revert move and return false
                        self.set_piece(P_o, Piece)
                        self.set_piece(P_n, None)
                        if take:
                            self.set_piece(P_n, Piece_t)
                        return False
                    else:
                        if take:
                            self.taken.append(Piece_t)
                        checks = True in map(lambda c_s: c_s[1], check_status.items())
                        mates = True in map(lambda m_s: m_s[1], self.mate_any())
                        move = History.Move(white_move, Piece, P_o, P_n, True,
                                            Piece_t, checks, mates, )
            else:
                return False

        else:
            return False

    def move_to_alg(self, M):
        """Convert move object to Algebraic Notation."""
        output = ''

        P_n_not = self.P_to_nt(M.P_n)

        if (M.castle in self.castle.keys()):
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
            poss_conf['R'] = self.rook_conflict(M.P_n)
            poss_conf['N'] = self.knight_conflict(M.p_n)

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

    def out_of_board(self, P):
        """ Check if given Position is within board."""
        if (P.x < 0 or P.x > 7 or P.y < 0 or P.y > 7):
            return False
        else:
            return True

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
            self.board[P_s.y][P_s.x] = data
