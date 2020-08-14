#include "Player.hpp"
#include <iostream>


Player::Player() {
    
}

bool Player::isBoardClear(){
 for (int i = 0; i < 3; ++i) 
    { 
        for (int j = 0; j < 3; ++j) 
        { 
            if(board[i][j] != ' '){
                return false;
            }
        } 
        
    } 
    return true;
}

char Player::placePeice(int x, int y, char p){
    board[x][y] = p;
    return p;
}

bool Player::displayBoard(){
    for (int i = 0; i < 3; ++i) 
    { 
        for (int j = 0; j < 3; ++j) 
        { 
            std::cout << board[i][j] << " ";
        } 
        std::cout << std::endl;
    } 
    return true; 
} 
bool Player::checkWin(char p){
    bool ret = false;
    bool isRow;
    bool isColumn;

    for (int i = 0; i < 3; ++i) 
    { 
        isRow = true;
        isColumn = true;
        for (int j = 0; j < 3; ++j) 
        { 
            if(board[i][j] != p){
                isRow = false;

            }
            if(board[j][i] != p){
                isColumn = false;
            }
        } 
        if(isColumn || isRow){
            ret = true;
            break;
        }
    } 
    if( board[0][0] == p && 
        board[1][1] == p &&
        board[2][2] == p 
    ){
            ret = true; 
    }

    if( board[0][2] == p && 
        board[1][1] == p &&
        board[2][0] == p
    ){
            ret = true; 
    }

    
    return ret;
}