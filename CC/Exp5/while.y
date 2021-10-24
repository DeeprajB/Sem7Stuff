%{ 
int yylex(void); 
void yyerror(char *);
#include<stdio.h> 
%}
 
%token WHILE ID G L GE LE 

%% 
program: 
        program STATEMENT         { printf("Valid Expression \n"); } 
        |  
        ;

STATEMENT:
        START '(' COND ')' '{' STAT ';' '}'
        ;
START:
        WHILE
        ;
COND:
        ID RELOP ID
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

