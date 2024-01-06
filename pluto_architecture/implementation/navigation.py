'''
this file "navigation" handles the navigation in the framework
'''
class NavigationManager:
    '''this is the navigation manager handler class'''
    def __init__(self):
        self.stack = []

    def push_screen(self, screen):
        '''stacks a screen on top of the another'''
        self.stack.append(screen)

    def pop_screen(self):
        '''removes the top screen in the screen'''
        if self.stack:
            self.stack.pop()

    def get_current_screen(self):
        '''
        returns the current screen or the screen on top
        of the stack
        '''
        return self.stack[-1] if self.stack else None
