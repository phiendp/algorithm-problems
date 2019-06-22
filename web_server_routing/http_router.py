class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        node = self.root

        for path in paths:
            if path not in node.children:
                node.children[path] = RouteTrieNode()

            node = node.children[path]

        node.handler = handler

    def find(self, paths):
        node = self.root

        for path in paths:
            if path not in node.children:
                return None
            node = node.children[path]

        return node.handler


class Router:
    def __init__(self, handler, not_found_handler="404"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie()
        self.routes.insert('/', handler)
        self.not_found = not_found_handler

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(route)
        self.routes.insert(paths, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(route)
        return self.routes.find(paths) or self.not_found

    def split_path(self, route):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(route) == 1:
            return "/"
        else:
            return route.strip("/").split("/")


# Create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# Some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# Should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# Should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# Should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
