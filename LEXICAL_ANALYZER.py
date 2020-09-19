#include <stdio.h>
#include <ctype.h>
#include <string.h>

void main ()
{
  char keyword[32][10] =
    { "auto", "double", "int", "struct", "break", "float", "continue", "char",
"if", "else",
    "long", "switch", "case", "enum", "register", "typedef", "extern",
      "return", "union", "const", "short",
    "unsigned", "signed", "void", "default", "goto", "sizeof", "while",
      "volatile", "do", "static", "for"
  };
  FILE *fp;
  int i, j;
  char buff[50], ch, b[20], flag;
  fp = fopen ("inp.txt", "r");
  ch = fgetc (fp);
  while (ch != EOF)
    {
      if (isalpha (ch))
	{
	  i = 0;
	  b[i] = ch;
	  i++;
	  ch = fgetc (fp);
	  while (isalpha (ch) || isdigit (ch) || ch == '_')
	    {
	      b[i] = ch;
	      i++;
	      ch = fgetc (fp);
	    }
	  b[i] = '\0';
	  flag = 0;
	  for (i = 0; i < 32; i++)
	    {
	      if (strcmp (b, keyword[i]) == 0)
		{
		  flag = 1;
		  break;
		}

	    }
	  if (flag == 1)
	    {
	      printf ("%s is a keyword\n", b);

	    }
	  else
	    {
	      printf ("%s is an identifier\n", b);
	    }
	}
      else if (isdigit (ch))
	{
	  while (isdigit (ch))
	    {
	      printf ("%c", ch);
	      ch = fgetc (fp);
	    }
	  printf ("is a constant \n");

	}
      else if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%'
	       || ch == '=')
	{
	  printf ("%c is an operator\n", ch);
	  ch = fgetc (fp);
	}
      else if (ch == '#')
	{
	  fgets (buff, 50, fp);
	  ch = fgetc (fp);


	}
      else if (ch == '(' || ch == ')')
	{
	  printf ("%c is a special character\n", ch);
	  ch = fgetc (fp);

	}
      else if (ch == '||' || ch == '&&' || ch == '!')
	{
	  printf ("%c is a logical operator\n", ch);
	  ch = fgetc (fp);
	}
      else
	{
	  ch = fgetc (fp);
	}

    }

