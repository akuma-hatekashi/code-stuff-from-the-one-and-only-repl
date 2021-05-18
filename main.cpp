//
//  main.cpp
//  game_of_24
//
//  Created by Oneta Dara on 5/5/21.
//

#include <iostream>
#include "card.h"
#include "deck.h"
using namespace std;



int main(int argc, const char * argv[]) {
    
    cardPtr  diamond,club,temp_club, temp_diamond, temp_heart;    //card pointers
    Deck diamonds(diamond);  //deck of playing cards takes a card pointer to point at cards in deck
   temp_diamond = diamond;  //pointer to move through deck
   while(temp_diamond!= NULL){
        if(temp_diamond->get_face_card()){
            cout << temp_diamond->get_face_card() << temp_diamond->get_card_suit() << endl;
        }
        else {
            if(temp_diamond->get_card_value() == 1){
                cout << temp_diamond->get_card_value() << temp_diamond->get_card_suit()<< temp_diamond->get_card_ace() << endl;
            }
            else{
            cout << temp_diamond->get_card_value() << temp_diamond->get_card_suit()<< endl;
            }
        }
        temp_diamond= temp_diamond->get_link(); //move to next node
    }
   /* Deck clubs(club);
    temp_club = club;
    while (temp_club != NULL) {
        if(temp_club->get_card_suit() == 'C'){  //for clubs only
        if(temp_club->get_face_card()){
            cout << temp_club->get_face_card() << temp_club->get_card_suit() << endl;
        }
        else {
            if(temp_club->get_card_value() == 1){
                cout << temp_club->get_card_value() << temp_club->get_card_suit()<< temp_club->get_card_ace() << endl;
            }
            else{
            cout << temp_club->get_card_value() << temp_club->get_card_suit()<< endl;
            }
        }
        }
        temp_club= temp_club->get_link();
    
   
}*/
}
