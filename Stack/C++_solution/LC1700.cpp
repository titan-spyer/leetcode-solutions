

#include <vector>
using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        // PHASE 1: TAKE INVENTORY
        int count_0 = 0;
        int count_1 = 0;

        // Loop through the 'students' array:
        for (int student : students) {
            if (student == 0) {
                count_0++;
            } else {
                count_1++;
            }
        }

        // PHASE 2: SERVE THE SANDWICHES
        for (int sandwich : sandwiches) {
            if (sandwich == 0) {
                if (count_0 > 0) {
                    count_0--;
                } else {
                    break;
                }
            } else {
                if (count_1 > 0) {
                    count_1--;
                } else {
                    break;
                }
            }
        }

        // PHASE 3: THE AFTERMATH
        return count_0 + count_1;
    }
};