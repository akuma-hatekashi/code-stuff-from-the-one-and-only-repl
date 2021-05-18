//
//  card.cpp
//  game_of_24
//
//  Created by Oneta Dara on 5/5/21.
//

#include "card.h"
#include <iostream>
using namespace std; 


Card ::  Card() : number(0), link(NULL){
    
    //default consrtuct for node or list
    
}
Card :: Card(int value, char suit, Card* next): number(value), suit(suit), link(next){
    //constructor for card node
}
Card :: Card(int value, char suit, char ace, Card* next): number(value), suit(suit), ace(ace), link(next){
        //constructor for the ace cards
}
Card :: Card (char value, char suit, Card* next) : number(10), face_card(value), suit(suit), link(next){
    
}
int Card :: get_card_value(){
    return number;
}
char Card :: get_card_ace(){
    return ace;
}
char Card :: get_card_suit(){
    return suit; 
}
char Card:: get_face_card(){
    return face_card;
}
void Card :: set_link(Card* next){
    link = next; 
}

Card* Card :: get_link(){
    return link;  
}




