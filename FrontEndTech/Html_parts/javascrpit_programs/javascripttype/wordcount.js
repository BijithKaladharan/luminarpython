var text="hello hai hello how"
var word=text.split(" ")

var went()
for(let wrd of word){
    if(wrd in went){
        went[wrd]+=1;

    }
    else{
        went[wrd]=1
    }
}
console.log(went)