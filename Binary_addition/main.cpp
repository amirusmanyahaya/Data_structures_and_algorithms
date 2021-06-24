#include <iostream>
#include <string>

int *sum(int *arr1,int *arr2, int size){
    int *sum_array = new int[size+1];
    // holds the carray value
    int rem{0};
    int value{0};
    // for each element from sum their values
    for(int i{size - 1}; i >= 0; --i){
        value = arr1[i]+arr2[i]+rem;
        if(value > 1){
            if (value % 2 == 0){
                value = 0;
            }else{
                value = 1;
            }
            rem = 1;
        }else{
            rem = 0;
        }

        sum_array[i+1] = value;
    }
    sum_array[0] = rem;
    return sum_array;
}

int main(){
    int n{4};
    int arr1[] = {1,0,0,1};
    int arr2[] = {1,1,0,1};
    
    int *my_sum_arr = sum(arr1,arr2,n);
    for(int i{0}; i < 5; ++i){
        std::cout << my_sum_arr[i] << " ";
    }
    std::cout <<"\n";
    delete my_sum_arr;
    return 0;
}