%{ 
int yylex(void); 
void yyerror(char *);
#include<stdio.h> 
%}
 
%token FOR WHILE ID NUM G L GE LE 

%% 
program: 
        program STATEMENT         { printf("Valid Expression \n"); } 
        |  
        ;

STATEMENT:
        STARTF '(' COND ')' '{' STAT STATEMENT '}'
        |STARTW '(' CONDW ')' '{' STAT STATEMENT '}'
        |
        ;
STARTF:
        FOR
        ;
STARTW:
        WHILE
        ;
COND:
        ID ';' ID RELOP NUM ';' ID '+' '+'
        |ID ';' ID RELOP NUM ';' ID '-' '-'
        ;
CONDW:
        ID RELOP ID
        ;

RELOP:
        G
        |L
        |GE
        |LE
        ;

STAT:
        ID '=' EXP ';' ID '=' EXP ';' STAT1
        ;

STAT1:
        ID '=' EXP ';' STAT1
        |
        ;

EXP:
        ID EXPD
        ;

EXPD:
        '+' EXP EXPD
        |'-' EXP EXPD
        |'*' EXP EXPD
        |
        ;


%% 

void yyerror(char *s) { 
   fprintf(stderr, "%s\n", s); 
    //return 0; 
} 

int main(void) { 
    yyparse(); 
    return 0; 
} 

