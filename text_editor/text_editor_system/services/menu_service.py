from pip._vendor.distlib.compat import raw_input

from text_editor_system import constants
from text_editor_system.models.editor import Editor
from text_editor_system.services.base_service import BaseService
from text_editor_system.services.text_editor_service import TextEditorService

#TODO: indexes on deletion and insertion
#TODO: UNDO service
class MenuService(BaseService):
    @classmethod
    def print_menu(cls, ):
        editor_obj = Editor()
        ans = True
        undo_stack = []
        redo_stack = []
        while ans:
            print("---- considering 0 based indexing in input ----")
            print ("""
            1. display 2.display(n, m) 3.insert(n, text) 4.delete(n) 5. copy(n, m) 6. paste(n) 7. undo 8.redo 9.delete(n, m)
            10.exit
            """)
            ch = input("enter your choice")

            if ch == 1:
                TextEditorService.display(editor_obj)
                redo_stack.append((constants.DISPLAY, -1, -1))
            elif ch == 2:
                n, m = map(int, raw_input("enter start and end").split(','))
                TextEditorService.display(editor_obj, n, m)
                undo_stack.append((constants.UNDO_MAPPING[constants.INSERT], n, m))
                redo_stack.append((constants.DISPLAY, n, m))

            elif ch == 3:
                n = input("enter line num")
                data = raw_input("enter data")
                TextEditorService.insert(editor_obj, n, data)
                redo_stack.append((constants.INSERT, n, -1))
                undo_stack.append((constants.UNDO_MAPPING[constants.DELETE], n, -1))
            elif ch == 4:
                n = input("enter row to be deleted")
                TextEditorService.delete_one_line(editor_obj, n)
                undo_stack.append((constants.UNDO_MAPPING[constants.DELETE], n, -1))
                redo_stack.append((constants.DELETE, n, -1))

            elif ch == 5:
                n, m = raw_input("enter start and end").split(',')
                TextEditorService.copy_data(editor_obj, n, m)
                undo_stack.append((constants.UNDO_MAPPING[constants.COPY], n, m))
                redo_stack.append((constants.COPY, n, m))

            elif ch == 6:
                n = input("enter line num")
                TextEditorService.paste(editor_obj, n)
                undo_stack.append((constants.UNDO_MAPPING[constants.PASTE], n, -1))
                redo_stack.append((constants.PASTE, n, -1))

            elif ch == 7:
                TextEditorService.undo(editor_obj, undo_stack)
                undo_stack.append((constants.UNDO_MAPPING[constants.UNDO], -1, -1))
                redo_stack.append((constants.UNDO_MAPPING[constants.REDO], -1, -1))
            elif ch == 8:
                TextEditorService.redo(editor_obj, redo_stack)
                undo_stack.append((constants.UNDO_MAPPING[constants.UNDO], -1, -1))
                redo_stack.append((constants.UNDO_MAPPING[constants.REDO], -1, -1))
            elif ch == 9:
                n, m = map(int, raw_input("enter start and end").split(','))
                TextEditorService.delete_range(editor_obj, n, m)
                undo_stack.append((constants.UNDO_MAPPING[constants.DELETE], n, m))
                redo_stack.append((constants.DELETE, n, m))
            elif ch == 10:
                print("exitting")
                ans = False
            else:
                print("Wrong value ..")
            print("------ displaying editor obj ------")
            TextEditorService.display_editor_obj(editor_obj)
