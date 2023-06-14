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
	long int size, i, l;

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
	l = size >= 10 ? 10 : size + 1;
	printf("  first %ld bytes:", l);
	for (i = 0; i < l; i++)
		printf(" %02x", str[i] >= 0 ? str[i] : 256 + str[i]);
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
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (j = 0; j < size; j++)
	{
		obj = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
