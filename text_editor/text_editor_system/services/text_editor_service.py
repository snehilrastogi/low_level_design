from text_editor_system.models.node import Node
from text_editor_system.services.base_service import BaseService


class TextEditorService(BaseService):
    @classmethod
    def display_editor_obj(cls, editor_obj):
        if editor_obj.head is None:
            print ("No object ....")
            return

        else:
            print ("total count--", editor_obj.count)
            if editor_obj.head:
                print ("if editor_obj.head -- data ", editor_obj.head.data, "index --", editor_obj.head.index)

            if editor_obj.tail:
                print ("if editor_obj.tail -- data ", editor_obj.tail.data, "index --", editor_obj.tail.index)

            if editor_obj.clipboard_head:
                print ("if editor_obj.clipboard_head -- data ", editor_obj.clipboard_head.data, "index --", editor_obj.clipboard_head.index)

            if editor_obj.clipboard_tail:
                print ("if editor_obj.clipboard_tail -- data ", editor_obj.clipboard_tail.data, "index --",
                       editor_obj.clipboard_tail.index)

    @classmethod
    def display(cls, editor_obj, start=-1, end=-1):
        if editor_obj.head is None:
            print ("FIle is empty ....")
            return
        node = editor_obj.head
        tail_node = editor_obj.tail
        count = editor_obj.count
        if start < 0:
            print("display whole file")
            while node is not None:
                print ("data -- ", node.data, "index --", node.index)
                node = node.next
        else:
            if start > end:
                print("Not these many lines")
                return
            while node is not None:
                if node.index == start:
                    while node is not None and node.index != end:
                        print ("data -- ", node.data, "index --", node.index)
                        node = node.next
                    if node and node.index == end:
                        print("data -- ", node.data, "index --", node.index)
                    else:
                        print ("upto only,", tail_node.index, "are present ")
                    break
                node = node.next

    @classmethod
    def delete_one_line(self, editor_obj, n):
        if editor_obj.head is None:
            print ("FIle is empty ....")
            return
        node = editor_obj.head
        count = editor_obj.count
        if n > count or n < 0:
            print("Not these lines present, count --", count)
            return
        while node is not None:
            if node.index == n:
                temp = node.prev
                next_node = node.next
                if temp is None and next_node is None:
                    editor_obj.head = None
                    editor_obj.tail = None
                    editor_obj.count = 0
                    p = node
                    # editor_obj.save()
                elif node == editor_obj.head:
                    editor_obj.head = node.next
                    # if node.next:
                    node.next.prev = None
                    p = node
                    editor_obj.count -= 1
                    # editor_obj.save()
                elif node == editor_obj.tail:
                    temp.next = node.next
                    p = node
                    editor_obj.tail = temp
                    # node=node.next
                    editor_obj.count -= 1
                    # editor_obj.save()
                else:
                    temp.next = next_node
                    next_node.prev = temp
                    p = node
                    editor_obj.count -= 1
                    # editor_obj.save()

                editor_obj.clipboard_head = p
                node.prev = None
                node.next = None
                editor_obj.clipboard_tail = p
                editor_obj.count = editor_obj.count-1
                # editor_obj.save()
                return

            else:
                node = node.next

    @classmethod
    def delete_range(self, editor_obj, n, m):
        if editor_obj.head is None:
            print ("FIle is empty ....")
            return
        node = editor_obj.head
        count = editor_obj.count
        if n > count or n < 0:
            print("Not these lines present")
            return
        if m < 0 or m < n:
            print("Wrong Data")
            return

        while node is not None:
            if node.index == n:
                temp = node.prev
                editor_obj.clipboard_head = node
                while node is not None or node.index != m:
                    node = node.next
                if temp is None and node is None:
                    editor_obj.head = None
                    editor_obj.tail = None
                    editor_obj.count = 0
                    p = node

                elif node == editor_obj.head:
                    editor_obj.head = node.next
                    node.next.prev = None
                    editor_obj.count = m - n + 1
                    p = node

                elif node == editor_obj.tail:
                    temp.next = node.next
                    p = node
                    editor_obj.tail = temp
                    editor_obj.count = m - n + 1
                    # editor_obj.save()


                else:
                    temp.next = node.next
                    node.next.prev = temp
                    editor_obj.count = m - n + 1
                    editor_obj.save()
                    p = node
                editor_obj.clipboard_tail = p
                # editor_obj.save()
            else:
                node = node.next

    @classmethod
    def insert(cls, editor_obj, n, text):
        new_node = Node(text)
        if editor_obj.head is None:
            new_node.index = 0
            # new_node.save()
            editor_obj.head = new_node
            editor_obj.tail = new_node
            editor_obj.clipboard_head = new_node
            editor_obj.clipboard_tail = new_node
            editor_obj.count+=1
            # editor_obj.save()

        else:
            node = editor_obj.head
            while node is not None and node.index != n - 1:
                node = node.next

            if node is None or node == editor_obj.tail:
                editor_obj.tail.next = new_node
                new_node.index = editor_obj.tail.index + 1
                new_node.prev = editor_obj.tail
                editor_obj.tail = new_node
                editor_obj.clipboard_head = new_node
                editor_obj.clipboard_tail = new_node
                editor_obj.count += 1
                # editor_obj.save()
                # new_node.save()
            else:
                temp = node.next
                node.next = new_node
                new_node.index = n
                new_node.next = temp
                temp.prev = new_node
                editor_obj.clipboard_head = new_node
                editor_obj.clipboard_tail = new_node
                editor_obj.count += 1
                # editor_obj.save()
                # new_node.save()

    @classmethod
    def copy_data(cls, editor_obj, n, m):
        if editor_obj.head is None:
            print ("File is empty ....")
            return
        node = editor_obj.head
        count = editor_obj.count
        if n > count or n < 0:
            print("Not these lines present")
            return
        if m < 0 or m > n:
            print("Wrong Data")
            return
        while node is not None or node.index != n:
            node = node.next

        temp = node.prev
        editor_obj.clipboard_head = node
        while node is not None and node.index != m:
            node = node.next

        if node is None:
            editor_obj.clipboard_tail = editor_obj.tail
        else:
            editor_obj.clipboard_tail = node
        # editor_obj.save()

    @classmethod
    def paste(cls, editor_obj, n):
        temp = editor_obj.clipboard_head
        if temp is None:
            n = 0
            TextEditorService.insert(editor_obj, n, temp.data)
        temp = editor_obj.clipboard_head
        m = editor_obj.clipboard_tail.index
        while temp.index != m and temp is not None:
            TextEditorService.insert(editor_obj, n, temp.data)
            temp = temp.next

    @classmethod
    def undo(cls, editor_obj, undo_stack):
        if undo_stack is None:
            print ("nothing to undo")
            return
        tup = undo_stack.pop()
        # print ("UNDOed data -- ", tup)
        # if 'insert' in tup[0]:
        #     TextEditorService.insert(editor_obj, tup[1], editor_obj.clipboard_head.data)

    @classmethod
    def redo(cls, editor_obj, redo_stack):
        if redo_stack is None:
            print ("nothing to redo")
            return
        tup = redo_stack.pop()

        print ("REDOed data -- ", tup)

        if 'empty' in tup[0].lower():
            print("can't redo")
            return

        if 'insert' in tup[0].lower():
            TextEditorService.insert(editor_obj, tup[1], editor_obj.clipboard_head.data)

        elif 'delete' in tup[0].lower():
            if tup[2] < 0:
                TextEditorService.delete_one_line(editor_obj, tup[1])
            else:
                TextEditorService.delete_range(editor_obj, tup[1], tup[2])

        elif 'copy' in tup[0].lower():
            TextEditorService.copy_data(editor_obj, tup[1], tup[2])

        elif 'paste' in tup[0].lower():
            TextEditorService.paste(editor_obj, tup[1])

        elif 'display' in tup[0].lower():
            TextEditorService.display(editor_obj, tup[1], tup[2])
