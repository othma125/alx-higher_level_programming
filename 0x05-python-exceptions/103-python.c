#include <Python.h>
/**
 * print_python_list - check code
 * @p: python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allctd, i;
	const char *type;
	PyVarObject *var_obj = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;

	size = var_obj->ob_size;
	allctd = list->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allctd);
	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - check code
 * @p: python list object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, j;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes: ", size);
	for (j = 0; j < size; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		printf("%c", j == size - 1 ? '\n' : ' ');
	}
}
/**
 * print_python_float - check code
 * @p: python list object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;
	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
