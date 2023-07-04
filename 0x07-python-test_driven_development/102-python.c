#include "Python.h"

/**
 * print_python_string - A function that prints Python strings
 *@p: It's a Python Object
 *Return: void
 */

void print_python_string(PyObject *p)
{
	PyObject *v, *n;

	(void)n;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	n = PyObject_Repr(p);
	v = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(v));
}
