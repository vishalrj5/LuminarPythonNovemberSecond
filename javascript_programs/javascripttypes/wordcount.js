var text = "hello hai hello how";
var word = text.split(" ");
console.log("Text has ", word.length, " words");
console.log(word);
dict={};
for (i = 0; i < word.length; i++) {
    var cnt = 0;
    for (j = 0; j < word.length; j++) {

        // console.log(word[i],word[j])
        if (word[i] == word[j]) {
            cnt = cnt + 1
            if(word in dict)
            {
                console.log("ifffffffffffffffffffffffffff")
                continue;
                
            }
            else{
                 dict[word[i]]=cnt
                }      
            //     }
    
            

        }


    }
    console.log(word[i], "has a count of ", cnt)
}
console.log("word count is \n", dict)