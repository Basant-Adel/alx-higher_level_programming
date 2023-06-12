#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: PyObject
 * Return void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *obj = ((PyListObject *)p);

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
