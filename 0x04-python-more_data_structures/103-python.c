#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list- Prints some basic info about Python lists.
 * @p: PyObject
 */

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
		if (!strcmp(PyList_GET_ITEM(p, i)->ob_type->tp_name, "bytes"))
			print_python_bytes(PyList_GET_ITEM(p, i));
	}
}

/**
 * print_python_bytes - prints some basic info about python lists
 * @p: address of pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	int i, bshow;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %li\n", PyBytes_Size(p));
	if (PyBytes_Size(p) > 0)
	{
		printf("  trying string: %s\n", PyBytes_AsString(p));

		bshow = PyBytes_Size(p) + 1;
		if (bshow > 10)
			bshow = 10;
			printf("  first %d bytes:", bshow);
			for (i = 0; i < bshow; i++)
			{
				printf(" %02x", (unsigned char)*(PyBytes_AsString(p) + i));
			}
			printf("\n");
	}
}
