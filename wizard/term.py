from simple_term_menu import TerminalMenu

def multi_select(options, title):
    terminal_menu = TerminalMenu(
        options,
        title=title,
        multi_select=True,
        show_multi_select_hint=True,
        show_search_hint=True
    )
    menu_entry_indices = terminal_menu.show()
    return terminal_menu.chosen_menu_entries