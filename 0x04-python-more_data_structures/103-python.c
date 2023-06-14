#include <Python.h>

/**
 * print_python_bytes - check code
 * @p: list
 * return: none
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	long int i;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %lu bytes:", size + 1);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - check code
 * @p: list
 * return: none
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	int i;
	const char *t;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		t = (((PyListObject *)p)->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, t);
		if (!strcmp(t, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}
