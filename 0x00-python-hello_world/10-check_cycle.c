#include "lists.h"

/**
 * check_cycle - check code
 * @h: pointer to head of list
 * Return: boolean
 */
int check_cycle(listint_t *h)
{
	listint_t *slow, *fast;

	if (h == NULL || h->next == NULL)
		return (0);
	slow = h->next;
	fast = slow->next;
	do {
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = (fast->next)->next;
	} while (fast);
	return (0);
}
