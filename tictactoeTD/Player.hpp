class Player{
    private:
        char board[3][3] = {{' ',' ',' '},
                            {' ',' ',' '},
                            {' ',' ',' '}};
    public:
        Player();
        bool isBoardClear();
        char placePeice(int x, int y,char p);
        bool displayBoard();
        bool checkWin(char p);
};