// Arrow functions

const func = () => {
    console.log("hello world");
}
const component = (a, b) => {
    return a+b;
}
// export const c1 = (a, b) => {
//     return a+b;
// }

{/* <button onclick = {
    () => {
        console.log("hello");
    }
}>
</button> */}

// --------------------------------------------------------------------------------------------------------------
// let age1 = 11;
// let div1 = 10, div2 = 100;

// let n = age1 == 10 && 10;
// let x = age1 == 11 || "abdul raheem";
// let name1 = age1 == 10 ? "10" : "not 10";

// const comp1 = () => {
//     return age1 = 11 ? div1 : div2;
// }
// console.log(comp1());

// --------------------------------------------------------------------------------------------------------------
// const hardworking = true;
// const person = {
//     name: "abdul raheem",
//     age: 1,
//     hardworking: true,
// };

// const {name, age, hardworking} = person ;

// const person2 = {
//     ...person, age: 10
// };
// console.log(person2);

const array = [1,2,3,4];
const nums = [...array,5];
// console.log(nums);


// --------------------------------------------------------------------------------------------------------------
// map, filter
names = ["AR","AS","ASDS"];
new_nums = nums.map((i) => {
    return i*10;
});

new_names = names.filter((name) => {
    return name != "AR";
});

nums2 = new_nums.filter((i) => {
    return i > 10;
});





































