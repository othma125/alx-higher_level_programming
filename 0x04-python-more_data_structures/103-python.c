#include <stdio.h>
#include <string.h>
#include <Python.h>
/**
 * print_python_bytes - check code
 * @p: python object
 * Return: none
 **/
void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t len, i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &s, &len);
	printf("  size: %lu\n", len);
	printf("  trying string: %s\n", s);
	len = len > 10 ? 10 : len + 1;
	printf("  first %lu bytes: ", len);
	for (i = 0; i < len - 1; i++)
		printf("%02x ", s[i] & 0xff);
	printf("%02x\n", s[len - 1] & 0xff);
}
/**
 * print_python_list - check code
 * @p: python object
 * Return: none
 **/
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *list;

	if (PyList_Check(p) != NULL)
		return;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		list = PySequence_GetItem(p, i);
		printf("Element %lu: %s\n", i, list->ob_type->tp_name);
		if (strcmp(list->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list);
	}
}
