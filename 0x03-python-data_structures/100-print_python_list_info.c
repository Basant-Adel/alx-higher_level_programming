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
	PyListObject *objList = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", objList->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(objList->ob_item[i])->tp_name);
	}
}
