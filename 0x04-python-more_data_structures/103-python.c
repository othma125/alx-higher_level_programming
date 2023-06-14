#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - check code
 * @p: Python Object
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, j, l;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	l = size >= 10 ? 10 : size + 1;
	printf("  first %ld bytes:", l);
	for (j = 0; j < l; j++)
		printf(" %02x", str[j] >= 0 ? str[j] : 256 + str[j]);
	printf("\n");
}

/**
 * print_python_list - check code
 * @p: Python Object
 * Return: none
 */
void print_python_list(PyObject *p)
{
	long int size;
	long int j;
	PyObject *obj;
	PyListObject *list;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (j = 0; j < size; j++)
	{
		obj = list->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
