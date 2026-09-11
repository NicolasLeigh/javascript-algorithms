class ListNode {
  constructor(key, val) {
    this.key = key;
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.map = new Map();

    this.head = new ListNode(0, 0);
    this.tail = new ListNode(0, 0);

    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  _remove(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  _addToHead(node) {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next.prev = node;
    this.head.next = node;
  }

  get(key) {
    if (!this.map.has(key)) return -1;
    const node = this.map.get(key);
    this._remove(node);
    this._addToHead(node);
    return node.val;
  }

  put(key, value) {
    if (this.map.has(key)) this._remove(this.map.get(key));
    const newNode = new ListNode(key, value);
    this._addToHead(newNode);
    this.map.set(key, newNode); // Don't forget

    if (this.map.size > this.capacity) {
      const lru = this.tail.prev;
      this._remove(lru);
      this.map.delete(lru.key); // Don't forget
    }
  }
}
