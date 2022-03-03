%{
#include<stdlib.h>
#include<stdio.h>
int yylex(void);
void yyerror(char*);
%}

%token NUM

%%
program:
        program STATEMENT  
        |
        ;
STATEMENT: 
        E '\n' { printf(" Value of Expression is = %d \n",$1); }
        ;
E : 
        E '+' E { $$=$1 + $3; }
        | E '-' E { $$=$1 - $3; }
        | NUM { $$=$1; }
        ;
%%

void yyerror(char* s)
{
fprintf(stderr,"%s",s);
}
int main()
{
yyparse();
return 0;
}