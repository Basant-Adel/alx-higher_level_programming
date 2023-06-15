#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes -> prints some basic info about Python bytes
 *
 * @p: Python Object
*/

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, ii, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);

	for (ii = 0;ii < lim; ii++)
		if (str[ii] >= 0)
			printf(" %02x", str[ii]);
		else
			printf(" %02x", 256 + str[ii]);

	printf("\n");
}

/**
 * print_python_list -> prints some basic info about Python lists
 *
 * @p: Python Object
*/

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (ii = 0; ii < size; ii++)
	{
		obj = ((PyListObject *)p)->ob_item[ii];
		printf("Element %ld: %s\n", ii, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
