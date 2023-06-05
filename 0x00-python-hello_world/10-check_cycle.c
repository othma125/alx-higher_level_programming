#include "lists.h"

/**
 * check_cycle - check code
 * @h: pointer to head of list
 * Return: boolean
 */
int check_cycle(listint_t *h)
{
	listint_t *fast;

	if (h == NULL || h->next == NULL)
		return (0);
	fast = h;
	while (fast)
	{
		h = h->next;
		fast = (fast->next)->next;
		if (h == fast)
			return (1);
	}
	return (0);
}
