%{
#include "y.tab.h"
#include<stdio.h>
%}

%%
[\t ]+ /* ignore the blank spaces */ ;
[-+*=\n,;(){}] { return *yytext; }
[a-zA-Z]+ { // return valid tokens to yacc program
yylval.string_value = strdup(yytext );
return ID;
};
[0-9]+ { // return valid tokens to yacc program
yylval.string_value = strdup(yytext );
return INTEGER;
};
%%