//for-loop
for(let i =1;i<=5;i++){
    console.log("Iteration number: " + i);
}

//while-loop
let j =1;
while(j<=5){
    console.log("While loop iteration: " + j);
    j++;
}

//do-while-loop
let k =1;
do{
    console.log("Do-While loop iteration: " + k);
    k++;
}while(k<=5);

//for-in loop
let obj = {a:1, b:2, c:3};  
for(let key in obj){
    console.log(key + ": " + obj[key]);
}   
