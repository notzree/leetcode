class ArrayWrapper {
    a: number[]
	constructor(nums: number[]) {
        this.a = nums
    }

	valueOf() { //overrides what adding does
        //return the sum of the array
        //Runs reducer function on all elements of array.
        //Basically:
        //psum = psum+a[i] for i in a
        return this.a.reduce((psum,a)=>psum+a,0)
    }

	toString() {
        let t = ""
        this.a.forEach((i)=>{
            t+=i.toString()+ ","
        })
        t = t.substring(0,t.length-1)
        return "[" + t + "]"
        
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */