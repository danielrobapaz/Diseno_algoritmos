#include <bits/stdc++.h>
using namespace std;

struct Node {
	int val;
	int weight, size;
	Node *left, *right;
	Node(int c) : val(c), weight(rand()), size(1), left(NULL), right(NULL) {}
} *root;

inline int size(Node *treap) { return treap ? treap->size : 0; }

void split(Node *treap, Node *&left, Node *&right, int val) {
	if (!treap) {
		left = right = NULL;
		return;
	}

	if (size(treap->left) < val) {
		split(treap->right, treap->right, right, val - size(treap->left) - 1);
		left = treap;
	} else {
		split(treap->left, left, treap->left, val);
		right = treap;
	}
	treap->size = 1 + size(treap->left) + size(treap->right);
}

void merge(Node *&treap, Node *left, Node *right) {
	if (left == NULL) {
		treap = right;
		return;
	}
	if (right == NULL) {
		treap = left;
		return;
	}

	if (left->weight < right->weight) {
		merge(left->right, left->right, right);
		treap = left;
	} else {
		merge(right->left, left, right->left);
		treap = right;
	}
	treap->size = 1 + size(treap->left) + size(treap->right);
}

ostream &operator<<(ostream &os, Node *n) {
	if (!n) return os;
	os << n->left;
	os << n->val;
	os << n->right;
	return os;
}

void multiswap(Node *&treap, int a, int b) {
    int segment_a, segment_b, segment_size;
    Node *treap_a, *treap_b, *treap_c, *treap_d, *treap_e, *treap_f;
    segment_a = b-a;
    segment_b = treap->size - b;

    segment_size = segment_a;
    if (segment_b < segment_a) {segment_size = segment_b;}

    /* Dado un a y b se puede dividir el array de la siguiente manera.
       [0..a) [a..a+segment_size) [a+segment_size..b) [b..b+segment_size) [b+segment_size..N)
       siendo N el tamano del array
       
        Dependiendo de los casos hay subarrays que pueden ser vacios
    */
    if (a+segment_size == b){
        // [a_segment_size..b) es vacio 
        split(treap, treap_a, treap_b, b); 
        split(treap_a, treap_c, treap_d, a);
        split(treap_b, treap_e, treap_f, segment_size);

        merge(treap, treap_c, treap_e);
        merge(treap_d, treap_d, treap_f);
        merge(treap, treap, treap_d);
    
    } else if (b+segment_size) {
        split(treap, treap_a, treap_b, b);
        split(treap_a, treap_c, treap_d, a);
        split(treap_d, treap_e, treap_f, segment_size);

        merge(treap_c, treap_c, treap_b);
        merge(treap_c, treap_c, treap_f);
        merge(treap, treap_c, treap_e);
    }
}

int main() {
	int N, M, a, b;

    cin >> N;
    cin >> M;

	int S[N];

    for (int i=0; i<N; i++) {merge(root, root, new Node(i)); }
    
    for (int i=0; i<M; i++) {
        cin >> a >> b;
        multiswap(root, a, b);
    }
    cout << root << '\n';
}