%{ 
#include <stdlib.h> 
void yyerror(char *); 
#include "y.tab.h" 
%} 

%% 
"while" { 
                return WHILE;
        } 
"for" { 
                return FOR;
        } 
">" { 
    return G;
    }
"<" { 
    return L;
    }
">=" { 
    return GE;
    }
"<=" { 
    return LE;
    }
[-+*=(){};]    {
                return *yytext;
        }
[ \t\n]+ ;
[0-9]+ { return NUM;}
[a-zA-Z_][a-zA-Z0-9_]* {return ID;}
. {printf("\n\nlex err");}

%% 

int yywrap(void) { 
    return 1; 
} 
