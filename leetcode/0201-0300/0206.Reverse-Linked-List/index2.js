class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const answer = (head) => {
  // const dummy = new Node(0); // Don't need dummy node
  // dummy.next = head;
  let pre = null;
  let cur = head;
  let next = null; // Don't forget

  // while (cur && cur.next) { // Important! Not this
  while (cur) {
    next = cur.next;
    cur.next = pre;
    pre = cur;
    cur = next;
  }

  // return cur; // Important! Not this
  return pre;
};
