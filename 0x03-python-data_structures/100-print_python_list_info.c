#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - check code
 * @p: PyObject
 *Return: none
 */

void print_python_list_info(PyObject *p)
{
	long int size = Py_SIZE(p);
	long int i = 0;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
