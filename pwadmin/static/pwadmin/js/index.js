window.onload = () => {
    let params = new URLSearchParams(window.location.search)
    if(params.get("pop_message"))
        alert(params.get("pop_message"))
}