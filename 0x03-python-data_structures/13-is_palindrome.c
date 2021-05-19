#include "lists.h"

int is_palindrome(listint_t **head)
{
	int count= 0, i = 0;
	listint_t  *current, *temp, *nextNode;

	/* Get the middle of a linked list */
	while (head)
	{
		head = head->next;
		count++;
	}
	current = head;
	while (i <= count / 2)
	{
		current = current->next;
		i++;
	}


}
/* reverse the second half of the linked list */

listint_t *reverse(listint_t *head)
{
	listint_t *prev, *current = head, *next;
	while (current)
	{
		next = current->next;
		current->next  = prev;
		prev = current;
		current = next;
	}
	return prev;
}
listint_t *reverse2ndhalf(listint_t *head)
{
	listint_t *fast = head, *slow = head, *prev = NULL;

	while (fast && fast->next)
	{
		prev = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (!fast) prev->next = reverse(slow);
	else  slow->next = reverse(slow->next);
	return head;
}
