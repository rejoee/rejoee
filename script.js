get = id => document.getElementById(id)
sleep = delay => new Promise((resolve) => setTimeout(resolve, delay))
async function started() {
    for (char of "Regi Weboldala".split("")) {
        get("h1").innerHTML += char;
        await sleep(100);
    }
}

function fooldal() {
    get("fooldal").style.display = "unset";
}
