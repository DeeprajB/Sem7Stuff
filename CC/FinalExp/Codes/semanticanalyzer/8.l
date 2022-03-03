%{
#include "y.tab.h"
void yyerror(char*);
%}

alpha [a-zA-Z_]
digit [0-9]

%%
{digit}+ { yylval = strtol(yytext, NULL, 10); return NUM; }
[+-,;\n] { return *yytext; }
[ \t] { ; }
. { yyerror("invalid character"); exit(0); }
%%

int yywrap(void)
{ return 1; }