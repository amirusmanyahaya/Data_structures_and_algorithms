#include <iostream>

using namespace std;

// Insertion sort in acesing order
void InsertionSort(int *arr){
    for(int i{1}; i < 6; i++){
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = key;
    }

}

// Insertion sort in reverse order
void InsertionSortReverse(int *arr){
    for (int i{1}; i < 6; ++i){
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] < key){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

void print_array(int *arr){
    for(int i{0}; i < 6 ; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}


int main(){

    int arr[] = {31,41,59,26,41,58};

    InsertionSort(arr);
    // output = 26,31,41,41,58,59
    print_array(arr);
    InsertionSortReverse(arr);
    // output = 59,58,41,41,31,26
    print_array(arr);
    return 0;
}