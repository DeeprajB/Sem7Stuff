%{ 
int yylex(void); 
void yyerror(char *);
#include<stdio.h> 
%}
 
%token FOR ID NUM G L GE LE 

%% 
program: 
        program STATEMENT         { printf("Valid Expression \n"); } 
        |  
        ;

STATEMENT:
        START '(' COND ')' '{' STAT ';' '}'
        ;
START:
        FOR
        ;
COND:
        ID ';' ID RELOP NUM ';' ID '+' '+'
        |ID ';' ID RELOP NUM ';' ID '-' '-'
        ;

RELOP:
        G
        |L
        |GE
        |LE
        ;

STAT:
        ID '=' EXP
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