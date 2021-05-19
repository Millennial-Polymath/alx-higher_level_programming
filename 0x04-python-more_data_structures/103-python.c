#include  <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - print python lists
 * @pyObject: python list
 *
 * Return: Void
 */

void print_python_list(PyObject *p)
{
	int i, len = 0;

	for (i = 0; *(p + i) != NULL; i++)
	{
		printf("%d", p[i]);
	}
}
