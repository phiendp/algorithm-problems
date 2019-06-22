# Autocomplete with Tries

## Introduction
A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
We want to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

## Approach
The suffixes function will recursively go down the trie and appending its children to a partial result list on the way.

## Analysis
Let N be the number of characters from the input list of words. The time complexity will be O(N), since we have to traverse all of the children when building the suffices. The space complexity will be O(N) as well, since we will create a new array for every node in the children.
