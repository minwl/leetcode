int maxArea(int* height, int heightSize){

int i = 0;
int j = heightSize-1;
int maxwater = 0;
int min_height;
while(i<j){
    
    if (height[i]<height[j]) min_height = height[i];
    else min_height = height[j];

    //최초 상태에서의 넓이로 시작
    int area = (j-i) * min_height; 

    if (maxwater< area) {maxwater = area;} //find max water 

    //두개 벽중 더 낮은 거를 버리고 pointer 이동
    if (height[i]<height[j]) i++; 
    else j --; //

}

return maxwater;
}