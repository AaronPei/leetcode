public static int binSearch(int[] array,int key){
	int start=0;
	int mid;
	int end=array.length-1;
	while(start<=end){
		mid=(end-start)/2+start;
		if(key<array[mid]){
			end=mid-1;
		}
		else if(key>array[mid]){
			start=mid+1;
		}else{
			return mid;
		}
	}
	return -1;
}