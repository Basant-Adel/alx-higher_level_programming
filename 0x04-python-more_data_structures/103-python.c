#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, a;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (a = 0; a < PyList_Size(p); a++)
	{
		item = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - adds a new node at the end of a listint_t list
 * @p: pointer PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, a;
	char *bytes_str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %ld bytes:", size + 1);
	for (i = 0; a < size + 1 && a < 10; a++)
	{
		printf(" %.2x", bytes_str[a] & 0xFF);
	}
	printf("\n");
}
