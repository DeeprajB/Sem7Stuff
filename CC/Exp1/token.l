%{
int count1,count2;
%}

digit   [0-9]
alpha   [a-zA-Z]

%%

{alpha}({alpha}|{digit})*     { printf("\nvariable=%s",yytext); }            
({digit})+		      		{ printf("\nNumber=%s",yytext);  }                           

%%

int yywrap(void)
{  return 0; } 

int main()
{

yylex();

return 0;
}


