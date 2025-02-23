#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * 
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *a, *b;

    if (list == NULL || list->next == NULL)
        return (0);
    b = list;
    a = list->next->next;
    
    while (b != a)
    {
        if (a == NULL || a->next == NULL)
            return (0);
        a = a->next->next;
        b = b->next;
    }

    return (1);
}
