%{ 
#include <stdlib.h> 
%} 

%% 
if|else|while|int|switch|for|char {printf("Valid Keyword\n");}
[-+]?[0-9]* {printf("Valid Integer\n");}
[-+]?[0-9]*[.][0-9]+ {printf("Valid Float\n");}
[a-zA-Z_][a-zA-Z0-9_]* {printf("Valid Identifier\n");}
[0-9_][a-zA-Z0-9_]* {printf("Invalid Identifier\n");}
[ \t\n]+ ;
. {printf("\nlex err\n");}

%% 

int yywrap(void) { 
    return 1; 
} 
