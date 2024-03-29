
// source = https://thepracticetest.com/typing/tests/practice-paragraphs/
// ########### SETTING CONSTANTS ###########

$(document).ready(function(){
    // source = https://thepracticetest.com/typing/tests/practice-paragraphs/
const paragraphs = [
    "An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission. One example: Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets. Products on the market must reveal the names of all ingredients on the label. Language must be in clear and precise terms that can be understood by everyone. This practice is very crucial for the lives of many people. It is prudent that we recall that the FDA specifically requires that all goods are pure, safe, and wholesome. The FDA states that all goods be produced under highly sanitary conditions. Drugs must be completely safe and must also be effective for their stated purpose. This policy applies to cosmetics that must be both safe and pure. Individuals are often totally unappreciative of the FDA's great dedication.",
    "Editing is a growing field of work in the service industry. Paid editing services may be provided by specialized editing firms or by self-employed (freelance) editors. Editing firms may employ a team of in-house editors, rely on a network of individual contractors or both. Such firms are able to handle editing in a wide range of topics and genres, depending on the skills of individual editors. The services provided by these editors may be varied and can include proofreading, copy editing, online editing, developmental editing, editing for search engine optimization (SEO), etc. Self-employed editors work directly for clients or offer their services through editing firms, or both. They may specialize in a type of editing and in a particular subject area. Those who work directly for authors and develop professional relationships with them are called authors' editors.",
    "Income before securities transactions was up 10.8 percent from $13.49 million in 1982 to $14.95 million in 1983. Earnings per share (adjusted for a 10.5 percent stock dividend distributed on August 26) advanced 10 percent to $2.39 in 1983 from $2.17 in 1982. Earnings may rise for 7 years. Hopefully, earnings per share will grow another 10 percent. Kosy, Klemin, and Bille began selling on May 23, 1964. Their second store was founded in Renton on August 3, 1965. From 1964 to 1984, they opened more than 50 stores through-out the country. As they expanded, 12 regional offices had to be organized. Each of these 12 regional offices had to be organized. Each of these 12 regions employs from 108 to 578 people. National headquarters employs 1,077 people. Carole owns 118 stores located in 75 cities ranging as far west as Seattle and as far east as Boston. She owns 46 stores south of the Mason-Dixon line and 24 stores north of Denver. Carole buys goods from 89 companies located in 123 countries and all 50 states. Carole started in business on March 3, 1975. She had less than $6,000 in capital assets.",
    "Historically, the fundamental role of pharmacists as a healthcare practitioner was to check and distribute drugs to doctors for medication that had been prescribed to patients. In more modern times, pharmacists advise patients and health care providers on the selection, dosages, interactions, and side effects of medications, and act as a learned intermediary between a prescriber and a patient. Pharmacists monitor the health and progress of patients to ensure the safe and effective use of medication. Pharmacists may practice compounding; however, many medicines are now produced by pharmaceutical companies in a standard dosage and drug delivery form. In some jurisdictions, pharmacists have prescriptive authority to either independently prescribe under their own authority or in collaboration with a primary care physician through an agreed upon protocol.",
    "Jim and Anne will be in charge of the spring field day to be held in early June. They will ask their friends' aid to get set up. There will be games for the boys and girls. The children will want to hike, ride their bikes, and swim. This yearly event will be held in the new Peach Grove Park. Ruth has work to do on the plans for food for the day. Last year Ruth spent most of her time helping the two cooks with many snacks. Hot dogs, fries, soft drinks, ice cream, and candy apples were big sellers. Apple pie and ice cream sold well too. I hope Ruth serves the same food this year. George Long will hire the band and singer for the day. A great jazz band will play. George's mom leads the group. The jazz band is sure to be one of the big hits. George is to have them play from one to four and also in the evening. The fine songs they will play are sure to please all of us. Nice gifts will be given to all of the winners in each of the events. Local news coverage will include television and newspapers. Joyce Scott will take care of the pictures for the school paper and yearbook. Maybe the national news will do a short story on the tenth annual spring field day.",
    "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study, \"The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed... fast typists... keep their hands fixed on one position, instead of moving them over the keyboard, and more consistently use the same finger to type a certain letter.\" To quote doctoral candidate Anna Feit: \"We were surprised to observe that people who took a typing course, performed at similar average speed and accuracy, as those that taught typing to themselves and only used 6 fingers on average\" (Wikipedia)",
    "Business meetings, and professional recordings can contain sensitive data, so security is something a transcription company should not overlook when providing services. Companies should therefore follow the various laws and industry best practice, especially so when serving law firms, government agencies or courts. Medical Transcription specifically is governed by HIPAA, which elaborates data security practices and compliance measures to be strictly followed, failure of which leads to legal action and penalties. Transcription security includes maintaining confidentiality of the data through information security practices including limiting access with passwords and ensuring a secure environment for data and appropriate methods of disposal of all materials and deletion of files. Personnel may be required to sign non-disclosure agreements on a regular basis as well as take various oaths regarding confidentiality and accuracy."
];
const typingText = document.querySelector(".typing-text p");
inputField = document.querySelector(".wrap .input-field");
mistakeTag = document.querySelector(".mistake span");
timeTag = document.querySelector(".time span b");
cpmTag = document.querySelector(".cpm span");
wpmTag = document.querySelector(".wpm span");
tryAgainButtonTag = document.querySelector(".try-again-button")

//let timer, maxTime = 60;    // set timer limit (in seconds)
let timer, maxTime = 10;
let timeLeft = maxTime;
let charIndex = mistakes = 0;
let isTyping = false;


// ########### GAME LOGIC ###########

function generateRandomParagraph() {
    $.ajax({
        type: 'GET',
        url: '/game-text',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
    })
    .done(function(data){
        typingText.innerHTML = "";
        if(data.error){

            console.log('generating paragraphs in html')

            // generate random number to get a random paragraph above
            let randIndex = Math.floor(Math.random() * paragraphs.length);

            // split all chars in random paragraph in to spans and add them inside <p>
            paragraphs[randIndex].split("").forEach(span => {
                let spanTag = `<span>${span}</span>`;
                typingText.innerHTML += spanTag;

            });
        }else{
            data.paragraph.split("").forEach(span => {
                let spanTag = `<span>${span}</span>`;
                typingText.innerHTML += spanTag;

            });
        }
        typingText.querySelectorAll("span")[0].classList.add("active");
        // when a key is pressed or mouse clicked focus on the input field so they
        // can type and begin the test without clicking the space
        //document.addEventListener("keydown", () => inputField.focus());
        typingText.addEventListener("click", () => inputField.focus());
    })


    /*
    // generate random number to get a random paragraph above
    let randIndex = Math.floor(Math.random() * paragraphs.length);
    typingText.innerHTML = "";
    // split all chars in random paragraph in to spans and add them inside <p>
    paragraphs[randIndex].split("").forEach(span => {
        let spanTag = `<span>${span}</span>`;
        typingText.innerHTML += spanTag;
    });
    typingText.querySelectorAll("span")[0].classList.add("active");
    // when a key is pressed or mouse clicked focus on the input field so they
    // can type and begin the test without clicking the space
    //document.addEventListener("keydown", () => inputField.focus());
    typingText.addEventListener("click", () => inputField.focus());
    */
}

function  initiateTyping() {
    const characters = typingText.querySelectorAll("span");
    let typedChar = inputField.value.split("")[charIndex];
    if (charIndex < characters.length -1 && timeLeft > 0) {
        if (!isTyping) {
            timer = setInterval(initiateTimer, 1000);
            isTyping = true;
        }
        if (typedChar == null) {
            charIndex -= 1;
            // make sure to only remove mistake count if class incorrect is there
            if (characters[charIndex].classList.contains("incorrect")) {
                mistakes -= 1;
            }
            characters[charIndex].classList.remove("correct", "incorrect");
        } else {
            if (characters[charIndex].innerText === typedChar) {
                characters[charIndex].classList.add("correct");
            } else {
                mistakes += 1;
                characters[charIndex].classList.add("incorrect");
            }
            charIndex += 1;
        }
        
        characters.forEach(span => span.classList.remove("active"));
        characters[charIndex].classList.add("active");
    
        let wpm = Math.round((((charIndex - mistakes) / 5) / (maxTime - timeLeft)) * 60);
        // having issues with infinity showing up so making it 0 until a nice number appears
        if (wpm < 0 || !wpm || wpm === Infinity) {
            wpm = 0;
        }
        mistakeTag.innerText = mistakes;
        wpmTag.innerText = wpm;
        cpmTag.innerText = charIndex - mistakes;
    } else {
        // here is where we need to submit results as the timer has ended.
        saveResults(mistakeTag.innerText, wpmTag.innerText, cpmTag.innerText)
        console.log("game finished.")
        restartGame()
        /*
        inputField.value = "";    // clear input field ready for new test
        clearInterval(timer);
        */
    }
}

function initiateTimer() {
    if (timeLeft > 0) {
        timeLeft -= 1;
        timeTag.innerText = timeLeft;
    } else {
        clearInterval(timer);
    }
};

function saveResults(mistakeResult, wpmResult, cpmResult) {
    $.ajax({
        type: "POST",
        headers: {"Content-Type": "application/json"},
        url: "/stat",
        data: JSON.stringify({mistake: mistakeResult, wpm: wpmResult, cpm: cpmResult}),
        success: function(response) {
            console.log(response);
    },
    error: function(response, error) {
        console.log(response);
        console.log(error);
    }
});
}


// reset vars and elements
// gen new text paragraph
function restartGame() {
    generateRandomParagraph();
    inputField.value = "";
    clearInterval(timer);
    timeLeft = maxTime;
    charIndex = mistakes = 0;
    isTyping = false;
    timeTag.innerText = timeLeft;
    mistakeTag.innerText = mistakes;
    wpmTag.innerText = 0;
    cpmTag.innerText = 0;
}

generateRandomParagraph();
inputField.addEventListener("input", initiateTyping);
inputField.addEventListener("click", initiateTyping);
tryAgainButtonTag.addEventListener("click", restartGame);


})

