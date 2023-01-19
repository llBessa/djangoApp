function showPopMessage(){
    // busca parametros na url
    let params = new URLSearchParams(window.location.search)
    if(params.get("popmessage")){
        // elemento da mensagem
        let flexMessage = document.createElement("div")
        flexMessage.style.display = "flex"
        flexMessage.style.justifyContent = "center"

        let popMessage = document.createElement("div")
        popMessage.className = `message-${params.get("poptype")}`
        popMessage.innerText = params.get("popmessage")

        flexMessage.appendChild(popMessage)

        // apresentação e remoção do elemento
        let mainTag = document.getElementsByTagName("main")[0]
        popMessage.onanimationend = (e) => {
            mainTag.removeChild(flexMessage)

            // limpa a url para impedir a reexibição da mensagem
            const url = new URL(window.location)
            url.search = ""
            window.history.replaceState(null, null, url)
        }
        mainTag.appendChild(flexMessage)
    }
}

function copyPassword(senhaId){
    var copyText = document.getElementById(senhaId);

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
  
     // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);
    console.log("passou")
}

export {showPopMessage, copyPassword};