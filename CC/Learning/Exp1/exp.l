%{ 
#include <stdlib.h> 
void yyerror(char *); 
#include "y.tab.h" 
%} 

%% 
[0-9]+      { 
                return INTEGER; 
            } 
[-+*\n]      return *yytext; 
[ \t]    
    ;       /* skip whitespace */ 
.           yyerror("invalid character"); 
%% 

int yywrap(void) { 
    return 1; 
} 
