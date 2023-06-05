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
	slow = h;
	fast = h;
	while (fast)
	{
		slow = slow->next;
		fast = (fast->next)->next;
		if (slow == fast)
		{
			slow = h;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
	}
	return (0);
}
