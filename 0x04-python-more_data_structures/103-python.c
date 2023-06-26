#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes -> prints some basic info about Python bytes
 *@p: Python Object
*/

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, oh, lim;

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

	for (oh = 0;oh < lim; oh++)
		if (str[oh] >= 0)
			printf(" %02x", str[oh]);
		else
			printf(" %02x", 256 + str[oh]);

	printf("\n");
}

/**
 * print_python_list -> prints some basic info about Python lists
 *@p: Python Object
*/

void print_python_list(PyObject *p)
{
	long int size, oh;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (oh = 0; oh < size; oh++)
	{
		obj = ((PyListObject *)p)->ob_item[oh];
		printf("Element %ld: %s\n", oh, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
