#include "lists.h"
/**
 * check_cycle -  checks for a loop in a linked list
 * @list: head pointer to the list
 *
 * Return: 1 when the cycle is present and 0 if abscent
 */

int check_cycle(listint_t *list)
{
	listint_t *slowPtr = list, *fastPtr = list;

	if (list == NULL)
		return (0);



	while (slowPtr && fastPtr && fastPtr->next)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
			return (1);
	}
		return (0);
}
