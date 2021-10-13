%{ 
int yylex(void); 
void yyerror(char *);
#include<stdio.h> 
%}
 
%token INTEGER 

%% 
program: 
        program expr '\n'         { printf("Valid Expression"); } 
        |  
        ; 
expr: 
        INTEGER                  {            } 
        | expr '+' expr           {             }   
        | expr '*' expr           {             } 
	| expr '-' expr		{             } 
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

