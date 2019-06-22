# HTTPRouter

## Introduction
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure.

## Approach
First, we initialize the routes with RouteTrie, in which there will be a `/` root route and the default `not found` handler. Then, in order to add a handler or to look up for a route, we will use the RouteTrie's `insert` and `find` functionalities, by passing the list of paths that are already splitted by the `/`.

## Analysis
The time complexity and space complexity will be O(1), since a url will not be too long (a few hundred of characters at most) and thus the size of the input does not drastically affect either the space used for creating a RouteTrie, nor the time it needs to lookup a route.
