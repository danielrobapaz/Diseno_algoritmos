#include <iostream>
#include <stack>
#include <stdlib.h>
using namespace std;
 
struct Point {
    int x, y;
};
 
// A global point needed for  sorting points with reference
// to  the first point Used in compare function of qsort()
Point p0;
 
// A utility function to find next to top in a stack
Point nextToTop(stack<Point> &S) {
    Point p = S.top();
    S.pop();
    Point res = S.top();
    S.push(p);
    return res;
}
 
// A utility function to swap two points
void swap(Point &p1, Point &p2) {
    Point temp = p1;
    p1 = p2;
    p2 = temp;
}
 
// A utility function to return square of distance
// between p1 and p2
int distSq(Point p1, Point p2) {
    return (p1.x - p2.x)*(p1.x - p2.x) +
          (p1.y - p2.y)*(p1.y - p2.y);
}
 
// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are collinear
// 1 --> Clockwise
// 2 --> Counterclockwise
int orientation(Point p, Point q, Point r) {
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);
 
    if (val == 0) return 0;  // collinear
    return (val > 0)? 1: 2; // clock or counterclock wise
}
 
// A function used by library function qsort() to sort an array of
// points with respect to the first point
int compare(const void *vp1, const void *vp2) {
   Point *p1 = (Point *)vp1;
   Point *p2 = (Point *)vp2;
 
   // Find orientation
   int o = orientation(p0, *p1, *p2);
   if (o == 0)
     return (distSq(p0, *p2) >= distSq(p0, *p1))? -1 : 1;
 
   return (o == 2)? -1: 1;
}
 
// Prints convex hull of a set of n points.
stack<Point> convexHull(stack<Point> s, int n) {
   Point points[s.size()];

   int i=0;
   while (!s.empty()) {
    points[i] = s.top();
    s.pop();
    i++;
   }

   // Find the bottommost point
   int ymin = points[0].y, min = 0;
   for (int i = 1; i < n; i++)
   {
     int y = points[i].y;
 
     // Pick the bottom-most or choose the left
     // most point in case of tie
     if ((y < ymin) || (ymin == y &&
         points[i].x < points[min].x))
        ymin = points[i].y, min = i;
   }
 
   // Place the bottom-most point at first position
   swap(points[0], points[min]);
 
   // Sort n-1 points with respect to the first point.
   // A point p1 comes before p2 in sorted output if p2
   // has larger polar angle (in counterclockwise
   // direction) than p1
   p0 = points[0];
   qsort(&points[1], n-1, sizeof(Point), compare);
 
   
   stack<Point> S, S_;

   S.push(points[0]);
 
   // Process remaining m-3 points
   for (int i = 1; i < n; i++)
   {
      // Keep removing top while the angle formed by
      // points next-to-top, top, and points[i] makes
      // a non-left turn
      while (S.size()>1 && orientation(nextToTop(S), S.top(), points[i]) != 2) {
        S_.push(S.top());
        S.pop();
      }
      S.push(points[i]);
   }
 
   // Now stack has the output points, print contents of stack
   return S_;
}
 
// Driver program to test above functions
int main() {
    int N, x, y, number_of_layers;

    cin >> N;
    
    stack<Point> points;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        points.push({x, y});
    }
    number_of_layers = 1;
    while (1) {
        points = convexHull(points, points.size());
        if (points.empty()) {
            break;
        }
        number_of_layers++;
    }

    cout << "El conjunto de puntos tiene: " << number_of_layers << " capa(s)" << endl;

    return 0;
}