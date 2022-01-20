

$(document).ready(function(){
 console.log("test.js code in action ")   
    // javascript code for my test page starts here
  let no_of_q = 10
  var static_url = $("#static_url").attr("data-url")
//   console.log(static_url)
//   var static_url = '/media/json_file/english.json'
  var position = 0
  var score = 0
  let jsonarray = []

  var qdiv = document.getElementById("questiondiv")
var optionsdiv = document.getElementById("optionsdiv")
var navqstns = document.getElementById("navqstns")
var positiondiv = document.getElementById("positiondiv")
var item = jsonarray[position]
var nextbtn = document.getElementById("next")
var prevbtn = document.getElementById("prev")
var ajaxbtn = document.getElementById("ajaxbtn")
var infoPanel = document.getElementById("info-panel")
var viewresultdiv = document.getElementById("resultdiv")
var maindiv2 = document.getElementById("main-div2")
var maindiv3 = document.getElementById("main-div3")
// var timebtn = document.getElementById("timebtn")

maindiv3.hidden = true
  
      // ajax function to pull json file from the server
      
      let aj = $.ajax({
        url: static_url,
        async: false,
        dataType: 'json',
        success: function(d){

            console.log("ajax function worked")
            $.each(d, function(i, one){
            // console.log(one)
            jsonarray.push(one)
        })

        },
        error: function(err){
            console.log("ajax error")
            console.log(err)
        }
    })    

    jsonarray = jsonarray.slice(0, 10)
    var item = jsonarray[position]
    // console.log(jsonarray)
    positiondiv.innerHTML = `<button class="btn btn-info p-3" >Question: 1</button>`
    // adding nav buttons to the navqstns div in order to redirect to each question based on click
//     var navbtnshtml = ''
//     for(i=1; i<=jsonarray.length; i++){
//         //console.log(i)
//         navbtnshtml += `<button class="navqstnsbtn" id=${i}>${i}</button>`
//     }
//     navqstns.innerHTML = navbtnshtml

//     let navqstnsbtn = document.querySelectorAll(".navqstnsbtn")
// //console.log(navqstnsbtn[0])
// navqstnsbtn.forEach((btn)=>{
//     btn.addEventListener('click', function(){
//         let btn_id = btn.id
//         //console.log(btn_id)
//         goto(btn_id)
//     })
// })
// console.log(item)
ajaxbtn.addEventListener('click', ajaxfunc)

function ajaxfunc (){
    console.log("ajax btn clicked")
    $.ajax({
        url: '/ajax/',
        type: 'get',
        data: {
            button_text: "ajax button text"
        },
        success: function(response){
            console.log(response)
            alert(response.seconds);
            
        }
    })
}

nextbtn.addEventListener('click', nextAction)
prevbtn.addEventListener('click', prevAction)
infoPanel.innerHTML = `<button class="btn btn-outline-info" id="submit" type="button">Submit Exam</button><button class="btn btn-info" type="button" id="infobtn">Ticked: 0/${jsonarray.length}</button>`
qdiv.innerHTML=`<p class="darktext" id="question">${item.question}</p>`
optionsdiv.innerHTML = `<div id="1"><input class="select" type="radio" value="${item.options.A}" id="A" name="options">
<label for="1">${item.options.A}</label><br></div>
<div id="2"><input class="select" type="radio" value="${item.options.B}" id="B" name="options">
<label for="2">${item.options.B}</label><br></div>
<div id="3"><input class="select" type="radio" value="${item.options.C}" id="C" name="options">
<label for="3">${item.options.C}</label><br></div>
<div id="4"><input class="select" type="radio" value="${item.options.D}" id="D"  name="options">
<label for="3">${item.options.D}</label><br></div>`



var submitbtn = document.getElementById("submit")
submitbtn.addEventListener('click', resultMarker)

function countQuestions(){
    q_count = jsonarray.length
    return q_count;
}
var checkedObject = {}

function updateEventListener(showAnswer=false){
    //console.log('update has been run')
    submitbtn.addEventListener('click', resultMarker)
    let radiobtns = document.querySelectorAll(".select")
    radiobtns.forEach((btn)=>{
        btn.addEventListener('click', function(){
            //console.log('radio has been clicked')
            let question_id = (position + 1)
            //console.log(typeof question_id)
            let btn_id = btn.id
            //console.log(btn_id)
            checkedObject[question_id] = btn_id
            //console.log(checkedObject)
            infoPanel.innerHTML = `<button class="btn btn-outline-info" id="submit" type="button">Submit Exam</button>
            <button class="btn btn-info" id="infobtn" disabled>Ticked: ${Object.keys(checkedObject).length }/${jsonarray.length}</button>`
            let submitbtn = document.getElementById("submit")
            submitbtn.addEventListener('click', resultMarker)

            //console.log(checkedObject)
            if(jsonarray[question_id-1].answer == btn_id){
                //console.log("correct")
            }
            else{
                //console.log("not correct")
            }
            //console.log(data[question_id-1].answer)
        })
    })
    if(showAnswer == true){
        $("#submit").text("Go Back")
        $("#submit").bind('click', function(){
            location.reload(true)
        })
        //$("#submit").prop("disabled", true)
        //let s = $("input.select")
        //console.log(s)
        $("input.select").each(function(){
            $(this).prop("disabled", true)
        })
    }

}
updateEventListener()


function resultMarker(){
    // clearInterval(intvl)
    let answered = Object.keys(checkedObject).length
    let check_keys = Object.keys(checkedObject)
    check_keys.forEach((k)=>{
        let val = checkedObject[k]
        //console.log(val)
        if (jsonarray[k-1].answer == val){
            score = score + 1
        }
        else{
            // do nothing
        }

    })
    //console.log(score)
    maindiv2.hidden = true
    maindiv3.hidden = false
    viewresultdiv.innerHTML = `<p class="stylep">Test Completed!!!</p>
    
    <p>You Scored: <b>${score}/${jsonarray.length}<b></p>

    <div class="retrydiv">
    <button class="btn btn-sm btn-info" id="retrybtn"> Retry</button>
    <button class="btn btn-sm  btn-info" id="correctbtn">View Correction</button>
    <button class="btn btn-sm btn-info" id="backbtn"> Go Back</button>

    </div>
    `

    let correctbtn = document.getElementById("correctbtn")
    let retrybtn = document.getElementById("retrybtn")
    let gobackbtn = document.getElementById("backbtn")
    //console.log(correctbtn)
    gobackbtn.addEventListener('click', function(){
        location.reload(true)
    })
    retrybtn.addEventListener('click', function(){
        location.reload(true)
    })
    correctbtn.addEventListener('click', correction)
    

}


function idToAlpha(id){
    if (id=="A"){
        return "one"
    }
    else if(id =="B"){
        return "two"
    }
    else if(id =="C"){
        return "three"
    }
    else if(id == "D"){
        return "four"
    }
    else{
        //console.log("no id presented")
    }
}


`<p class="question darktext" id="question">${item.question}</p>`
optionsdiv.innerHTML = `<div id="1"><input class="select" type="radio" value="${item.options.A}" id="A" name="options">
<label for="1">${item.options.A}</label><br></div>
<div id="2"><input class="select" type="radio" value="${item.options.B}" id="B" name="options">
<label for="2">${item.options.B}</label><br></div>
<div id="3"><input class="select" type="radio" value="${item.options.C}" id="C" name="options">
<label for="3">${item.options.C}</label><br></div>
<div id="4"><input class="select" type="radio" value="${item.options.D}" id="D"  name="options">
<label for="3">${item.options.D}</label><br></div>`


function idToIndex(id){
    if (id=="A"){
        return 1
    }
    else if(id =="B"){
        return 2
    }
    else if(id =="C"){
        return 3
    }
    else if(id == "D"){
        return 4
    }
    else{
        //console.log("no id presented")
    }
}

function saveChecked(index, showAnswer = false){
    //console.log("save just ran")
    if(index in checkedObject){
        selectedRadId = checkedObject[index]
        //console.log(selectedRadId)
        //
        let i = document.querySelector(`input[id=${selectedRadId}]`)
        //console.log(checkedObject[index])
        //console.log(data[index-1].answer)

        i.checked = true;


        //console.log(d)
        if(showAnswer == true){
            if (checkedObject[index] == jsonarray[index-1].answer){
                $(`div#${idToIndex(i.id)}`).css("background-color", "green")
            }
            else{
                $(`div#${idToIndex(i.id)}`).css("background-color", "red")
            }
            $(`div#${idToIndex(jsonarray[index-1].answer)}`).css("background-color", "green")
        }
    }
    if(showAnswer == true){
        $(`div#${idToIndex(jsonarray[index-1].answer)}`).css("background-color", "green")
    }


}


function goto(index, showAnswer = false){
    //console.log(`index: ${index}`)

    // navqstnsbtn.forEach((btn)=>{
    //   btn.classList.remove("btn","btn-sm","btn-info")
    // })
    //console.log("navbtns classes updated")
    position = index-1
    let item = jsonarray[position]
    qdiv.innerHTML=`<p class="question" id="question">${item.question}</p>`
    positiondiv.innerHTML = `<button class="btn btn-info p-3" >Question: ${index}</button>`
    optionsdiv.innerHTML = `<div id="1"><input class="select" type="radio" value="${item.options.A}" id="A" name="options">
    <label for="1">${item.options.A}</label><br></div>
    <div id="2"><input class="select" type="radio" value="${item.options.B}" id="B" name="options">
    <label for="2">${item.options.B}</label><br></div>
    <div id="3"><input class="select" type="radio" value="${item.options.C}" id="C" name="options">
    <label for="3">${item.options.C}</label><br></div>
    <div id="4"><input class="select" type="radio" value="${item.options.D}" id="D"  name="options">
    <label for="3">${item.options.D}</label><br></div>`

    //let current_navbtn = $(`.navqstnsbtn#${index}`)
    // current_navbtn  = navqstnsbtn[position]
    // current_navbtn.classList.add("btn", "btn-sm", "btn-info")
    //console.log(current_navbtn)
    //current_navbtn.addClass("btn btn-sm btn-info")
    //console.log(item.options.A)
    // MathJax.typeset()
    saveChecked(index, showAnswer)
    updateEventListener(showAnswer)

    //current_navbtn.addClass("btn btn-sm btn-info")
    //console.log(current_navbtn)
    if(showAnswer == true){
        console.log("button will be disabled")
        //$("#submit").prop("disabled", true)
        //console.log(submitbtn)
    }

}


function nextAction(showAnswer = false){


    let q_count = countQuestions()

    if (position == (q_count - 1)){
        //console.log(q_count)
        position = (q_count - 1)
    }
    else{
        position = position + 1

    }
    goto(position + 1, showAnswer)

}


function prevAction(showAnswer = false){

    if (position == 0){
        position = 0
    }
    else{
    position = position - 1

    }
    goto(position + 1, showAnswer)
    //console.log(position)
    //updateEventListener()
    //let index=position + 1
    //saveChecked(index)

}


  // javascript code for my test page ends  here

})