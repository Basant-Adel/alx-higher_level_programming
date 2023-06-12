#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: PyObject
 * Return void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item;
	Py_ssize_t *allocatedObj = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", allocatedObj);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
