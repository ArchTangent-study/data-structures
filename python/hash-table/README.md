# Hash Table

Hash Table (Hash Map, Dictionary) implementations in Python, with testing available via `pytest`.

Qualities of a good hash table:
- A low *load factor* (number of items in table / number of slots in table)
- A good *hash function*

Implementations to look at:
- Rust's [Hashbrown](https://github.com/rust-lang/hashbrown) hashmap
- Rust's [AHash](https://github.com/tkaitchuck/aHash) hasher
- [SHA2](https://en.wikipedia.org/wiki/SHA-2)] hash

## Time complexity

| Operation | Best Case  | Worst Case |
| ----------|------------|------------|
| Search    |   `O(1)`   |   `O(n)`   |
| Insert    |   `O(1)`   |   `O(n)`   |
| Delete    |   `O(1)`   |   `O(n)`   |

## Approach

## Visualization

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest hash_table_1.py`
